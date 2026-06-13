# Source: https://autonomy-today.getoutline.com/s/404b04ea-ebb1-49fc-aaf6-d620352bdde8/doc/user-agency-overrides-csVRsodYFl

User agency overrides

Override agency default settings for a specific user.

**Scope:** User + Agency (override applies to one user in one agency).

## #Purpose

Agency settings define defaults (e.g., NCIC off for everyone). Overrides grant or deny exceptions for one person.

Hierarchy:

1. Agency default
 
2. User override (if present)
 
3. **Effective setting** = what the user gets
 

## #Open

In **Web Admin**, open the user’s agency settings or the dedicated overrides screen when your deployment provides it.

API: `POST/GET /agencies/{agencyId}/users/{userId}/settings`

> **Availability note:** Per-user override screens may not be linked from the Users page in all deployments. If missing, contact your Cadmus administrator.

> Screenshot placeholder: User agency overrides panel

## #Overridable settings (typical)

<table style="--default-cell-min-width: 25px; min-width: 75px;"><colgroup><col><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Setting</p></th><th><p dir="auto">Agency default</p></th><th data-last-column="true"><p dir="auto">Override use</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>Traffic Stops Allowed</strong></p></td><td><p dir="auto">On</p></td><td data-last-column="true"><p dir="auto">Trainee off until FTO sign-off</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>State/NCIC Access</strong></p></td><td data-last-row="true"><p dir="auto">Off</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Certified operator on</p></td></tr></tbody></table>

## #Required for overrides

- **Reason** text (audit trail)
 
- **AgencyAdmin** or higher
 
- Setting must allow `canBeOverridden`
 

## #Audit

Overrides store:

- Who changed it
 
- When
 
- Reason
 

Review during accreditations and CJIS audits.

## #Dispatch and mobile impact

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Effective setting</p></th><th data-last-column="true"><p dir="auto">Field behavior</p></th></tr><tr><td data-first-column="true"><p dir="auto">NCIC on</p></td><td data-last-column="true"><p dir="auto">Query actions enabled</p></td></tr><tr><td data-first-column="true"><p dir="auto">NCIC off</p></td><td data-last-column="true"><p dir="auto">Queries blocked or hidden</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Traffic stops off</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Traffic stop / citation flows restricted</p></td></tr></tbody></table>

See **Dispatch CAD** documentation: [Query commands](https://../dispatch-cad/command-line/query-commands.md)

## #Common mistakes

- Override without documented reason.
 
- Leaving override after user transfers agencies.
 
- Enabling NCIC for user without agency CJIS routing configured.
 

## #Warnings

> **Warning:** NCIC overrides without CJIS site configuration still fail at query time—configure org CJIS first.

> **Warning:** Overrides are auditable—do not use for informal favors outside policy.

 [Outline](https://www.getoutline.com?ref=sharelink)