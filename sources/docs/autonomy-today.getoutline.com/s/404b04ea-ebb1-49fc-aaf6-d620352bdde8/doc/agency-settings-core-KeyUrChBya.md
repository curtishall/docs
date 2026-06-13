# Source: https://autonomy-today.getoutline.com/s/404b04ea-ebb1-49fc-aaf6-d620352bdde8/doc/agency-settings-core-KeyUrChBya

Agency settings (core)

Agency-level toggles for safety, access, and features.

**Scope:** Agency (`/agencies/{agencyId}/settings`).

**Requires:** AgencyAdmin or higher (`canManageAgencyResources`).

> Screenshot placeholder: Agency settings page with toggle grid (requires AgencyAdmin)

## #Open

1. Select organization.
 
2. Go to **Agencies**.
 
3. Choose agency → **Settings**.
 

Or navigate directly: `/agencies/{agencyId}/settings`

## #Boolean settings

### #Traffic Stops Allowed

- **Category:** Safety
 
- **Default:** Enabled
 
- **Meaning:** Users may conduct traffic stops and citations from dispatch and mobile apps.
 
- **User override:** Allowed
 

### #State/NCIC Access

- **Category:** Access
 
- **Default:** Disabled
 
- **Meaning:** User may run state/NCIC queries when also authorized at user level and CJIS is configured.
 
- **User override:** Allowed
 

### #Separate RMS report numbers

- **Category:** Features
 
- **Default:** Disabled
 
- **Meaning:** When enabled, “Report to Follow” can assign RMS case numbers separate from CFS number.
 
- **User override:** Not allowed (agency-wide)
 

## #String settings

### #Report number format

Visible when **Separate RMS report numbers** is on.

Tokens: `{YYYY}`, `{YY}`, `{NNNN}`, `{NNNNNN}`, `{AGENCY}`

Example: `{AGENCY}-{YY}-{NNNN}` → `CPD-26-0001`

## #Save workflow

1. Select **Edit** (when shown).
 
2. Toggle settings or edit format string.
 
3. **Save**.
 
4. Confirm toast success.
 

## #Categories

Settings display in groups:

- **Safety** (red)
 
- **Access** (blue)
 
- **Features** (green)
 
- **Compliance** (orange)
 

## #Dispatch and mobile impact summary

<table style="--default-cell-min-width: 25px; min-width: 75px;"><colgroup><col><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Setting</p></th><th><p dir="auto">When OFF</p></th><th data-last-column="true"><p dir="auto">When ON</p></th></tr><tr><td data-first-column="true"><p dir="auto">Traffic stops</p></td><td><p dir="auto">Traffic/citation flows restricted</p></td><td data-last-column="true"><p dir="auto">Normal traffic stop workflow</p></td></tr><tr><td data-first-column="true"><p dir="auto">NCIC access</p></td><td><p dir="auto">Queries denied</p></td><td data-last-column="true"><p dir="auto">Queries allowed if user effective access</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Separate report numbers</p></td><td data-last-row="true"><p dir="auto">Report # = CFS #</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Custom RMS numbering</p></td></tr></tbody></table>

## #Related pages

- [Citation and report settings](https://citation-and-report-settings.md)
 
- [User agency overrides](https://user-agency-overrides.md)
 
- [Integrations settings](https://integrations-settings.md)
 

## #Common mistakes

- Enabling NCIC without org CJIS site.
 
- Changing report format after numbers issued.
 
- Assumes mobile and dispatch read the same settings — no separate copies.
 

## #Warnings

> **Warning:** Disabling traffic stops mid-shift affects units already on traffic calls—communicate before toggling.

> **Warning:** Report number seed/format changes can duplicate or skip sequences—coordinate with records manager.

 [Outline](https://www.getoutline.com?ref=sharelink)