#!/usr/bin/env python3
"""Build the Anthropic-directory edition of the caffeinity plugin into plugin/.

    python scripts/build.py PATH/TO/caffeinity-skills/plugins/caffeinity
    python scripts/build.py SRC --check     # exit 1 if plugin/ is stale

A non-Verified organization may ship only Markdown, text, JSON, YAML and images, with no install
or launcher commands, no piping downloads into an interpreter and no credentials read from the
environment, even in documentation. A skill is copied only when every file passes; the rest are
listed with their reasons in EXCLUDED.md, which is the to-do list for fixing them at their source
repos. Fix a skill there and the next sync includes it.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "plugin"
ALLOWED_EXT = {".md", ".txt", ".json", ".yaml", ".yml", ".png", ".jpg", ".jpeg", ".gif", ".webp"}
TEXT_EXT = {".md", ".txt", ".json", ".yaml", ".yml"}
DROP = {".gitignore", ".DS_Store", "Thumbs.db", "desktop.ini"}  # dropped silently, never shipped
PKG_FILES = re.compile(r"^(package(-lock)?\.json|requirements.*\.txt|pnpm-.*\.yaml|yarn\.lock|.*\.lock|\.npmrc|bunfig\.toml|uv\.toml|pyproject\.toml)$")
MAX_BYTES = 256 * 1024
# ponytail: regex screen, not the directory's scanner; the validator stays the final word.
RULES = [
    ("install or launcher command", re.compile(
        r"\b(npx|bunx|uvx|pnpm dlx|yarn dlx|pipx run|uv run|uv pip|npm (i|install|ci)|pip3? install"
        r"|brew install|pnpm (add|install)|yarn add|cargo install|go install|gem install|apt(-get)? install)\b")),
    ("pipes into a shell or interpreter", re.compile(r"\|\s*(sudo\s+)?(ba|z)?sh\b|\|\s*(python3?|node|iex)\b")),
    ("credential from the environment", re.compile(r"\b[A-Z][A-Z0-9_]*(TOKEN|SECRET|API_KEY|PASSWORD|ACCESS_KEY)\b")),
]
MANIFEST_KEYS = ["name", "displayName", "version", "description", "author", "homepage", "repository",
                 "license", "keywords", "icon", "documentationUrl", "supportUrl"]


def frontmatter(text):
    """(dict, body) for a file that starts with a --- block, else (None, text)."""
    m = re.match(r"---\r?\n(.*?)\r?\n---\r?\n?", text, re.S)
    if not m:
        return None, text
    return yaml.safe_load(m.group(1)) or {}, text[m.end():]


def check_skill(d):
    """Reasons this skill folder cannot ship; empty when it can."""
    why = set()
    for f in sorted(p for p in d.rglob("*") if p.is_file() and p.name not in DROP):
        rel = f.relative_to(d).as_posix()
        if f.suffix.lower() not in ALLOWED_EXT:
            why.add(f"ships a {f.suffix or f.name} file ({rel})")
            continue
        if PKG_FILES.match(f.name):
            why.add(f"package-manager file ({rel})")
        if f.stat().st_size > MAX_BYTES:
            why.add(f"file over 256 KiB ({rel})")
        if f.suffix.lower() not in TEXT_EXT:
            continue
        text = f.read_text(encoding="utf-8-sig", errors="replace")
        if text.startswith("#!"):
            why.add(f"starts with #! ({rel})")
        for i, line in enumerate(text.splitlines(), 1):
            for label, rx in RULES:
                if rx.search(line):
                    why.add(f"{label} ({rel}:{i})")
    try:
        meta, _ = frontmatter((d / "SKILL.md").read_text(encoding="utf-8-sig"))
        if not meta or not isinstance(meta.get("description"), str):
            why.add("SKILL.md frontmatter has no text description")
    except (OSError, yaml.YAMLError) as e:
        why.add(f"SKILL.md unreadable: {e.__class__.__name__}")
    return sorted(why)


def write_skill(src, dst):
    for f in src.rglob("*"):
        if not f.is_file() or f.name in DROP:
            continue
        t = dst / f.relative_to(src)
        t.parent.mkdir(parents=True, exist_ok=True)
        if f.name == "SKILL.md":
            meta, body = frontmatter(f.read_text(encoding="utf-8-sig"))
            # Only name and description: the directory refuses keys outside its list for non-Verified orgs.
            desc = " ".join(meta["description"].split())
            fm = f"---\nname: {meta.get('name', src.name)}\ndescription: {json.dumps(desc, ensure_ascii=False)}\n---\n"
            t.write_text(fm + body.lstrip("\r\n").replace("\r\n", "\n"), encoding="utf-8", newline="\n")
        elif f.suffix.lower() in TEXT_EXT:
            t.write_text(f.read_text(encoding="utf-8-sig").replace("\r\n", "\n"), encoding="utf-8", newline="\n")
        else:
            shutil.copyfile(f, t)


def readme(included):
    rows = "\n".join(f"- **{n}**: {d}" for n, d in included)
    return f"""# Caffeinity skills (directory edition)

