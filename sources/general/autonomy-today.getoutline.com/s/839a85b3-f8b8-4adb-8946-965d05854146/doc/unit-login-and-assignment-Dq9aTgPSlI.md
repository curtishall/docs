# Source: https://autonomy-today.getoutline.com/s/839a85b3-f8b8-4adb-8946-965d05854146/doc/unit-login-and-assignment-Dq9aTgPSlI

Unit login and assignment

Log crew onto units, manage off-duty pool, and assign units to calls.

## #Login User (F2)

Opens the **Unit Assignment** dialog:

- Filter units by beat, agency, or unit type.
 
- **Logon** — add crew to a unit.
 
- **Logout all crew** — clear entire unit.
 
- Filters: **All Beats**, **All Agencies**, **All Unit Types**.
 

> Screenshot placeholder: Unit Assignment dialog with unit list and Logon button

## #Active Units sidebar

- Lists on-duty units with current status.
 
- **Units list density** — compact vs comfortable.
 
- Filter **All** or by status.
 

> Screenshot placeholder: Active Units sidebar with status colors

## #Unit context menu

Right-click or menu on a unit row:

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Action</p></th><th data-last-column="true"><p dir="auto">Notes</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>Create Call</strong></p></td><td data-last-column="true"><p dir="auto">Start call tied to unit</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Off Duty</strong></p></td><td data-last-column="true"><p dir="auto">Move unit off duty</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Mark Available</strong></p></td><td data-last-column="true"><p dir="auto">Return to available</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Logout User</strong></p></td><td data-last-column="true"><p dir="auto">Remove one crew member</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>Devices…</strong></p></td><td data-last-column="true" data-last-row="true"><p dir="auto">MDT device enrollment</p></td></tr></tbody></table>

Some items may show **Coming soon** (e.g. Traffic Stop from sidebar, Memo Location).

> Screenshot placeholder: Unit context menu

## #Off-duty and batch login

- **Off Duty** sidebar section lists available off-duty units.
 
- **Batch Log In** / **Batch Log In Units** — log multiple units at shift start.
 

> Screenshot placeholder: Off Duty section with Batch Log In

## #Set unit off duty

Dialog: **Set {unit} Off Duty**

- Confirm crew is logged off first when policy requires.
 
- Error toast **Cannot Set {unit} Off Duty** if unit is on an active call.
 

## #Logout user from unit

**Logout User from {unit}** — removes one officer without clearing the whole unit.

## #Unit greaseboard (F5)

- **Units** (F5) or **Unit greaseboard** opens live status grid.
 
- Options: **Open in new window**, **Table view**, **Sort: Status**.
 
- Online/offline indicators per unit.
 

> Screenshot placeholder: Unit greaseboard grid view

## #Unit devices (MDT enrollment)

From **Devices for {unit}**:

- Enroll mobile/tablet MDT for the unit.
 
- **Copy** activation code for field device setup.
 
- **Revoke device?** when decommissioning hardware.
 

> Screenshot placeholder: Unit devices enrollment dialog

## #Client impact from Web Admin

- Units and crews are configured in **Web Admin** (Units pages).
 
- NCIC and traffic-stop behavior follows agency settings.
 

## #Common mistakes

- Logging unit on duty but not assigning to call (call still pending).
 
- Setting unit off duty while still assigned to open CFS.
 
- Forgetting batch login at major shift change.
 

## #Warnings

> **Warning:** Logout and off-duty actions affect field MDT login state — coordinate with officers before forcing logout.

 [Outline](https://www.getoutline.com?ref=sharelink)