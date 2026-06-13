# Source: https://autonomy-today.getoutline.com/s/404b04ea-ebb1-49fc-aaf6-d620352bdde8/doc/roles-reference-kHPbvO7pK3

Roles reference

Full role matrix for **Web Admin**, **Dispatch CAD**, and **Mobile CAD** access.

## #Role tiers

<table style="--default-cell-min-width: 25px; min-width: 75px;"><colgroup><col><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Tier</p></th><th><p dir="auto">Roles</p></th><th data-last-column="true"><p dir="auto">Scope</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>Platform</strong></p></td><td><p dir="auto">CadmusAdmin</p></td><td data-last-column="true"><p dir="auto">All organizations</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Organization</strong></p></td><td><p dir="auto">OrgAdmin</p></td><td data-last-column="true"><p dir="auto">One organization</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Agency</strong></p></td><td><p dir="auto">AgencyAdmin, AgencySupervisor, AgencyUser, Dispatcher, ExternalViewer</p></td><td data-last-column="true"><p dir="auto">Agency operations</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>Restricted</strong></p></td><td data-last-row="true"><p dir="auto">ReadOnly-Calls</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Incidents only in admin</p></td></tr></tbody></table>

## #CadmusAdmin (platform)

- Access to **all** organizations
 
- Configure CJIS site, RMS webhooks, cross-org tools
 
- Use organization picker carefully before saving
 

## #OrgAdmin (organization)

- Manage agencies, users, org incident types, GIS, locations
 
- Open **Settings** for org geographic area and Clerk sync
 
- Cannot access other organizations
 

## #AgencyAdmin

- Manage units, vehicles, agency settings, user overrides
 
- Route: `/agencies/{agencyId}/settings`
 

## #AgencySupervisor / AgencyUser / Dispatcher

- Operational access — **Dispatch CAD** for call handling
 
- Limited or no **Web Admin** configuration pages
 
- Dispatcher uses **Dispatch CAD** daily
 

## #ExternalViewer

- API key access for integrations
 
- **Account → API keys**
 

## #ReadOnly-Calls (restricted)

- **Incidents only** in **Web Admin** sidebar
 
- Redirected away from dashboard root
 
- Cannot open organizations or agency settings
 
- Does not replace **Dispatch CAD** access — role is for admin UI only
 

## #Sidebar visibility

Navigation is filtered by role. If a menu item is missing, your role lacks permission for that route.

## #Common assignments

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Person</p></th><th data-last-column="true"><p dir="auto">Typical role</p></th></tr><tr><td data-first-column="true"><p dir="auto">County CAD director</p></td><td data-last-column="true"><p dir="auto">OrgAdmin</p></td></tr><tr><td data-first-column="true"><p dir="auto">Chief / sheriff (small agency)</p></td><td data-last-column="true"><p dir="auto">OrgAdmin + AgencyAdmin — see <a href="https://./small-agency-admin.md" class="use-hover-preview" rel="noopener noreferrer nofollow">small-agency-admin.md</a></p></td></tr><tr><td data-first-column="true"><p dir="auto">Dispatch supervisor</p></td><td data-last-column="true"><p dir="auto">AgencyAdmin or Dispatcher</p></td></tr><tr><td data-first-column="true"><p dir="auto">Line dispatcher</p></td><td data-last-column="true"><p dir="auto">Dispatcher</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Records (view only)</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">ReadOnly-Calls</p></td></tr></tbody></table>

## #Warnings

> **Warning:** Grant NCIC-related access only to CJIS-certified users per agency policy.

> **Warning:** CadmusAdmin changes can affect every tenant — confirm organization before saving.

 [Outline](https://www.getoutline.com?ref=sharelink)