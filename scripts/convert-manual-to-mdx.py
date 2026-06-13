#!/usr/bin/env python3
"""Convert manual/docs markdown to Mintlify MDX with link fixes and callouts."""

from __future__ import annotations

import re
from pathlib import Path

MANUAL = Path("/home/curt/apps/cadmus/manual/docs")
CAD_DOCS = Path(__file__).resolve().parents[1]

# manual stem -> mintlify page slug (no extension)
MOBILE_MAP = {
    "intro": "introduction",
    "calls-list": "calls-list",
    "call-details": "call-details",
    "close-call": "close-call",
    "unit-status": "unit-status",
    "dispatch-notes": "dispatch-notes",
    "find-a-call": "find-a-call",
    "ncic-overview": "ncic-overview",
    "ecitations-overview": "ecitations-overview",
    "evidence-capture": "evidence-capture",
    "dashboard-overview": "dashboard-overview",
    "map-and-navigation": "map-and-navigation",
    "bolos-and-warrants": "bolos-and-warrants",
    "unit-chat": "unit-chat",
    "unit-calendar": "unit-calendar",
    "voice-alerts": "voice-alerts",
    "profile-and-unit": "profile-and-unit",
    "connectivity-offline": "connectivity-offline",
    "settings-and-display": "settings-and-display",
    "training-mode": "training-mode",
}

DISPATCH_TOP_MAP = {
    "intro": None,  # handled separately
    "sms-templates-and-messaging": "sms-templates-messaging",
    "admin-manager-guide": "admin-manager-guide",
}

DISPATCH_CMD_MAP = {
    "overview": "command-line-overview",
    "getting-started": "command-line-getting-started",
    "command-reference": "command-reference",
    "smart-triggers": "smart-triggers",
    "creating-calls": "creating-calls-command-line",
    "unit-status-commands": "unit-status-commands",
    "in-call-commands": "in-call-commands",
    "messaging-commands": "messaging-commands",
    "query-commands": "query-commands",
    "admin-configuration": "command-admin-configuration",
    "tips-and-shortcuts": "command-tips-shortcuts",
}

WEB_ADMIN_MAP = {
    "roles-reference": "roles-reference",
}

DISPATCH_LINK = {
    "intro": "introduction",
    "getting-started": "getting-started",
    "dashboard-overview": "dashboard-overview",
    "create-cfs-workflow": "create-cfs",
    "new-cfs-form-fields": "cfs-form-fields",
    "call-detail-overview": "call-detail",
    "close-call": "close-call",
    "unit-login-and-assignment": "unit-login",
    "dispatching-units": "dispatching-units",
    "quick-calls-and-f-keys": "quick-calls-fkeys",
    "map-and-location": "map-and-location",
    "chat-sms-comms": "chat-sms-comms",
    "sms-templates-and-messaging": "sms-templates-messaging",
    "bolo-greaseboard-wrecker": "bolo-greaseboard-wrecker",
    "queries-ncic": "queries-ncic",
    "find-a-call": "find-a-call",
    "troubleshooting": "troubleshooting",
    "admin-manager-guide": "admin-manager-guide",
    "command-line/overview": "command-line-overview",
    "command-line/getting-started": "command-line-getting-started",
    "command-line/command-reference": "command-reference",
    "command-line/smart-triggers": "smart-triggers",
    "command-line/creating-calls": "creating-calls-command-line",
    "command-line/unit-status-commands": "unit-status-commands",
    "command-line/in-call-commands": "in-call-commands",
    "command-line/messaging-commands": "messaging-commands",
    "command-line/query-commands": "query-commands",
    "command-line/admin-configuration": "command-admin-configuration",
    "command-line/tips-and-shortcuts": "command-tips-shortcuts",
}

WEB_LINK = {
    "intro": "introduction",
    "roles-and-access": "roles-and-access",
    "roles-reference": "roles-reference",
    "organization-and-agency-basics": "organization-agency-basics",
    "users-lifecycle": "users-lifecycle",
    "user-notification-preferences": "user-notification-preferences",
    "user-agency-overrides": "user-agency-overrides",
    "agency-settings-core": "agency-settings",
    "citation-and-report-settings": "citation-report-settings",
    "integrations-settings": "integrations-overview",
    "rapidsos-management": "rapidsos-management",
    "small-agency-admin": "small-agency-admin",
    "troubleshooting-and-audit-checks": "troubleshooting-audit",
}

MOBILE_LINK = {k: v for k, v in MOBILE_MAP.items()}


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3 :].lstrip("\n")
    return text


def title_from_h1(body: str, fallback: str) -> tuple[str, str]:
    m = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    title = m.group(1).strip() if m else fallback.replace("-", " ").title()
    sidebar = title if len(title) <= 28 else title[:25] + "…"
    return title, sidebar


def remove_h1(body: str) -> str:
    return re.sub(r"^#\s+.+\n?", "", body, count=1, flags=re.MULTILINE)


