# Source: https://autonomy-today.getoutline.com/s/404b04ea-ebb1-49fc-aaf6-d620352bdde8/doc/rapidsos-management-BEprumWLfu

RapidSOS management

Configure RapidSOS credentials so **Dispatch CAD** can receive emergency location data, run phone lookups, and show device locations on the map.

**Audience:** **OrgAdmin** or **CadmusAdmin**. **AgencyAdmin** and dispatchers cannot access this page.

> Screenshot placeholder: RapidSOS Management page with credentials table

## #Open

**Web Admin** sidebar → **RapidSOS Management**

Admin URL: `/rapidsos`

## #Who can access

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Role</p></th><th data-last-column="true"><p dir="auto">Access</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>OrgAdmin</strong></p></td><td data-last-column="true"><p dir="auto">Own organization</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>CadmusAdmin</strong></p></td><td data-last-column="true"><p dir="auto">All organizations</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>AgencyAdmin</strong></p></td><td data-last-column="true"><p dir="auto">No</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>Dispatcher</strong></p></td><td data-last-column="true" data-last-row="true"><p dir="auto">No</p></td></tr></tbody></table>

If the menu item is missing, your role lacks access — contact a Cadmus administrator.

## #Credentials table

Lists organizations with RapidSOS status:

- Organization name
 
- **Sandbox** configuration status
 
- **Production** configuration status
 
- Created date
 
- Client ID (truncated)
 

Use the search/filter bar to find an organization.

Summary cards may show counts of configured vs not configured tenants.

> Screenshot placeholder: Organization row with Sandbox and Production badges

## #Set credentials

1. Select organization (if you manage more than one).
 
2. **Set Credentials** (or edit from the row actions menu **⋮**).
 
3. Complete the form:
 

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Field</p></th><th data-last-column="true"><p dir="auto">Notes</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>Environment</strong></p></td><td data-last-column="true"><p dir="auto">Sandbox or Production</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Client ID</strong></p></td><td data-last-column="true"><p dir="auto">From RapidSOS portal</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Client Secret</strong></p></td><td data-last-column="true"><p dir="auto">Stored securely; re-enter when rotating</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Base URL</strong></p></td><td data-last-column="true"><p dir="auto">Pre-filled per environment when available</p></td></tr><tr><td data-first-column="true"><p dir="auto"><strong>Token Endpoint</strong></p></td><td data-last-column="true"><p dir="auto">OAuth token URL</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>IRP Token Endpoint</strong></p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Optional; for IRP-specific flows</p></td></tr></tbody></table>

4. Optional: **Test** before save — see below.
 
5. Save credentials.
 

### #Default endpoints (typical)

<table style="--default-cell-min-width: 25px; min-width: 75px;"><colgroup><col><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Environment</p></th><th><p dir="auto">API base</p></th><th data-last-column="true"><p dir="auto">WebSocket (location stream)</p></th></tr><tr><td data-first-column="true"><p dir="auto"><strong>Sandbox</strong></p></td><td><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">https://api-sandbox.rapidsos.com</span></code></p></td><td data-last-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">wss://ws.edx-sandbox.rapidsos.com/v1</span></code></p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto"><strong>Production</strong></p></td><td data-last-row="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">https://api.rapidsos.com</span></code></p></td><td data-last-column="true" data-last-row="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">wss://ws.edx.rapidsos.com/v1</span></code></p></td></tr></tbody></table>

Your Cadmus implementer may override WebSocket URLs for special network routing — ask IT if lookups work but live tracks fail.

## #Test credentials

Before or after saving, run **Test Credentials**:

- OAuth token generation
 
- **RAD-E** API connection
 
- **LEI** API connection
 

Provide a **test caller ID** in E.164 format (e.g. `+15555555556`) when prompted for phone-based tests.

The test dialog shows pass/fail per check. Fix errors before relying on RapidSOS in production dispatch.

> Screenshot placeholder: Credential test results dialog

## #Edit and delete

From the row **⋮** menu:

- **Edit** — update secrets or endpoints
 
- **Test** — re-run connectivity checks
 
- **Delete** — remove configuration for that environment (dispatch loses RapidSOS for that org until reconfigured)
 

