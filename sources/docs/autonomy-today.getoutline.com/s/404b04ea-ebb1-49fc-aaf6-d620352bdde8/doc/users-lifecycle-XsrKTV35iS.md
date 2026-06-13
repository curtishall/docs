# Source: https://autonomy-today.getoutline.com/s/404b04ea-ebb1-49fc-aaf6-d620352bdde8/doc/users-lifecycle-XsrKTV35iS

Users lifecycle

Invite, edit, and deactivate users in your organization.

**Scope:** Organization (users belong to org; agency assignments vary).

> Screenshot placeholder: Users list page (requires OrgAdmin session)

## #Open Users

Navigation: **Users** → `/users`

Requires OrgAdmin or higher (agency-scoped views may use `/agencies/{id}/users`).

## #Invite a user

1. Select **Invite** or **Add user**.
 
2. Enter email and assign **role** (Dispatcher, AgencyAdmin, etc.).
 
3. Assign **agencies** if prompted.
 
4. Send invite.
 

Clerk sends email with sign-up link. Contact IT if redirects fail.

> Screenshot placeholder: User invite dialog (requires invite permissions)

## #Edit a user

1. Open user row → **Edit**.
 
2. Update name, role, agency access, active flag.
 
3. Save.
 

Role changes take effect on next sign-in (sidebar may update immediately).

## #Deactivate

Deactivate instead of delete when someone leaves:

- Blocks sign-in
 
- Preserves audit history
 

Confirm no critical workflows depend on that user’s API keys.

## #Notification preferences tab

On user detail, open **Notification Preferences** tab.

See [user-notification-preferences.md](https://user-notification-preferences.md).

## #Import / export

Users page may include import/export panel for bulk CSV operations (when enabled).

> Screenshot placeholder: User import panel (requires import feature enabled)

## #Clerk sync (org settings)

Org **Settings** may offer:

- Sync Clerk memberships
 
- Sync Clerk users
 

Use after bulk changes in Clerk dashboard.

> Screenshot placeholder: Clerk sync cards on Settings page (requires OrgAdmin)

## #Common mistakes

- Inviting with wrong role (ReadOnly-Calls vs Dispatcher).
 
- Forgetting agency assignment for agency-scoped dispatchers.
 
- Deactivating user still listed as unit crew—log them out in **Dispatch CAD** first.
 

## #Dispatch and mobile impact

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Action</p></th><th data-last-column="true"><p dir="auto">Effect</p></th></tr><tr><td data-first-column="true"><p dir="auto">Role → Dispatcher</p></td><td data-last-column="true"><p dir="auto">Can use <strong>Dispatch CAD</strong></p></td></tr><tr><td data-first-column="true"><p dir="auto">Role → ReadOnly-Calls</p></td><td data-last-column="true"><p dir="auto">Incidents-only admin access</p></td></tr><tr><td data-first-column="true"><p dir="auto">Deactivate</p></td><td data-last-column="true"><p dir="auto">Cannot sign in to <strong>Dispatch CAD</strong> or <strong>Web Admin</strong></p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Agency change</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">May change visible units/calls</p></td></tr></tbody></table>

## #Warnings

> **Warning:** OrgAdmin can see all agencies in the org—assign minimum role needed.

> **Warning:** Re-inviting same email may conflict if old Clerk user exists—check Clerk dashboard.

 [Outline](https://www.getoutline.com?ref=sharelink)