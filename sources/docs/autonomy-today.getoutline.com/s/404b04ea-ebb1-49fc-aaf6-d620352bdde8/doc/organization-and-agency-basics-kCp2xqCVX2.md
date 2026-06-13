# Source: https://autonomy-today.getoutline.com/s/404b04ea-ebb1-49fc-aaf6-d620352bdde8/doc/organization-and-agency-basics-kCp2xqCVX2

Organization and agency basics

How organizations, agencies, and settings scope fit together.

## #Definitions

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Term</p></th><th data-last-column="true"><p dir="auto">Meaning</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>Organization</strong></p></td><td data-last-column="true"><p dir="auto">Top-level tenant (e.g., county CAD)</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Agency</strong></p></td><td data-last-column="true"><p dir="auto">Department within org (Sheriff, PD, Fire, EMS)</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Unit</strong></p></td><td data-last-column="true"><p dir="auto">Field resource (call sign / apparatus)</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>User</strong></p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Person with login; may belong to org with roles</p></td></tr></tbody></table>

## #Organization picker

After sign-in, pick the **organization** you administer. All list pages (users, agencies, settings) filter to that org.

> Screenshot placeholder: Organization picker dropdown (requires admin session)

## #Live vs Sandbox

Many deployments use **paired** Live and Sandbox organizations for training and promotion.

- Create pairs from organization form
 
- Promote Sandbox → Live when ready
 

Ask CadmusAdmin about Live/Sandbox org pairing

> Screenshot placeholder: Organization promotion page (requires CadmusAdmin)

## #Agencies list

Path: **Agencies** or **Organizations → {org} → Agencies**

Each agency has:

- Units and vehicles
 
- Agency-specific settings (`/agencies/{id}/settings`)
 
- Optional scoped user lists
 

## #Agency sharing

Some orgs share CFS visibility across agencies when **CFS sharing** is enabled in org settings.

## #Where to configure what

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Need</p></th><th data-last-column="true"><p dir="auto">Where</p></th></tr><tr><td data-first-column="true"><p dir="auto">Service area / geocoding radius</p></td><td data-last-column="true"><p dir="auto">Org <strong>Settings</strong></p></td></tr><tr><td data-first-column="true"><p dir="auto">Incident types, tags, locations</p></td><td data-last-column="true"><p dir="auto">Organization configuration menus</p></td></tr><tr><td data-first-column="true"><p dir="auto">Traffic stops / NCIC</p></td><td data-last-column="true"><p dir="auto"><strong>Agency settings</strong></p></td></tr><tr><td data-first-column="true"><p dir="auto">Quick call F-keys</p></td><td data-last-column="true"><p dir="auto">Quick Call Shortcuts</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Units &amp; crews</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Units</p></td></tr></tbody></table>

## #Impact on Dispatch CAD

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Admin change</p></th><th data-last-column="true"><p dir="auto">Dispatch CAD effect</p></th></tr><tr><td data-first-column="true"><p dir="auto">New incident type</p></td><td data-last-column="true"><p dir="auto">Appears in New CFS</p></td></tr><tr><td data-first-column="true"><p dir="auto">GIS / locations</p></td><td data-last-column="true"><p dir="auto">Address validation &amp; common places</p></td></tr><tr><td data-first-column="true"><p dir="auto">Agency NCIC off</p></td><td data-last-column="true"><p dir="auto">Query buttons hidden or denied</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Quick call template</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">F8–F12 behavior updates after reload</p></td></tr></tbody></table>

See **Dispatch CAD** documentation: [Admin configuration](https://../dispatch-cad/command-line/admin-configuration.md)

## #Common mistakes

- Editing Sandbox thinking it is Live (similar names).
 
- Creating units under wrong agency.
 
- Enabling CFS sharing without coordinating dispatch SOP.
 

## #Tips

- Name Sandbox orgs clearly (e.g., “County CAD – Sandbox”).
 
- Document agency abbreviations used in report number formats.
 
- After org promotion, re-verify Clerk membership sync.
 

 [Outline](https://www.getoutline.com?ref=sharelink)