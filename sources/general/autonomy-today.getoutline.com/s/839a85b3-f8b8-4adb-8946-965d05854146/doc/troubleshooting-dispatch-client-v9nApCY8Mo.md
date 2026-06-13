# Source: https://autonomy-today.getoutline.com/s/839a85b3-f8b8-4adb-8946-965d05854146/doc/troubleshooting-dispatch-client-v9nApCY8Mo

Troubleshooting (dispatch client)

Common problems and quick recovery steps.

> Screenshot placeholder: Example error toast on dashboard

## #Cannot sign in

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Check</p></th><th data-last-column="true"><p dir="auto">Action</p></th></tr><tr><td data-first-column="true"><p dir="auto">Account active?</p></td><td data-last-column="true"><p dir="auto">Agency admin reactivates user in Web Admin</p></td></tr><tr><td data-first-column="true"><p dir="auto">Wrong environment?</p></td><td data-last-column="true"><p dir="auto">Confirm Live vs Sandbox org</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Clerk invite pending?</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Resend invite</p></td></tr></tbody></table>

## #Empty dashboard / no calls

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Check</p></th><th data-last-column="true"><p dir="auto">Action</p></th></tr><tr><td data-first-column="true"><p dir="auto">Agency filter</p></td><td data-last-column="true"><p dir="auto">Header <strong>Select Agencies</strong> — include correct agencies</p></td></tr><tr><td data-first-column="true"><p dir="auto">Wrong org</p></td><td data-last-column="true"><p dir="auto">Confirm org in header badge</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Stale data</p></td><td data-last-column="true" data-last-row="true"><p dir="auto"><strong>Reload Units &amp; Dashboard Data</strong></p></td></tr></tbody></table>

> Screenshot placeholder: Reload success toast

## #Units not updating

1. **Reload Data** from settings menu.
 
2. Check WebSocket indicator if visible (connection quality).
 
3. Confirm unit is on duty and logged in (F2).
 

## #NCIC queries fail

See [Queries and NCIC](https://./queries-ncic.md) admin checklist.

## #Incident type missing on New CFS

1. Web Admin → incident types → **Active**.
 
2. Reload client data.
 
3. Confirm correct organization.
 

## #Quick call F-key does nothing

1. Web Admin → Quick Call Shortcuts — template exists for that key.
 
2. Reload client.
 
3. Restart client if template was just added.
 

## #Map or RapidSOS issues

- Confirm org GIS and RapidSOS configured in Web Admin.
 
- RapidSOS header button may be disabled in production builds.
 
- Try **Refresh Address Resolution** on call before map pin.
 

## #Settings and tools (diagnostics)

Gear menu **Settings & tools**:

- **Machine Diagnostics**
 
- **Test Connection**
 
- **View Logs** (for IT)
 
- **Clear All Caches**
 
- **Force Reload**
 

> Screenshot placeholder: Settings and tools menu expanded

## #Feedback

**Feature request / Report a problem** — in-app feedback to product team.

## #When to escalate

Collect for support: org name, agency, user email, time, screenshots (no NCIC data), steps to reproduce.

## #Warnings

> **Warning:** **Clear All Caches** may sign you out or reset local preferences.

> **Warning:** Never paste NCIC responses into feedback tickets.

 [Outline](https://www.getoutline.com?ref=sharelink)