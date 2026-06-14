# cad-docs

End-user documentation for Cadmus products, published with [Mintlify](https://mintlify.com).

| Folder | Product |
|--------|---------|
| `dispatch/` | Dispatch CAD |
| `admin/` | Web Admin |
| `mobile/` | Mobile CAD |

**Site:** https://cadmus.mintlify.app  
**Repo:** https://github.com/AutonomyToday/cad-docs

## Edit docs

1. Change MDX under `dispatch/`, `admin/`, or `mobile/`.
2. Update `docs.json` when adding or moving pages.
3. Preview: `npx mintlify@latest dev`
4. Check links: `npx mintlify@latest broken-links`
5. Commit and push from this folder (`cad-docs/` is its own git repo).

Agent/writing standards: see [AGENTS.md](AGENTS.md) and [.cursor/rules/documentation-assistant.mdc](.cursor/rules/documentation-assistant.mdc).

## Legacy note

User docs previously lived in workspace `manual/` (markdown + Outline sync). That pipeline is **retired** — **`cad-docs/`** is the source of truth. Old Outline exports may remain under `sources/` for reference only.
