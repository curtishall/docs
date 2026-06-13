# Source: https://autonomy-today.getoutline.com/s/404b04ea-ebb1-49fc-aaf6-d620352bdde8/doc/troubleshooting-and-audit-checks-RxBsm48B5O

Troubleshooting and audit checks

Common admin mistakes and how to verify settings.

## #User cannot sign in

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Check</p></th><th data-last-column="true"><p dir="auto">Action</p></th></tr><tr><td data-first-column="true"><p dir="auto">User active?</p></td><td data-last-column="true"><p dir="auto">Users → reactivate</p></td></tr><tr><td data-first-column="true"><p dir="auto">Clerk invite accepted?</p></td><td data-last-column="true"><p dir="auto">Resend invite</p></td></tr><tr><td data-first-column="true"><p dir="auto">Wrong Clerk instance?</p></td><td data-last-column="true"><p dir="auto">Compare org Clerk ID in Settings</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Role assigned?</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Edit user role</p></td></tr></tbody></table>

If invite links fail, contact IT to verify Clerk redirect URLs

## #User sees empty call board

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Check</p></th><th data-last-column="true"><p dir="auto">Action</p></th></tr><tr><td data-first-column="true"><p dir="auto">Correct org in Dispatch CAD header?</p></td><td data-last-column="true"><p dir="auto">Switch org</p></td></tr><tr><td data-first-column="true"><p dir="auto">User assigned to agency?</p></td><td data-last-column="true"><p dir="auto">Users → agency access</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Wrong environment URL?</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">IT verifies deployment URL</p></td></tr></tbody></table>

See **Dispatch CAD** collection and [troubleshooting](https://./troubleshooting-and-audit-checks.md)

## #NCIC queries fail

1. Org **Settings** → CJIS site configured (CadmusAdmin).
 
2. Agency **State/NCIC Access** enabled.
 
3. User effective access (no denying override).
 
4. CJIS relay online (on-prem).
 

## #Incident type missing in Dispatch CAD

1. Organization **Incident types** → type is **Active**.
 
2. User’s org matches type’s organization.
 
3. Reload **Dispatch CAD** after admin change.
 

## #Quick call F-key does nothing

1. **Quick Call Shortcuts** template exists for that key.
 
2. Template incident type still valid.
 
3. Restart **Dispatch CAD** or reload data.
 

## #Report numbers wrong format

1. **Separate RMS report numbers** on/off as intended.
 
2. Format string tokens valid.
 
3. Sequence seed not reset mid-year without records approval.
 

## #Audit checklist (quarterly)

- Review users with NCIC overrides
 
- Review deactivated users still in Clerk
 
- Sandbox vs Live org names distinct
 
- Agency settings match written SOP
 
- Notification templates match current statutes
 
- API keys rotated for departed integrators
 
- RMS webhook logs show no repeated failures
 

## #Route availability notes

Some admin pages may not appear in the sidebar in all deployments:

- **Groups**
 
- **Roles** (dedicated page)
 
- **Notification Policies** (organization-wide)
 

Document as **availability-dependent**; use Users + Notification Templates until those pages are available.

## #When to escalate to Cadmus support

- Clerk sync fails for entire org
 
- Promotion Sandbox → Live errors
 
- GIS import corrupts beats
 
- Widespread WebSocket failures
 

Collect: org ID, agency ID, user email, time, screenshots (no CJIS data).

## #Warnings

> **Warning:** Never paste NCIC responses or CJIS credentials into support tickets.

> **Warning:** Audit logs may be required for compliance—do not disable user accounts without offboarding procedure.

 [Outline](https://www.getoutline.com?ref=sharelink)