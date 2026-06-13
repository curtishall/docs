# Source: https://autonomy-today.getoutline.com/s/839a85b3-f8b8-4adb-8946-965d05854146/doc/sms-templates-and-messaging-mN8Ywp5ZAa

SMS templates and messaging

Deep dive on sending text messages from **Dispatch CAD** call detail: built-in templates, merge fields, recipients, delivery status, and how **Web Admin** configuration fits in.

> Screenshot placeholder: Send SMS sheet open on call detail with template dropdown and recipients

## #Overview

Dispatch SMS is **manual, call-scoped texting** to agency users (field officers, supervisors, etc.) — not the same as texting a reporting party from a personal phone. Messages are tied to the open CFS, logged on the call, and sent through your agency’s configured SMS service.

Three layers work together:

<table style="--default-cell-min-width: 25px; min-width: 75px;"><colgroup><col><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Layer</p></th><th><p dir="auto">What it is</p></th><th data-last-column="true"><p dir="auto">Where configured</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>Quick templates</strong></p></td><td><p dir="auto">Four starter messages in the <strong>Send SMS</strong> sheet</p></td><td data-last-column="true"><p dir="auto">Built into <strong>Dispatch CAD</strong> picker</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Merge fields</strong></p></td><td><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">{{variables}}</span></code> expanded from live call data when you send</p></td><td data-last-column="true"><p dir="auto">Typed in the message box; expanded at send time</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>Notification templates</strong></p></td><td data-last-row="true"><p dir="auto">Reusable <strong>Incident SMS</strong> / <strong>Critical Alert SMS</strong> bodies for automated or policy-driven notifications</p></td><td data-last-column="true" data-last-row="true"><p dir="auto"><strong>Web Admin</strong> → <strong>Notification Templates</strong></p></td></tr></tbody></table>

