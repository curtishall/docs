# Source: https://autonomy-today.getoutline.com/s/404b04ea-ebb1-49fc-aaf6-d620352bdde8/doc/small-agency-admin-SgsGzN7ITc

Small agency admin

For small agencies (rural police, small fire, sheriff, EMS), one person often handles both **organizational policy** and **day-to-day operations**.

## #What is a small agency admin?

A user with **both**:

- **OrgAdmin** — incident types, org settings, GIS, users org-wide
 
- **AgencyAdmin** — units, vehicles, agency toggles, daily ops
 

### #Good fit for

- Small police departments (chief wears both hats)
 
- Rural fire departments
 
- Small sheriff's offices
 
- Small EMS services
 

## #What they can do

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Area</p></th><th data-last-column="true"><p dir="auto">Examples</p></th></tr><tr><td data-first-column="true"><p dir="auto">Organization</p></td><td data-last-column="true"><p dir="auto">Incident types, tags, common places, GIS radius</p></td></tr><tr><td data-first-column="true"><p dir="auto">Agency</p></td><td data-last-column="true"><p dir="auto">Units, vehicles, NCIC/traffic stop toggles, report numbers</p></td></tr><tr><td data-first-column="true"><p dir="auto">Users</p></td><td data-last-column="true"><p dir="auto">Invite dispatchers and officers</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Field</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Same person may also dispatch from <strong>Dispatch CAD</strong></p></td></tr></tbody></table>

## #Setup (via Web Admin)

1. Create or select the user under **Users**.
 
2. Assign **OrgAdmin** role for the organization.
 
3. Assign **AgencyAdmin** (or agency access) for the primary agency.
 
4. Confirm user can open **Settings** (org) and **Agencies → Settings** (agency).
 
5. Have the user sign in to **Web Admin** and **Dispatch CAD** to verify sidebar items.
 

Your Cadmus implementer may handle initial user provisioning during go-live — ask IT if users were pre-provisioned in Clerk.

## #Daily workflow tips

- Configure **incident types** and **quick calls** before go-live.
 
- Set **agency settings** (traffic stops, NCIC) before training officers on mobile.
 
- Use **Sandbox** org for training if your deployment includes a paired sandbox tenant.
 
- Document who holds OrgAdmin — avoid shared accounts.
 

## #Common mistakes

- Giving OrgAdmin to every officer (over-permissioned).
 
- Enabling NCIC at agency without org CJIS site configured.
 
- Editing sandbox org thinking it is production.
 

## #Related pages

- [Roles and access](https://./roles-and-access.md)
 
- [Organization and agency basics](https://./organization-and-agency-basics.md)
 
- [Agency settings (core)](https://./agency-settings-core.md)
 
- [Integrations settings](https://./integrations-settings.md)
 
- [Admin and manager setup guide](https://../dispatch-cad/admin-manager-guide.md) — verify admin changes in **Dispatch CAD**
 

## #Warnings

> **Warning:** Small agency admins have broad power — use separate accounts for testing vs daily dispatch when possible.

> **Warning:** CJIS and NCIC settings must follow your state/agency compliance policy.

 [Outline](https://www.getoutline.com?ref=sharelink)