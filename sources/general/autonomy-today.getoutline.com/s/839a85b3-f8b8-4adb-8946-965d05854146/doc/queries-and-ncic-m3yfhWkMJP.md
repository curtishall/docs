# Source: https://autonomy-today.getoutline.com/s/839a85b3-f8b8-4adb-8946-965d05854146/doc/queries-and-ncic-m3yfhWkMJP

Queries and NCIC

CJIS query workspace and in-call queries.

> Screenshot placeholder: Query Workspace full screen (F3)

## #Query Workspace (F3)

Law-enforcement agencies with NCIC enabled:

- Header **Query** opens **Query Workspace**
 
- If denied: **CJIS Access Denied** — contact admin for **State/NCIC Access**
 

### #Query categories (rail)

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Category</p></th><th data-last-column="true"><p dir="auto">Use</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>Plate</strong></p></td><td data-last-column="true"><p dir="auto">License plate</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>VIN</strong></p></td><td data-last-column="true"><p dir="auto">Vehicle identification</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Name / DOR</strong></p></td><td data-last-column="true"><p dir="auto">Person/driver</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Vehicle Owner</strong></p></td><td data-last-column="true"><p dir="auto">Registered owner</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Boat</strong></p></td><td data-last-column="true"><p dir="auto">Watercraft</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Gun</strong></p></td><td data-last-column="true"><p dir="auto">Firearm serial</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Serial</strong></p></td><td data-last-column="true"><p dir="auto">General serial</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Wanted</strong></p></td><td data-last-column="true"><p dir="auto">Wanted persons</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>Criminal History</strong></p></td><td data-last-column="true" data-last-row="true"><p dir="auto">History query</p></td></tr></tbody></table>

> Screenshot placeholder: Query category rail in workspace

### #Recent queries

- **Recent Queries** sidebar inside workspace.
 

> Screenshot placeholder: Recent Queries panel

## #In-call queries

From call detail blocks:

- **REPORTING PARTY** → **Query**
 
- **Run CJIS person query** on persons
 
- **Run CJIS vehicle query** on vehicles
 
- **Run Query** panel with **Persons**, **Vehicles**, **Serial**, **Gun**
 
- **RESTRICTED** label when query type not allowed
 

> Screenshot placeholder: Run Query panel on open call

## #CJIS query history

On call detail:

- **CJIS Query History** with **Refresh**
 
- Audit trail of queries tied to incident.
 

> Screenshot placeholder: CJIS Query History block

## #Command line queries

See [Query commands](https://./command-line/query-commands.md): **DL**, **LP**, **NAME**, etc.

## #Admin requirements

1. Org **Settings** → CJIS site (CadmusAdmin).
 
2. Agency **State/NCIC Access** enabled.
 
3. User effective access (no denying override).
 

See **Web Admin** → Integrations settings.

## #Tips

- Include **state** on out-of-state plates/licenses.
 
- Query from open call when results must tie to CFS audit.
 
- Use **Recent Queries** to repeat similar lookups.
 

## #Warnings

> **Warning:** All queries are logged — use only for official purposes per CJIS policy.

> **Warning:** Do not read NCIC results aloud on open radio — use secure channels.

> **Warning:** **CJIS Access Denied** usually means admin config, not a Dispatch CAD issue — escalate to agency admin.

 [Outline](https://www.getoutline.com?ref=sharelink)