This guide focuses on the **Send SMS** workflow. Automated incident SMS (assignment alerts, critical notifications) uses **Notification Templates** and per-user preferences — see [User notification preferences](https://../web-admin/user-notification-preferences.md).

## #Prerequisites

SMS must be **enabled for your deployment** (agency SMS provider configured by Cadmus/IT). If **Send SMS** is missing or sends always fail, escalate to your administrator — admin toggles alone do not enable texting.

Recipients must have a **mobile phone number** on their user profile. Users without a number are skipped silently when resolving groups.

Dispatchers need permission to send SMS when your deployment assigns **send SMS** capabilities to the dispatcher role.

## #Open Send SMS

1. Open **call detail** for the CFS.
 
2. Click **Send SMS** (SMS icon in the call toolbar).
 

The sheet header shows **Send SMS** and a one-line **call description** summary for context.

> Screenshot placeholder: Send SMS toolbar button on call detail

## #Built-in quick templates

The **Template** dropdown pre-fills the **Message** box:

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Template</p></th><th data-last-column="true"><p dir="auto">Pre-filled text (concept)</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>Status Update</strong></p></td><td data-last-column="true"><p dir="auto">Call status update: <em>{call description}</em></p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Unit Dispatch</strong></p></td><td data-last-column="true"><p dir="auto">Unit dispatched to: <em>{call description}</em></p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Priority Change</strong></p></td><td data-last-column="true"><p dir="auto">Priority changed for call: <em>{call description}</em></p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>Custom Message</strong></p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Empty — write your own</p></td></tr></tbody></table>

The picker inserts the call’s **description** field where the template says “description.” You can edit the text before sending.

> Screenshot placeholder: Template dropdown with Status Update selected

### #When to use each

- **Status Update** — general situational text to field units (“RP on scene,” “cancelled,” etc.).
 
- **Unit Dispatch** — notify off-duty or secondary units of an assignment context.
 
- **Priority Change** — after elevating or lowering priority on the call.
 
- **Custom Message** — anything else; use merge fields below for structured data.
 

## #Merge fields (variables)

If you type `**{{variable}}**` placeholders in the message (in any template or custom text), they are replaced with **live call data** when you tap **Send SMS**.

### #Primary fields (recommended)

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Variable</p></th><th data-last-column="true"><p dir="auto">Replaced with</p></th></tr><tr><td data-first-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">{{agency_cfs}}</span></code></p></td><td data-last-column="true"><p dir="auto">Agency CFS / call number</p></td></tr><tr><td data-first-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">{{incident_type}}</span></code></p></td><td data-last-column="true"><p dir="auto">Incident type name</p></td></tr><tr><td data-first-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">{{RP_FullName}}</span></code></p></td><td data-last-column="true"><p dir="auto">Reporting party name</p></td></tr><tr><td data-first-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">{{phone}}</span></code></p></td><td data-last-column="true"><p dir="auto">Reporting party phone (may format as a dial link)</p></td></tr><tr><td data-first-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">{{address}}</span></code></p></td><td data-last-column="true"><p dir="auto">Incident address / location</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">{{CallDescription}}</span></code></p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Call description / narrative</p></td></tr></tbody></table>

### #Additional fields (legacy / optional)

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Variable</p></th><th data-last-column="true"><p dir="auto">Replaced with</p></th></tr><tr><td data-first-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">{{incidentId}}</span></code></p></td><td data-last-column="true"><p dir="auto">Internal incident identifier</p></td></tr><tr><td data-first-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">{{location}}</span></code></p></td><td data-last-column="true"><p dir="auto">Location text</p></td></tr><tr><td data-first-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">{{priority}}</span></code></p></td><td data-last-column="true"><p dir="auto">Priority level</p></td></tr><tr><td data-first-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">{{description}}</span></code></p></td><td data-last-column="true"><p dir="auto">Description (same family as call narrative)</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">{{timestamp}}</span></code></p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Call created time</p></td></tr></tbody></table>

### #Example custom message

```
CFS #{{agency_cfs}} {{incident_type}}
RP: {{RP_FullName}} {{phone}}
{{address}}
{{CallDescription}}
```

After send, recipients see resolved values — not the curly-brace placeholders.

> **Tip:** Use **Preview** before sending when you rely on merge fields, so you confirm the message box looks right. Final merge happens at send time on the server.

## #Message length

The **Message** field shows a **160-character** counter in **Dispatch CAD**. Standard SMS is one segment at 160 GSM characters; longer or Unicode text may split into multiple billable segments on the carrier.

Keep critical info (CFS number, address) in the first segment when possible.

## #Recipients

**Recipients** section with a count badge (e.g. “3 selected”).

### #Groups tab

Checkbox list of **groups** defined in **Web Admin** (when Groups management is available):

- Group name
 
- **N members** subtitle
 

Selecting a group includes every member with a phone number. Duplicate numbers across groups or individuals are deduplicated.

> Screenshot placeholder: Groups tab with two groups selected

### #Individuals tab

Checkbox list of organization **users**:

- Name
 
- Email subtitle (for identification)
 

Only users with a stored **phone number** receive SMS.

> Screenshot placeholder: Individuals tab with user checkboxes

You may select **both** groups and individuals in one send.

## #Preview and send

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Button</p></th><th data-last-column="true"><p dir="auto">Action</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>Preview</strong></p></td><td data-last-column="true"><p dir="auto">Dialog: recipient count + message text as entered (merge may still apply at send)</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>Send SMS</strong></p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Sends to all selected recipients; label shows <strong>Sending…</strong> while in progress</p></td></tr></tbody></table>

Validation:

- Message cannot be empty.
 
- At least one group or individual must be selected.
 

### #Send results dialog

After send, **SMS Send Results** shows:

- **Total Recipients**
 
- **Sent** / **Failed** counts
 
- Per-number rows: phone, **sent** or **failed**, optional error text
 

> Screenshot placeholder: SMS Send Results dialog with mixed sent/failed rows

Partial success is possible — review failed numbers and retry or contact IT.

## #SMS history on the call

Scroll call detail to **SMS History** (below **History & Logs**).

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Element</p></th><th data-last-column="true"><p dir="auto">Meaning</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>Refresh</strong></p></td><td data-last-column="true"><p dir="auto">Reload history from server</p></td></tr><tr><td data-first-column="true"><p dir="auto">Empty state</p></td><td data-last-column="true"><p dir="auto"><strong>No SMS messages sent for this call</strong></p></td></tr><tr><td data-first-column="true"><p dir="auto">Status badge</p></td><td data-last-column="true"><p dir="auto"><strong>SENT</strong>, <strong>FAILED</strong>, <strong>PENDING</strong>, <strong>DELIVERED</strong>, etc.</p></td></tr><tr><td data-first-column="true"><p dir="auto">Timestamp</p></td><td data-last-column="true"><p dir="auto">Local time and “time ago”</p></td></tr><tr><td data-first-column="true"><p dir="auto">Recipient</p></td><td data-last-column="true"><p dir="auto">Destination phone or address</p></td></tr><tr><td data-first-column="true"><p dir="auto">Error line</p></td><td data-last-column="true"><p dir="auto">Carrier or provider error when failed</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Metadata line</p></td><td data-last-column="true" data-last-row="true"><p dir="auto"><strong>Recipients: N | Sent: X | Failed: Y</strong> for bulk sends</p></td></tr></tbody></table>

> Screenshot placeholder: SMS History block with two entries and status badges

Successful sends also appear in **History & Logs** on the call (dispatcher name and message summary when available).

## #Web Admin setup (administrators)

### #Notification Templates

**Web Admin** → **Notification Templates** (`/notification-templates`)

**OrgAdmin** can create templates by type:

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Type</p></th><th data-last-column="true"><p dir="auto">Use</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>Incident SMS</strong></p></td><td data-last-column="true"><p dir="auto">Standard incident notification body (160-char guidance in editor)</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Critical Alert SMS</strong></p></td><td data-last-column="true"><p dir="auto">High-urgency short alerts</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>Incident Email</strong> / <strong>Critical Alert Email</strong></p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Email counterparts</p></td></tr></tbody></table>

Template editor supports the same `**{{variable}}**` family as manual sends (see tables above). Use **Preview** in admin to test rendering.

Default **Incident SMS** pattern (example agencies use):

```
CFS #{{agency_cfs}} {{incident_type}}
RP: {{RP_FullName}} Phone: {{phone}}
Address: {{address}}

{{CallDescription}}
```

These templates drive **automated** SMS where your deployment wires incident events to notifications — separate from the manual **Send SMS** sheet, but the same variable names keep wording consistent.

### #Recipient groups

**Web Admin** → **Groups** (when available in your deployment)

- Create named groups (e.g. “Patrol Sergeants,” “Fire mutual aid”).
 
- Add members with phone numbers.
 
- Groups appear on the **Groups** tab in **Send SMS**.
 

If the Groups page is not in the sidebar, contact Cadmus support — you may still send to **Individuals** only.

### #User phone numbers

**Web Admin** → **Users** → edit user → ensure **phone number** is populated for anyone who should receive dispatch SMS.

### #User notification preferences

Per-user SMS scope (assigned calls only, all calls, critical only) affects **automated** notifications, not necessarily manual **Send SMS** from dispatch. See [User notification preferences](https://../web-admin/user-notification-preferences.md).

## #API reference

Manual send and history (authenticated dispatcher session):

<table style="--default-cell-min-width: 25px; min-width: 75px;"><colgroup><col><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Action</p></th><th><p dir="auto">Method</p></th><th data-last-column="true"><p dir="auto">Path</p></th></tr><tr><td data-first-column="true"><p dir="auto">Send SMS for call</p></td><td><p dir="auto">POST</p></td><td data-last-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">/incidents/{incidentId}/send-sms</span></code></p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">SMS history</p></td><td data-last-row="true"><p dir="auto">GET</p></td><td data-last-column="true" data-last-row="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">/incidents/{incidentId}/sms-history</span></code></p></td></tr></tbody></table>

**Send body (JSON):**

<table style="--default-cell-min-width: 25px; min-width: 75px;"><colgroup><col><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Field</p></th><th><p dir="auto">Required</p></th><th data-last-column="true"><p dir="auto">Description</p></th></tr><tr><td data-first-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">incidentId</span></code></p></td><td><p dir="auto">Yes</p></td><td data-last-column="true"><p dir="auto">CFS / incident ID</p></td></tr><tr><td data-first-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">message</span></code></p></td><td><p dir="auto">Yes</p></td><td data-last-column="true"><p dir="auto">Final or templated message text</p></td></tr><tr><td data-first-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">recipientUserIds</span></code></p></td><td><p dir="auto">One of users or groups</p></td><td data-last-column="true"><p dir="auto">Array of user IDs</p></td></tr><tr><td data-first-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">recipientGroupIds</span></code></p></td><td><p dir="auto">One of users or groups</p></td><td data-last-column="true"><p dir="auto">Array of group IDs</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">correlationId</span></code></p></td><td data-last-row="true"><p dir="auto">No</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Optional tracking ID</p></td></tr></tbody></table>

**Response:** `success`, `sentCount`, `failedCount`, `correlationId`, and per-recipient `results` (phone, status, error).

Recipient lists for the UI:

<table style="--default-cell-min-width: 25px; min-width: 75px;"><colgroup><col><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Action</p></th><th><p dir="auto">Method</p></th><th data-last-column="true"><p dir="auto">Path</p></th></tr><tr><td data-first-column="true"><p dir="auto">List groups</p></td><td><p dir="auto">GET</p></td><td data-last-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">/groups</span></code></p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">List users</p></td><td data-last-row="true"><p dir="auto">GET</p></td><td data-last-column="true" data-last-row="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">/users</span></code></p></td></tr></tbody></table>

Notification templates (admin):

<table style="--default-cell-min-width: 25px; min-width: 75px;"><colgroup><col><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Action</p></th><th><p dir="auto">Method</p></th><th data-last-column="true"><p dir="auto">Path</p></th></tr><tr><td data-first-column="true"><p dir="auto">List templates</p></td><td><p dir="auto">GET</p></td><td data-last-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">/notification-templates</span></code></p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Template variables help</p></td><td data-last-row="true"><p dir="auto">GET</p></td><td data-last-column="true" data-last-row="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">/notification-templates/variables/incident_sms</span></code></p></td></tr></tbody></table>

## #Troubleshooting

<table style="--default-cell-min-width: 25px; min-width: 75px;"><colgroup><col><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Symptom</p></th><th><p dir="auto">Likely cause</p></th><th data-last-column="true"><p dir="auto">Action</p></th></tr><tr><td data-first-column="true"><p dir="auto">No <strong>Send SMS</strong> button</p></td><td><p dir="auto">SMS not enabled for deployment</p></td><td data-last-column="true"><p dir="auto">Contact IT / Cadmus admin</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Failed to load data</strong> on open</p></td><td><p dir="auto">Groups/users API error</p></td><td data-last-column="true"><p dir="auto">Check network; verify org access</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Please select at least one recipient</strong></p></td><td><p dir="auto">No checkboxes selected</p></td><td data-last-column="true"><p dir="auto">Pick group or user</p></td></tr><tr><td data-first-column="true"><p dir="auto">All recipients <strong>failed</strong></p></td><td><p dir="auto">SMS provider misconfigured</p></td><td data-last-column="true"><p dir="auto">IT checks provider credentials</p></td></tr><tr><td data-first-column="true"><p dir="auto">Some numbers <strong>failed</strong></p></td><td><p dir="auto">Invalid or missing mobile number</p></td><td data-last-column="true"><p dir="auto">Update user profile in Web Admin</p></td></tr><tr><td data-first-column="true"><p dir="auto">Merge field shows literal <code class="inline" spellcheck="false"><span class="code-word">{{agency_cfs}}</span></code></p></td><td><p dir="auto">Typo in variable name</p></td><td data-last-column="true"><p dir="auto">Match spelling exactly (case-sensitive)</p></td></tr><tr><td data-first-column="true"><p dir="auto">Empty groups list</p></td><td><p dir="auto">No groups created</p></td><td data-last-column="true"><p dir="auto">Web Admin → Groups</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">History empty after “success”</p></td><td data-last-row="true"><p dir="auto">Refresh needed or logging delay</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Tap <strong>Refresh</strong> in SMS History</p></td></tr></tbody></table>

## #Related pages

- [Chat, SMS, and comms](https://./chat-sms-comms.md) — chat vs SMS overview
 
- [Admin and manager setup guide](https://./admin-manager-guide.md) — go-live checklist
 
- [User notification preferences](https://../web-admin/user-notification-preferences.md)
 
- [Messaging commands](https://./command-line/messaging-commands.md) — **MSG** / **BC** (unit chat, not SMS)
 

## #Warnings

> **Warning:** SMS to field units is not a secure CJIS channel — do not include NCIC returns, SSNs, or criminal history in text.

> **Warning:** Reporting party phone numbers in messages may be PII — follow agency policy on sharing RP data with third parties.

> **Warning:** Confirm recipient list before send — group selections can include many numbers at once.

> **Warning:** Carrier delivery is not guaranteed — use radio or unit status for life-safety confirmations.

 [Outline](https://www.getoutline.com?ref=sharelink)