## #What happens after save

Once credentials are valid and services are running:

1. RapidSOS WebSocket connects for the organization.
 
2. Emergency location alerts can create or enrich incidents automatically (per your deployment rules).
 
3. **Dispatch CAD** map layers **RapidSOS Locations** and **RapidSOS Breadcrumbs** receive live data.
 
4. **Track Phone Number** and **RapidSOS Lookup** dialogs can query LEI/RAD-E.
 

Field verification: see **Dispatch CAD** [Map and location](https://../dispatch-cad/map-and-location.md).

## #Sandbox vs production

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Use</p></th><th data-last-column="true"><p dir="auto">Environment</p></th></tr><tr><td data-first-column="true"><p dir="auto">Training, demos, go-live rehearsal</p></td><td data-last-column="true"><p dir="auto"><strong>Sandbox</strong></p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Live 911 / emergency operations</p></td><td data-last-column="true" data-last-row="true"><p dir="auto"><strong>Production</strong></p></td></tr></tbody></table>

Configure **both** if you maintain separate Sandbox and Live Cadmus organizations. Match each Cadmus org to the correct RapidSOS environment.

Never point a **Live** dispatch org at Sandbox credentials.

## #API reference (administrators)

<table style="--default-cell-min-width: 25px; min-width: 75px;"><colgroup><col><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Action</p></th><th><p dir="auto">Method</p></th><th data-last-column="true"><p dir="auto">Path</p></th></tr><tr><td data-first-column="true"><p dir="auto">List credentials</p></td><td><p dir="auto">GET</p></td><td data-last-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">/admin/organizations/{orgId}/rapidsos/credentials</span></code></p></td></tr><tr><td data-first-column="true"><p dir="auto">Save credentials</p></td><td><p dir="auto">POST</p></td><td data-last-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">/admin/organizations/{orgId}/rapidsos/credentials</span></code></p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Test credentials</p></td><td data-last-row="true"><p dir="auto">POST</p></td><td data-last-column="true" data-last-row="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">/admin/organizations/{orgId}/rapidsos/test</span></code></p></td></tr></tbody></table>

## #Troubleshooting

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Symptom</p></th><th data-last-column="true"><p dir="auto">Checks</p></th></tr><tr><td data-first-column="true"><p dir="auto">Page not in sidebar</p></td><td data-last-column="true"><p dir="auto">Role must be OrgAdmin or CadmusAdmin</p></td></tr><tr><td data-first-column="true"><p dir="auto">Test fails on token</p></td><td data-last-column="true"><p dir="auto">Client ID/secret, token endpoint URL</p></td></tr><tr><td data-first-column="true"><p dir="auto">Test passes, no map data</p></td><td data-last-column="true"><p dir="auto">Wrong environment (sandbox vs production); WebSocket connectivity from server</p></td></tr><tr><td data-first-column="true"><p dir="auto">Lookup works, no auto-incidents</p></td><td data-last-column="true"><p dir="auto">Deployment incident rules; confirm with Cadmus support</p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Dispatchers see no F4 tools</p></td><td data-last-column="true" data-last-row="true"><p dir="auto">Credentials saved for wrong organization; user signed into different org</p></td></tr></tbody></table>

## #Verification checklist

1. Credentials saved for correct org and environment.
 
2. Test dialog all green.
 
3. Dispatcher runs **RapidSOS Lookup** on a known test number (sandbox).
 
4. Map layer **RapidSOS Locations** toggles on and shows a pin when tracking.
 
5. Document credential rotation date and RapidSOS portal owner.
 

## #Related pages

- [Integrations settings](https://./integrations-settings.md) — org settings overview
 
- **Dispatch CAD** [Map and location](https://../dispatch-cad/map-and-location.md) — dispatcher tools
 
- [Organization and agency basics](https://./organization-and-agency-basics.md) — Sandbox vs Live orgs
 

## #Warnings

> **Warning:** Client secrets are criminal-justice sensitive — do not paste into email or chat.

> **Warning:** Production RapidSOS misconfiguration can block live location during emergencies — test in Sandbox before cutover.

 [Outline](https://www.getoutline.com?ref=sharelink)