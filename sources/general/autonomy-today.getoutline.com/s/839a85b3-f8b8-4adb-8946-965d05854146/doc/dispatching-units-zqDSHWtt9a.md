# Source: https://autonomy-today.getoutline.com/s/839a85b3-f8b8-4adb-8946-965d05854146/doc/dispatching-units-zqDSHWtt9a

Dispatching units

Assign units and progress status from dashboard or call detail.

> Screenshot placeholder: Assign Unit flow on call detail

## #Assign from call detail

1. Open the CFS.
 
2. In **Units** block or **Quick Actions**, choose **Assign Unit**.
 
3. Select unit from available list or **AVAILABLE UNITS** row.
 
4. Confirm assignment — unit status typically moves to dispatched.
 

## #Assign from dashboard

- Drag unit from sidebar onto call card.
 
- Or use command line: `DU A23 #26-00045` — see [Command Line](https://./command-line/getting-started.md).
 

## #Status progression

Typical path:

**Available → Dispatched → Enroute → On scene → Clear**

Quick status chips on call detail:

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Chip</p></th><th data-last-column="true"><p dir="auto">Meaning</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>DISP</strong></p></td><td data-last-column="true"><p dir="auto">Dispatched</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>ENRT</strong></p></td><td data-last-column="true"><p dir="auto">Enroute</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>SCENE</strong></p></td><td data-last-column="true"><p dir="auto">On scene</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>CLR</strong></p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Cleared from call</p></td></tr></tbody></table>

> Screenshot placeholder: Unit row with status chips on call detail

## #Quick status change

From units sidebar without opening call:

- **Quick status change** on unit menu when supported.
 

## #Remove unit from call

- **Clear Call** / **CU** command removes unit assignment.
 
- Confirm unit is not needed before clearing.
 

## #Conflicts

If unit is on another call, server returns error toast — clear from other incident first or reassign.

## #Multi-unit assign

On call detail command line (in-call mode):

`ASSIGN @351 @422 @M1`

See [In-call commands](https://./command-line/in-call-commands.md).

## #Tips

- Assign closest available unit when policy allows.
 
- Update enroute/on scene promptly for accurate board state.
 
- Use greaseboard (F5) for big-picture unit picture.
 

## #Warnings

> **Warning:** Clearing primary unit on active in-progress call may violate SOP — confirm with supervisor.

 [Outline](https://www.getoutline.com?ref=sharelink)