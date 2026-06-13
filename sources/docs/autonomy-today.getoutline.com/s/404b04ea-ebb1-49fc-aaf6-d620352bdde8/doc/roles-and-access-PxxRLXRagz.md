# Source: https://autonomy-today.getoutline.com/s/404b04ea-ebb1-49fc-aaf6-d620352bdde8/doc/roles-and-access-PxxRLXRagz

Roles and access

Who can see and change settings in **Web Admin**.

> Screenshot placeholder: Sidebar navigation for OrgAdmin role (requires signed-in admin session)

## #Role tiers

<table style="--default-cell-min-width: 25px; min-width: 75px;"><colgroup><col><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Tier</p></th><th><p dir="auto">Roles</p></th><th data-last-column="true"><p dir="auto">Scope</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>Platform</strong></p></td><td><p dir="auto">CadmusAdmin</p></td><td data-last-column="true"><p dir="auto">All organizations</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Organization</strong></p></td><td><p dir="auto">OrgAdmin</p></td><td data-last-column="true"><p dir="auto">One organization</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Agency</strong></p></td><td><p dir="auto">AgencyAdmin, AgencySupervisor, AgencyUser, Dispatcher</p></td><td data-last-column="true"><p dir="auto">Agency operations</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>Restricted</strong></p></td><td data-last-row="true"><p dir="auto">ReadOnly-Calls, ExternalViewer</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Limited (see below)</p></td></tr></tbody></table>

See [Roles reference](https://./roles-reference.md)

## #Common roles in daily use

### #OrgAdmin

- Manage agencies, users, org-wide incident types, locations, GIS
 
- Open **Settings** (`/settings`) for org geographic area, CJIS site (with CadmusAdmin), Clerk sync
 

### #AgencyAdmin

- Manage units, vehicles, agency settings, user overrides for their agency
 
- Route: `/agencies/{agencyId}/settings`
 

### #Dispatcher

- Operational pages (incidents, units)—not full org configuration
 
- Uses **Dispatch CAD**, not most admin settings pages
 

### #ReadOnly-Calls

- **Incidents only** in sidebar
 
- Redirected away from dashboard root
 
- Cannot open organizations or agency settings
 

## #What controls the sidebar

Navigation is filtered by your role. If a menu item is missing, your account does not have permission for that area.

## #API keys (External Viewer)

Integrations may use **Account → API keys** (`/account/api-keys`).

> Screenshot placeholder: API keys page (requires ExternalViewer or admin role)

## #Testing roles

Contact your Cadmus administrator if you need a temporary role change for training or testing.

## #Scope callouts on settings pages

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Scope</p></th><th data-last-column="true"><p dir="auto">Example</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>Organization</strong></p></td><td data-last-column="true"><p dir="auto">Geographic center, CFS sharing, CJIS site</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Agency</strong></p></td><td data-last-column="true"><p dir="auto">Traffic stops allowed, NCIC access</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>User</strong></p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Notification preferences, per-user agency overrides</p></td></tr></tbody></table>

## #Common mistakes

- Expecting Dispatcher to edit agency NCIC toggles.
 
- Using ReadOnly-Calls account for training on admin pages.
 
- Changing production org while intending Sandbox.
 

## #Warnings

> **Warning:** CadmusAdmin actions affect all tenants—confirm organization picker before saving.

> **Warning:** Grant NCIC access only to users with CJIS certification per agency policy.

 [Outline](https://www.getoutline.com?ref=sharelink)