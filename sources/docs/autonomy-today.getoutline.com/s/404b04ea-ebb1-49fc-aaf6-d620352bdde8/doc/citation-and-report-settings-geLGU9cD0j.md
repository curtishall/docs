# Source: https://autonomy-today.getoutline.com/s/404b04ea-ebb1-49fc-aaf6-d620352bdde8/doc/citation-and-report-settings-geLGU9cD0j

Citation and report settings

Citation templates and RMS report numbering for an agency.

**Scope:** Agency (settings page + citation designer).

> Screenshot placeholder: Agency citation settings section (requires AgencyAdmin)

## #Citations

On agency settings page, **Citation** section includes:

- Citation template configuration
 
- PDF designer (when enabled)
 

### #Typical workflow

1. Open `/agencies/{agencyId}/settings`.
 
2. Scroll to **Citations**.
 
3. Configure template fields and layout.
 
4. Save and test print/PDF with training user.
 

> Screenshot placeholder: Citation template designer (requires citation module enabled)

## #Report numbers

Controlled by agency settings:

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Setting</p></th><th data-last-column="true"><p dir="auto">Effect</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>Separate RMS report numbers</strong> OFF</p></td><td data-last-column="true"><p dir="auto">Report number matches CFS</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>Separate RMS report numbers</strong> ON</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Uses <strong>Report number format</strong> template</p></td></tr></tbody></table>

### #Format tokens

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Token</p></th><th data-last-column="true"><p dir="auto">Output</p></th></tr><tr><td data-first-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">{YYYY}</span></code></p></td><td data-last-column="true"><p dir="auto">4-digit year</p></td></tr><tr><td data-first-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">{YY}</span></code></p></td><td data-last-column="true"><p dir="auto">2-digit year</p></td></tr><tr><td data-first-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">{NNNN}</span></code></p></td><td data-last-column="true"><p dir="auto">4-digit sequence</p></td></tr><tr><td data-first-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">{NNNNNN}</span></code></p></td><td data-last-column="true"><p dir="auto">6-digit sequence</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">{AGENCY}</span></code></p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Agency abbreviation</p></td></tr></tbody></table>

Example: `{YY}-{NNNN}` → `26-0042`

### #Sequence seed

Super admins may set sequence seed when separate numbering is enabled—use only during initial go-live.

> Screenshot placeholder: Report number info / seed controls (requires separate numbering enabled)

## #Dispatch and mobile impact

- Deputies generate citations from call detail when **Traffic Stops Allowed** is on.
 
- Closing call with **Report to Follow** triggers report number assignment per agency rules.
 

See **Dispatch CAD** documentation: [Call detail overview](https://../dispatch-cad/call-detail-overview.md)

## #Common mistakes

- Editing template after citations already issued (historical PDF mismatch).
 
- Wrong `{AGENCY}` abbreviation in format string.
 
- Enabling separate numbers without training records staff.
 

## #Tips

- Test one citation in Sandbox before Live.
 
- Document format string in agency SOP.
 
- Align with RMS vendor field requirements.
 

## #Warnings

> **Warning:** Report number gaps may occur if calls are deleted or workflows aborted—records should reconcile sequences.

> **Warning:** Citation templates may be legal documents—have agency attorney review before production use.

 [Outline](https://www.getoutline.com?ref=sharelink)