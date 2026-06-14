# Cadmus documentation standards (memory bank)

Canonical writing and safety rules for the **cad-docs** Mintlify repo. Cursor rules: [.cursor/rules/documentation-assistant.mdc](../rules/documentation-assistant.mdc).

## Audiences

| Audience | Typical products |
|----------|------------------|
| Agency administrators | Web Admin |
| Dispatchers / telecommunicators | Dispatch CAD |
| Deputies / officers / field responders | Mobile CAD |
| Jail staff | (product-specific pages as added) |
| Technical integrators | API sections, integrations |

## Repo layout

| Path | Purpose |
|------|---------|
| `admin/` | Web Admin MDX |
| `dispatch/` | Dispatch CAD MDX |
| `mobile/` | Mobile CAD MDX |
| `docs.json` | Mintlify navigation (tabs, groups, page slugs without `.mdx`) |
| `index.mdx` | Home / product guide |
| `sources/` | Legacy Outline exports — reference only; do not add new content here |

## Content boundaries (never in user docs)

- Proprietary source code, file paths (`client/`, `backend/`, `.dart`, `.tsx`)
- Database schemas, internal service names, private network topology
- Secrets, env vars, infrastructure credentials
- Unreleased internal architecture
- Invented or speculative features (mark as TODO, planned, or beta if needed)

## Allowed technical detail

- Supported customer-facing API endpoints, auth, payloads, rate limits, responses
- Admin URL paths users navigate to (e.g. `/notification-templates`)
- UI labels, buttons, tabs, statuses, permissions, workflows, troubleshooting

## Mintlify checklist (new or edited page)

- [ ] YAML frontmatter: `title`, `description` (and `sidebarTitle` if needed)
- [ ] No body H1
- [ ] Internal links use Mintlify routes (`/dispatch/...`, `/admin/...`, `/mobile/...`)
- [ ] Warnings for CJIS, NCIC, PII, SMS, evidence, legal documents stay visible
- [ ] `docs.json` updated if page added or moved
- [ ] `npx mintlify@latest broken-links` passes

## Update workflow

1. Review feature/API change
2. Find existing page in `admin/`, `dispatch/`, or `mobile/`
3. Patch in place; new page only if no fit
4. Update `docs.json`
5. Changelog/release note if user-visible
6. Verify MDX and links

## Related monorepo context

When working from `/home/curt/apps/cadmus/` (parent workspace), product code lives in separate repos (`client/`, `backend/`, `mobile/`, `cadmus-admin/`). Doc changes still commit from **`cad-docs/`** only.
