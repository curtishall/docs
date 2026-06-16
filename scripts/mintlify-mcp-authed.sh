#!/usr/bin/env bash
# Mintlify authenticated search MCP proxy for Cursor.
# Reads credentials from ~/.config/cadmus/mintlify-mcp.env (not committed).
set -euo pipefail

ENV_FILE="${MINTLIFY_MCP_ENV_FILE:-$HOME/.config/cadmus/mintlify-mcp.env}"
if [[ -f "$ENV_FILE" ]]; then
  # shellcheck disable=SC1090
  source "$ENV_FILE"
fi

: "${MINTLIFY_MCP_CLIENT_ID:?Set MINTLIFY_MCP_CLIENT_ID in $ENV_FILE}"
: "${MINTLIFY_MCP_CLIENT_SECRET:?Set MINTLIFY_MCP_CLIENT_SECRET in $ENV_FILE}"

MCP_BASE="${MINTLIFY_MCP_BASE_URL:-https://cadmus.mintlify.app}"
TOKEN_URL="${MCP_BASE}/authed/mcp/oauth/token"
MCP_URL="${MCP_BASE}/authed/mcp"

TOKEN_RESPONSE="$(
  curl -sS -X POST "$TOKEN_URL" \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d "grant_type=client_credentials&client_id=${MINTLIFY_MCP_CLIENT_ID}&client_secret=${MINTLIFY_MCP_CLIENT_SECRET}"
)"

if ! ACCESS_TOKEN="$(python3 - <<'PY' "$TOKEN_RESPONSE"
import json, sys
data = json.loads(sys.argv[1])
if "access_token" not in data:
    raise SystemExit(f"Token exchange failed: {data}")
print(data["access_token"])
PY
)"; then
  echo "Mintlify MCP token exchange failed. Check credentials and that authenticated MCP is enabled in the Mintlify dashboard." >&2
  exit 1
fi

exec npx -y mcp-remote@0.1.29 "$MCP_URL" --header "Authorization:Bearer ${ACCESS_TOKEN}"