{len(included)} agent skills for Claude Code by Abdul Rahman P Z: writing and content, search
visibility, release checks, research and decisions, careers, outbound and learning. Every skill
is plain Markdown. Nothing in this plugin runs code, installs packages, sends data anywhere or
reads credentials: each skill is instructions and reference notes that Claude reads when the
task matches its description.

This is the subset of the full Caffeinity collection that meets the Claude directory's rules for
plain-Markdown plugins. The full collection, with scripts and workflow agents, is at
[github.com/arm-pz/caffeinity-skills](https://github.com/arm-pz/caffeinity-skills). Each skill has
its own page, source repo and trigger tests at [skillsmith.tech](https://skillsmith.tech/).

## Skills

{rows}

## License

MIT. See LICENSE.
"""


def build(src, out):
    included, excluded = [], {}
    for d in sorted(p for p in (src / "skills").iterdir() if (p / "SKILL.md").is_file()):
        why = check_skill(d)
        if why:
            excluded[d.name] = why
            continue
        write_skill(d, out / "skills" / d.name)
        meta, _ = frontmatter((d / "SKILL.md").read_text(encoding="utf-8-sig"))
        first = re.split(r"(?<=\.)\s", " ".join(meta["description"].split()), maxsplit=1)[0]
        included.append((d.name, first))
    srcm = json.loads((src / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8-sig"))
    m = {k: srcm[k] for k in MANIFEST_KEYS if k in srcm}
    m.update(displayName="Caffeinity skills", repository="https://github.com/arm-pz/caffeinity-directory",
             supportUrl="https://github.com/arm-pz/caffeinity-directory/issues",
             keywords=["agent-skills", "writing", "seo", "search-visibility", "release-checks", "research", "career"],
             description=f"{len(included)} plain-Markdown agent skills: writing and content, search visibility, "
                         "release checks, research and decisions, careers, outbound and learning. "
                         "No scripts, no installs, no network calls.")
    icon = src / ".claude-plugin" / "icon.png"
    if icon.is_file():
        (out / ".claude-plugin").mkdir(parents=True, exist_ok=True)
        shutil.copyfile(icon, out / ".claude-plugin" / "icon.png")
        m["icon"] = "./.claude-plugin/icon.png"
    (out / "README.md").write_text(readme(included), encoding="utf-8", newline="\n")
    shutil.copyfile(ROOT / "LICENSE", out / "LICENSE")
    return m, included, excluded


def digest(folder):
    h = hashlib.sha256()
    for f in sorted(p for p in folder.rglob("*") if p.is_file() and p.name != "plugin.json"):
        h.update(f.relative_to(folder).as_posix().encode() + b"\0" + f.read_bytes())
    return h.hexdigest()[:16]


def excluded_md(excluded):
    lines = ["# Skills not yet in the directory edition", "",
             "Fix each at its source repo (arm-pz/<skill>); the hourly sync adds it once every rule passes.", ""]
    for name, why in excluded.items():
        lines.append(f"## {name}")
        lines += [f"- {w}" for w in why[:12]] + ([f"- …and {len(why) - 12} more"] if len(why) > 12 else []) + [""]
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("src", type=Path, help="caffeinity-skills/plugins/caffeinity")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    tmp = ROOT / ".build"
    shutil.rmtree(tmp, ignore_errors=True)
    m, included, excluded = build(a.src, tmp)
    old = OUT / ".claude-plugin" / "plugin.json"
    oldm = json.loads(old.read_text(encoding="utf-8")) if old.is_file() else {}
    same = OUT.is_dir() and digest(tmp) == digest(OUT) and {k: v for k, v in oldm.items() if k != "version"} == {
        k: v for k, v in m.items() if k != "version"}
    m["version"] = oldm["version"] if same and "version" in oldm else "1." + dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d.%H%M")
    ordered = {k: m[k] for k in MANIFEST_KEYS if k in m}
    (tmp / ".claude-plugin").mkdir(parents=True, exist_ok=True)
    (tmp / ".claude-plugin" / "plugin.json").write_text(json.dumps(ordered, indent=2) + "\n", encoding="utf-8", newline="\n")
    files = sum(1 for p in tmp.rglob("*") if p.is_file())
    print(f"included {len(included)}, excluded {len(excluded)}, {files} files, {'unchanged' if same else 'changed'}")
    if a.check:
        shutil.rmtree(tmp)
        return 0 if same else 1
    shutil.rmtree(OUT, ignore_errors=True)
    tmp.rename(OUT)
    (ROOT / "EXCLUDED.md").write_text(excluded_md(excluded), encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
