# Source: https://autonomy-today.getoutline.com/s/839a85b3-f8b8-4adb-8946-965d05854146/doc/admin-and-manager-setup-guide-UAESNxwilP

Admin and manager setup guide

For **AgencyAdmin**, **OrgAdmin**, and supervisors who configure **Web Admin** and verify behavior in **Dispatch CAD** (and **Mobile CAD**).

Use this as a go-live checklist: change settings in admin, then confirm in dispatch before training the full shift.

> Screenshot placeholder: Split view — Web Admin agency settings and Dispatch CAD dashboard

## #Who this is for

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Role</p></th><th data-last-column="true"><p dir="auto">Typical use</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>AgencyAdmin</strong></p></td><td data-last-column="true"><p dir="auto">Agency toggles, units, quick calls, command aliases</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>OrgAdmin</strong></p></td><td data-last-column="true"><p dir="auto">Users, incident types, GIS, RapidSOS, org settings</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>Small agency lead</strong></p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Both roles — see <a href="https://../web-admin/small-agency-admin.md" class="use-hover-preview" rel="noopener noreferrer nofollow">Small agency admin</a></p></td></tr></tbody></table>

## #Before you start

1. Know whether you are in **Sandbox** or **Live** organization.
 
2. Use a dedicated admin account for configuration (not a shared dispatch login).
 
3. Keep a second browser or window: **Web Admin** + **Dispatch CAD**.
 

## #Go-live checklist

### #1\. Users and roles

