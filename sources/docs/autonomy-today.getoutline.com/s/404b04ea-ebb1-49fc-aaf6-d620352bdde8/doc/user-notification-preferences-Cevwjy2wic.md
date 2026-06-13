# Source: https://autonomy-today.getoutline.com/s/404b04ea-ebb1-49fc-aaf6-d620352bdde8/doc/user-notification-preferences-Cevwjy2wic

User notification preferences

Per-user notification controls in **Web Admin**.

**Scope:** User (within selected organization).

## #Open

1. Go to **Users**.
 
2. Select a user.
 
3. Open **Notification Preferences** tab.
 

> Screenshot placeholder: Notification Preferences tab on user detail (requires user selected)

## #What you can configure

Options depend on deployment; typical areas:

- Email or in-app notifications for incident types
 
- Alert channels tied to notification templates/policies
 

> **Availability note:** Organization-wide **Notification Policies** may not appear in all deployments. Use the user tab and **Notification Templates** under org configuration when the policies page is unavailable.

## #Related configuration

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Item</p></th><th data-last-column="true"><p dir="auto">Location</p></th></tr><tr><td data-first-column="true"><p dir="auto">Message templates</p></td><td data-last-column="true"><p dir="auto"><strong>Notification Templates</strong> (<code class="inline" spellcheck="false"><span class="code-word">/notification-templates</span></code>) — see <strong>Dispatch CAD</strong> <a href="https://../dispatch-cad/sms-templates-and-messaging.md" class="use-hover-preview" rel="noopener noreferrer nofollow">SMS templates and messaging</a></p></td></tr><tr><td data-first-column="true"><p dir="auto">Incident type linkage</p></td><td data-last-column="true"><p dir="auto">Organization incident types</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Dispatch CAD alerts</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Dispatch CAD audio/UI (see Dispatch CAD troubleshooting)</p></td></tr></tbody></table>

## #Common mistakes

- Changing templates but not user preferences (user still opted out).
 
- Expecting SMS from admin toggles alone—SMS requires a configured SMS service.
 

## #Dispatch and mobile impact

Preferences filter which notifications a user receives; they do not change CFS data on the board.

## #Tips

- Set preferences for supervisors separately from line dispatchers.
 
- After template changes, ask users to reload **Dispatch CAD**.
 

## #Warnings

> **Warning:** Disabling all notifications may cause missed critical alerts—document agency minimums.

 [Outline](https://www.getoutline.com?ref=sharelink)