def convert_callouts(body: str) -> str:
    # Docusaurus-style admonitions
    body = re.sub(
        r":::tip\s+([^\n]+)\n\n([\s\S]*?):::\n",
        lambda m: f"<Tip>\n{m.group(2).strip()}\n</Tip>\n",
        body,
        flags=re.IGNORECASE,
    )
    body = re.sub(
        r":::note\s+([^\n]+)\n\n([\s\S]*?):::\n",
        lambda m: f"<Note>\n{m.group(2).strip()}\n</Note>\n",
        body,
        flags=re.IGNORECASE,
    )
    body = re.sub(
        r":::warning\s+([^\n]+)\n\n([\s\S]*?):::\n",
        lambda m: f"<Warning>\n{m.group(2).strip()}\n</Warning>\n",
        body,
        flags=re.IGNORECASE,
    )

    lines = body.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^>\s*\*\*Warning:\*\*\s*(.*)$", line)
        if m:
            out.append(f"<Warning>{m.group(1).strip()}</Warning>")
            i += 1
            continue
        m = re.match(r"^>\s*\*\*Tip:\*\*\s*(.*)$", line) or re.match(
            r"^>\s*\*\*Availability note:\*\*\s*(.*)$", line
        )
        if m:
            out.append(f"<Tip>{m.group(1).strip()}</Tip>")
            i += 1
            continue
        if line.startswith("> Screenshot placeholder:"):
            out.append(f"<Note>{line[2:].strip()}</Note>")
            i += 1
            continue
        if line.startswith("> **Warning:**"):
            out.append(f"<Warning>{line.replace('> **Warning:**', '').strip()}</Warning>")
            i += 1
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def fix_links(body: str) -> str:
    def repl_md(m: re.Match) -> str:
        label, path = m.group(1), m.group(2)
        path = path.split("#")[0]
        if path.startswith("../dispatch-cad/"):
            rel = path.replace("../dispatch-cad/", "").replace(".md", "")
            slug = DISPATCH_LINK.get(rel, rel.replace("/", "-"))
            return f"[{label}](/dispatch/{slug})"
        if path.startswith("../web-admin/"):
            rel = path.replace("../web-admin/", "").replace(".md", "")
            slug = WEB_LINK.get(rel, rel)
            return f"[{label}](/admin/{slug})"
        if path.startswith("../mobile-cad/"):
            rel = path.replace("../mobile-cad/", "").replace(".md", "")
            slug = MOBILE_LINK.get(rel, rel)
            return f"[{label}](/mobile/{slug})"
        if path.startswith("./"):
            rel = path.replace("./", "").replace(".md", "")
            return m.group(0)  # caller sets prefix
        return m.group(0)

    body = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl_md, body)
    return body


def fix_links_for_section(body: str, section: str) -> str:
    def repl(m: re.Match) -> str:
        label, path = m.group(1), m.group(2).split("#")[0]
        if path.startswith("./"):
            rel = path.replace("./", "").replace(".md", "")
            if section == "mobile":
                slug = MOBILE_LINK.get(rel, rel)
                return f"[{label}](/mobile/{slug})"
            if section == "admin":
                slug = WEB_LINK.get(rel, rel)
                return f"[{label}](/admin/{slug})"
            if section == "dispatch":
                slug = DISPATCH_LINK.get(rel, rel)
                return f"[{label}](/dispatch/{slug})"
        return fix_links(f"[{label}]({path})")

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, body)


def make_description(title: str, body: str) -> str:
    for line in body.split("\n"):
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith(">"):
            line = re.sub(r"[*_`]", "", line)
            if len(line) > 20:
                return line[:155] + ("…" if len(line) > 155 else "")
    return f"Guide to {title} in Cadmus."


def write_mdx(
    source: Path,
    target: Path,
    section: str,
    title_override: str | None = None,
    sidebar_override: str | None = None,
) -> None:
    raw = source.read_text(encoding="utf-8")
    body = strip_frontmatter(raw)
    title, sidebar = title_from_h1(body, source.stem)
    if title_override:
        title = title_override
    if sidebar_override:
        sidebar = sidebar_override
    body = remove_h1(body)
    body = convert_callouts(body)
    body = fix_links_for_section(body, section)
    desc = make_description(title, body)
    front = (
        f"---\ntitle: \"{title}\"\n"
        f"sidebarTitle: \"{sidebar}\"\n"
        f"description: \"{desc.replace(chr(34), chr(39))}\"\n---\n\n"
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(front + body.strip() + "\n", encoding="utf-8")
    print(f"  wrote {target.relative_to(CAD_DOCS)}")


def main() -> None:
    print("Mobile CAD")
    for stem, slug in MOBILE_MAP.items():
        src = MANUAL / "mobile-cad" / f"{stem}.md"
        write_mdx(src, CAD_DOCS / "mobile" / f"{slug}.mdx", "mobile")

    print("Dispatch backfill")
    for stem, slug in DISPATCH_TOP_MAP.items():
        if slug is None:
            continue
        src = MANUAL / "dispatch-cad" / f"{stem}.md"
        write_mdx(src, CAD_DOCS / "dispatch" / f"{slug}.mdx", "dispatch")

    print("Command line")
    for stem, slug in DISPATCH_CMD_MAP.items():
        src = MANUAL / "dispatch-cad" / "command-line" / f"{stem}.md"
        write_mdx(src, CAD_DOCS / "dispatch" / f"{slug}.mdx", "dispatch")

    print("Web Admin backfill")
    for stem, slug in WEB_ADMIN_MAP.items():
        src = MANUAL / "web-admin" / f"{stem}.md"
        write_mdx(src, CAD_DOCS / "admin" / f"{slug}.mdx", "admin")

    print("Done.")


if __name__ == "__main__":
    main()