**Web Admin:** [Users lifecycle](https://../web-admin/users-lifecycle.md)

- Invite dispatchers with **Dispatcher** role.
 
- Assign correct **agency access**.
 
- Deactivate test accounts before production.
 

**Verify in Dispatch CAD:**

- User signs in and sees expected org in header.
 
- Sidebar matches role ([Roles and access](https://../web-admin/roles-and-access.md)).
 

### #2\. Incident types and New CFS

**Web Admin:** Organization **Incident types** — active types for your org.

**Verify in Dispatch CAD:**

- **New CFS** (F1) → types appear in dropdown.
 
- Create a test call in Sandbox; confirm type, priority, and numbering.
 

See [Create CFS workflow](https://./create-cfs-workflow.md) and [New CFS form fields](https://./new-cfs-form-fields.md).

### #3\. Quick calls (F8–F12)

**Web Admin:** Organization **Quick Call Shortcuts** — map keys to incident types.

**Verify in Dispatch CAD:**

- Press each configured F-key from dashboard.
 
- Reload **Dispatch CAD** if a template was just added.
 

See [Quick calls and F-keys](https://./quick-calls-and-f-keys.md).

### #4\. Agency settings

**Web Admin:** [Agency settings (core)](https://../web-admin/agency-settings-core.md)

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Setting</p></th><th data-last-column="true"><p dir="auto">Verify in dispatch / mobile</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>State/NCIC Access</strong></p></td><td data-last-column="true"><p dir="auto"><strong>Query</strong> (F3) available when org CJIS also configured</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Traffic Stops Allowed</strong></p></td><td data-last-column="true"><p dir="auto">Mobile e-citation / traffic stop flows</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Separate RMS report numbers</strong></p></td><td data-last-column="true"><p dir="auto">Close call / <strong>REPORT#</strong> behavior</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Report number format</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Close with RTF assigns expected format</p></td></tr></tbody></table>

### #5\. CJIS and NCIC

**Web Admin:** [Integrations settings](https://../web-admin/integrations-settings.md)

1. **CadmusAdmin** sets org **CJIS site**.
 
2. **AgencyAdmin** enables **State/NCIC Access**.
 
3. User overrides only if policy requires ([User agency overrides](https://../web-admin/user-agency-overrides.md)).
 

**Verify in Dispatch CAD:**

- Run training query on Sandbox call — see [Queries and NCIC](https://./queries-ncic.md).
 
- Confirm **CJIS Access Denied** is resolved before go-live.
 

### #6\. Command line aliases

**Web Admin:** [Admin configuration (Web Admin)](https://./command-line/admin-configuration.md) — **Command Aliases**, **Call Shortcodes**, **Disposition Codes**.

**Verify in Dispatch CAD:**

- Type `**HELP**` on dashboard and on call detail — lists match what you enabled.
 
- Dry-run test in admin **test** box if available.
 

See [Command Line](https://./command-line/overview.md) overview.

### #7\. Units and login

**Web Admin:** Units and vehicles for the agency.

**Verify in Dispatch CAD:**

- **Login User** (F2) — units appear, login succeeds.
 
- Mobile unit sees assignments — [Unit login and assignment](https://./unit-login-and-assignment.md).
 

### #8\. Notifications

**Web Admin:** [User notification preferences](https://../web-admin/user-notification-preferences.md) and org **Notification Templates**.

**Verify:**

- Dispatcher hears/sees alerts for test incident types.
 
- Mobile voice alerts if used — [Voice alerts](https://../mobile-cad/voice-alerts.md).
 

### #8b. Dispatch SMS (if enabled)

**Web Admin:**

- **Notification Templates** (`/notification-templates`) — **Incident SMS** wording
 
- **Groups** — recipient lists for field supervisors
 
- User **phone numbers** on every SMS recipient
 

**Verify in Dispatch CAD:**

- **Send SMS** on a Sandbox test call — see [SMS templates and messaging](https://./sms-templates-and-messaging.md)
 
- Confirm **SMS History** and send-results dialog
 

### #9\. RapidSOS (if used)

**Web Admin:** [RapidSOS management](https://../web-admin/rapidsos-management.md)

**Verify in Dispatch CAD:**

- Map layers **RapidSOS Locations** / **Breadcrumbs**.
 
- **RapidSOS Lookup** or **Track Phone Number** on sandbox test number.
 

See [Map and location](https://./map-and-location.md).

### #10\. BOLOs and operational boards

**Verify in Dispatch CAD:**

- Create test BOLO — appears on **BOLOs** tab and in mobile [BOLOs and warrants](https://../mobile-cad/bolos-and-warrants.md).
 
- Operational greaseboard categories match SOP — [BOLO, greaseboard, and wrecker](https://./bolo-greaseboard-wrecker.md).
 

### #11\. Citations (if used)

**Web Admin:** [Citation and report settings](https://../web-admin/citation-and-report-settings.md)

**Verify on Mobile CAD:**

- **E-Ticket** available when **Traffic Stops Allowed** is on.
 
- See [E-citations overview](https://../mobile-cad/ecitations-overview.md).
 

## #Daily admin tasks

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Task</p></th><th data-last-column="true"><p dir="auto">Where</p></th></tr><tr><td data-first-column="true"><p dir="auto">Add dispatcher</p></td><td data-last-column="true"><p dir="auto">Web Admin → Users</p></td></tr><tr><td data-first-column="true"><p dir="auto">New incident type</p></td><td data-last-column="true"><p dir="auto">Web Admin → Incident types → reload Dispatch CAD</p></td></tr><tr><td data-first-column="true"><p dir="auto">NCIC for one officer</p></td><td data-last-column="true"><p dir="auto">User override + CJIS already configured</p></td></tr><tr><td data-first-column="true"><p dir="auto">Shift pass-on note</p></td><td data-last-column="true"><p dir="auto">Dispatch CAD greaseboard or chat</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Audit who has OrgAdmin</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Web Admin → Users + written roster</p></td></tr></tbody></table>

## #Common mistakes

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Mistake</p></th><th data-last-column="true"><p dir="auto">Fix</p></th></tr><tr><td data-first-column="true"><p dir="auto">Configured Sandbox, dispatchers use Live</p></td><td data-last-column="true"><p dir="auto">Match org names; sign out/in</p></td></tr><tr><td data-first-column="true"><p dir="auto">NCIC on at agency, no CJIS site</p></td><td data-last-column="true"><p dir="auto">Org <strong>Settings</strong> → CJIS site first</p></td></tr><tr><td data-first-column="true"><p dir="auto">Quick call key silent</p></td><td data-last-column="true"><p dir="auto">Template missing or inactive incident type</p></td></tr><tr><td data-first-column="true"><p dir="auto">Units empty on F2</p></td><td data-last-column="true"><p dir="auto">Wrong agency or units not created under agency</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">RapidSOS test OK, map empty</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Wrong org credentials; check environment</p></td></tr></tbody></table>

## #Escalation

Collect for Cadmus support: organization name, agency name, user email, time of issue, screenshots (no CJIS data or query responses).

See [Troubleshooting](https://./troubleshooting.md) and [Web Admin troubleshooting](https://../web-admin/troubleshooting-and-audit-checks.md).

## #Related documentation

- **Web Admin** — [intro](https://../web-admin/intro.md)
 
- **Mobile CAD** — settings that affect field units
 
- **Dispatch CAD** — [Getting started](https://./getting-started.md)
 

## #Warnings

> **Warning:** Test all NCIC and RapidSOS changes in Sandbox before Live.

> **Warning:** Do not use production org for training exercises with real citizen phone numbers without agency policy approval.

 [Outline](https://www.getoutline.com?ref=sharelink)