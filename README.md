# caffeinity-directory

The Claude directory edition of [caffeinity-skills](https://github.com/arm-pz/caffeinity-skills).
Submit the **`plugin/`** folder; everything else here only builds it.

The directory accepts only Markdown, text, JSON, YAML and images from organizations that aren't
Verified, with no install commands or credentials even in documentation. `scripts/build.py` copies
each skill from the full plugin that meets those rules, keeps only `name` and `description` in its
frontmatter, and writes the rest to [EXCLUDED.md](EXCLUDED.md) with the reasons.

- `.github/workflows/sync.yml` rebuilds hourly and commits only when something changed.
- To bring a skill in, fix the lines EXCLUDED.md names in its source repo (`arm-pz/<skill>`);
  the next sync includes it.
- Local run: `python scripts/build.py ../caffeinity-skills/plugins/caffeinity`
