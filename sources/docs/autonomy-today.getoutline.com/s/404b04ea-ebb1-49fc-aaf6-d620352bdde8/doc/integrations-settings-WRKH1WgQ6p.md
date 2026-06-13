# Source: https://autonomy-today.getoutline.com/s/404b04ea-ebb1-49fc-aaf6-d620352bdde8/doc/integrations-settings-WRKH1WgQ6p

Integrations settings

RapidSOS, CJIS, RMS, and ATAK configuration touchpoints.

Settings span **organization** and **agency** scopes.

## #Organization Settings (`/settings`)

**Scope:** Organization. Some cards require **CadmusAdmin**.

> Screenshot placeholder: Organization Settings page (requires OrgAdmin)

### #Geographic service area

- Radius and map center for geocoding / “outside coverage” behavior
 
- Affects **Dispatch CAD** address validation
 

See **Dispatch CAD** documentation: [Map and location](https://../dispatch-cad/map-and-location.md)

### #CFS number sharing

- Toggle **Enable CFS sharing** across agencies in org
 

### #Clerk membership & user sync

- Sync Clerk org memberships and users after bulk changes
 

### #CJIS site (CadmusAdmin)

- Per-organization **target site** for NCIC/ConnectCIC relay
 
- Required before agency NCIC toggles work end-to-end
 

> Screenshot placeholder: CJIS site configuration card (requires CadmusAdmin)

Test NCIC from **Dispatch CAD** after CJIS site is saved.

### #RMS webhook (CadmusAdmin)

- Outbound webhook when incidents update
 
- URL, secret, enable flag
 

**Dispatch CAD** may show RMS submission status on call detail when configured.

### #ATAK / TAK integration

Configure TAK server connection on the Settings page when your deployment includes ATAK integration.

> Screenshot placeholder: ATAK integration panel (requires ATAK feature enabled)

## #RapidSOS

Dedicated page: **RapidSOS Management** (`/rapidsos`)

Configure RapidSOS keys in the RapidSOS Management page. For step-by-step credential setup, testing, and troubleshooting, see [RapidSOS management](https://./rapidsos-management.md).

**Dispatch CAD:** header **F4** / RapidSOS dialogs when enabled.

## #Agency-level access toggles

**State/NCIC Access** on agency settings works with org CJIS site.

See [agency-settings-core.md](https://agency-settings-core.md)

## #Quick calls & command integration

Not on Settings page but affect integrations:

<table style="--default-cell-min-width: 25px; min-width: 50px;"><colgroup><col><col></colgroup><tbody><tr><th data-first-column="true"><p dir="auto">Feature</p></th><th data-last-column="true"><p dir="auto">Path</p></th></tr><tr><td data-first-column="true"><p dir="auto">Quick Call Shortcuts</p></td><td data-last-column="true"><p dir="auto">Organization quick call page</p></td></tr><tr><td data-first-column="true"><p dir="auto">Command aliases</p></td><td data-last-column="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">/agencies/{id}/command-aliases</span></code></p></td></tr><tr><td data-first-column="true" data-last-row="true"><p dir="auto">Call type shortcodes</p></td><td data-last-column="true" data-last-row="true"><p dir="auto"><code class="inline" spellcheck="false"><span class="code-word">/agencies/{id}/call-type-shortcodes</span></code></p></td></tr></tbody></table>

## #Common mistakes

- Enabling NCIC at agency without CJIS site on org.
 
- RMS webhook URL pointing to dev endpoint in production org.
 
- RapidSOS keys in wrong org (Live vs Sandbox).
 

## #Verification checklist

1. CJIS site saved for org (CadmusAdmin).
 
2. Agency **State/NCIC Access** on for test agency.
 
3. User override or default allows test user.
 
4. Run test query from **Dispatch CAD** on training call.
 
5. RapidSOS lookup returns data in dev sandbox.
 
6. RMS test webhook receives sample payload.
 

## #Warnings

> **Warning:** CJIS credentials and site routing are criminal justice sensitive—limit CadmusAdmin access.

> **Warning:** Webhook secrets in screenshots or tickets—rotate if exposed.

 [Outline](https://www.getoutline.com?ref=sharelink)