# Source: https://autonomy-today.getoutline.com/s/839a85b3-f8b8-4adb-8946-965d05854146/doc/new-cfs-form-fields-RjmRbiqync

New CFS form fields

Field-by-field guide for **Create New Call for Service** (F1).

> Screenshot placeholder: Create New Call for Service dialog — full form

## #Required fields

<table style="--default-cell-min-width: 25px; min-width: 75px;"><colgroup><col><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Field</p></th><th><p dir="auto">Label</p></th><th data-last-column="true"><p dir="auto">Notes</p></th></tr><tr><td data-first-column="true"><p dir="auto">Incident type</p></td><td><p dir="auto"><strong>Incident Type *</strong></p></td><td data-last-column="true"><p dir="auto">Select from list — do not rely on free text alone</p></td></tr><tr><td data-first-column="true"><p dir="auto">Location</p></td><td><p dir="auto"><strong>Location *</strong></p></td><td data-last-column="true"><p dir="auto">Address, cross street, or common place</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Details</p></td><td data-last-row="true"><p dir="auto"><strong>Incident Details *</strong></p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Who, what, where, immediate risks</p></td></tr></tbody></table>

See also [Create CFS workflow](https://./create-cfs-workflow.md).

## #Priority and type

- **Priority Level \*** — numeric priority (1 Emergency … 4 Low typical).
 
- Incident type drives tags and downstream workflows.
 

> Screenshot placeholder: Incident type dropdown with search

## #Location modes

- Street address with validation feedback.
 
- Cross street when no exact address.
 
- Common place from org-configured list.
 
- **Geo verified** indicator when GIS validates.
 

> Screenshot placeholder: Location field with Geo verified badge

## #Address validation

While typing:

- **Validating address…** spinner may appear.
 
- Follow snackbar or inline cues before submitting.
 

See agency GIS settings in **Web Admin**.

> Screenshot placeholder: Address validation message under location field

## #Reporting party

- **RP same as scene** — copy scene location to RP when appropriate.
 
- **Add Phone Number** — additional callback numbers.
 
- **Add Caller** — secondary reporting parties at create time.
 

> Screenshot placeholder: Reporting party section expanded

## #Timer

- **Disable Timer** — skip default status timer when policy allows.
 

## #Vehicles at create

- **Add Vehicle** — optional vehicle record at creation.
 

## #Actions

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Button</p></th><th data-last-column="true"><p dir="auto">Effect</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>Create Call</strong></p></td><td data-last-column="true"><p dir="auto">Saves CFS and opens call detail</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Drop Call</strong></p></td><td data-last-column="true"><p dir="auto">Abandon without saving (confirm if prompted)</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Done</strong></p></td><td data-last-column="true"><p dir="auto">Close dialog after save</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>Append note</strong></p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Add narrative after initial create</p></td></tr></tbody></table>

## #Tips

- Select incident type from list after typing 2–4 letters.
 
- Use cross street when address unknown — update when corrected.
 
- Create first, add images in call detail **History/Logs**.
 

## #Warnings

> **Warning:** Unvalidated addresses may geocode incorrectly — verify map pin after create.

> **Warning:** **Drop Call** may discard entered data — use only when intentionally canceling.

 [Outline](https://www.getoutline.com?ref=sharelink)