# Source: https://autonomy-today.getoutline.com/s/839a85b3-f8b8-4adb-8946-965d05854146/doc/quick-calls-and-f-keys-8tPe0w0VBZ

Quick calls and F-keys

Keyboard shortcuts and org-configured quick call templates.

> Screenshot placeholder: Header showing F1–F5 and quick call buttons

## #Function keys (header)

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Key</p></th><th data-last-column="true"><p dir="auto">Action</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>F1</strong></p></td><td data-last-column="true"><p dir="auto"><strong>New CFS</strong></p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>F2</strong></p></td><td data-last-column="true"><p dir="auto"><strong>Login User</strong></p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>F3</strong></p></td><td data-last-column="true"><p dir="auto"><strong>Query</strong> (law enforcement / NCIC enabled)</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>F4</strong></p></td><td data-last-column="true"><p dir="auto"><strong>Map</strong> (RapidSOS may use F4 in training/sandbox environments)</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>F5</strong></p></td><td data-last-column="true" data-last-row="true"><p dir="auto"><strong>Units</strong> / unit greaseboard</p></td></tr></tbody></table>

## #Quick call templates (F8–F12)

Org-configured templates appear in the header. Defaults vary by agency; common examples:

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Key</p></th><th data-last-column="true"><p dir="auto">Typical template</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>F8</strong></p></td><td data-last-column="true"><p dir="auto"><strong>Traffic Stop</strong></p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>F9</strong></p></td><td data-last-column="true"><p dir="auto"><strong>Follow-up</strong></p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>F10</strong></p></td><td data-last-column="true"><p dir="auto"><strong>Paper Service</strong></p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">F11–F12</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Additional org templates</p></td></tr></tbody></table>

**More quick calls** menu holds overflow templates.

> Screenshot placeholder: Quick call buttons F8–F12 in header

Configure templates in **Web Admin** → Quick Call Shortcuts.

## #Traffic stop quick call

- Opens traffic-stop workflow with plate entry.
 
- **Run Plate** — query before create when configured.
 
- **Create Traffic Stop** — creates CFS with template type.
 

> Screenshot placeholder: Traffic stop quick call dialog

## #Follow-up and paper service

- **Follow-up** — links to prior activity; may assign unit on create.
 
- **Paper Service** — service-of-paper template with location and unit.
 

## #Tips

- Learn your agency's F8–F12 mappings — they differ per org.
 
- After admin changes templates, **Reload Data**.
 
- Quick calls still create normal CFS records — verify location before submit.
 

## #Warnings

> **Warning:** Traffic stop template may require **Traffic Stops Allowed** in agency settings.

> **Warning:** RapidSOS header shortcut may be unavailable in some live deployments — use map-side tracking when applicable.

 [Outline](https://www.getoutline.com?ref=sharelink)