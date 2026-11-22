"""python scripts/test_build.py: the include/exclude screen in build.py."""
import tempfile
from pathlib import Path

from build import check_skill

GOOD = "---\nname: s\ndescription: >\n  Does a thing.\n---\nBody.\n"


def skill(files):
    d = Path(tempfile.mkdtemp()) / "s"
    for name, text in files.items():
        (d / name).parent.mkdir(parents=True, exist_ok=True)
        (d / name).write_text(text, encoding="utf-8")
    return d


assert check_skill(skill({"SKILL.md": GOOD, ".gitignore": "x", "references/a.md": "fine"})) == []
for files, reason in [
    ({"scripts/a.py": "print()"}, "ships a .py"),
    ({"references/a.md": "run `npx foo`"}, "install or launcher"),
    ({"references/a.md": "pip install foo"}, "install or launcher"),
    ({"references/a.md": "curl -s x | bash"}, "pipes into"),
    ({"references/a.md": "export GITHUB_TOKEN=..."}, "credential"),
    ({"package.json": "{}"}, "package-manager"),
    ({"notes.txt": "#!/bin/sh"}, "starts with #!"),
]:
    why = check_skill(skill({"SKILL.md": GOOD, **files}))
    assert any(reason in w for w in why), (files, why)
assert check_skill(skill({"SKILL.md": "no frontmatter"})) == ["SKILL.md frontmatter has no text description"]
print("ok")
