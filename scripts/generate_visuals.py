#!/usr/bin/env python3
"""Generate the self-contained SVG artwork used by the profile README."""

from __future__ import annotations

import base64
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def write(name: str, content: str) -> None:
    (ASSETS / name).write_text(content.strip() + "\n", encoding="utf-8")


def hero(theme: str) -> str:
    palettes = {
        "dark": {
            "bg": "#0B0E11",
            "panel": "#12171D",
            "panel2": "#171E25",
            "border": "#303944",
            "text": "#FFF4E7",
            "muted": "#A6B0BB",
            "grid": "#202832",
            "orange": "#F39A45",
            "green": "#48D597",
            "amber": "#F4C15D",
        },
        "light": {
            "bg": "#F3EDE4",
            "panel": "#FFF9F0",
            "panel2": "#F8EFE3",
            "border": "#D6C8B7",
            "text": "#29241F",
            "muted": "#6D645B",
            "grid": "#E5D9CA",
            "orange": "#C96720",
            "green": "#187B50",
            "amber": "#9A620A",
        },
    }
    p = palettes[theme]
    cat = base64.b64encode((ASSETS / "chai-cat.jpg").read_bytes()).decode("ascii")

    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="500" viewBox="0 0 1200 500" role="img" aria-labelledby="title desc">
  <title id="title">Devashish Bhat's ChaiOps console</title>
  <desc id="desc">A playful reliability dashboard with a calm orange cat drinking chai, subtle system signals, and three measured engineering outcomes.</desc>
  <defs>
    <pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M 28 0 L 0 0 0 28" fill="none" stroke="{p['grid']}" stroke-width="1"/>
    </pattern>
    <clipPath id="catClip">
      <rect x="906" y="86" width="236" height="294" rx="24"/>
    </clipPath>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="12" stdDeviation="18" flood-color="#000000" flood-opacity=".18"/>
    </filter>
    <style>
      .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
      .sans {{ font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
      .pulse {{ transform-origin: 1084px 42px; animation: pulse 2.6s ease-out infinite; }}
      .steam {{ stroke-dasharray: 18 16; animation: steam 3.8s ease-in-out infinite; }}
      .packet {{ animation: packetFade 4.8s ease-in-out infinite; }}
      @keyframes pulse {{ 0%, 60%, 100% {{ transform: scale(1); opacity: .95; }} 75% {{ transform: scale(1.8); opacity: .18; }} }}
      @keyframes steam {{ 0%, 100% {{ stroke-dashoffset: 0; opacity: .18; }} 50% {{ stroke-dashoffset: -28; opacity: .85; }} }}
      @keyframes packetFade {{ 0%, 100% {{ opacity: 0; }} 12%, 75% {{ opacity: 1; }} }}
      @media (prefers-reduced-motion: reduce) {{
        .pulse, .steam, .packet {{ animation: none !important; }}
        .packet {{ display: none; }}
      }}
    </style>
  </defs>

  <rect width="1200" height="500" rx="30" fill="{p['bg']}"/>
  <rect width="1200" height="500" rx="30" fill="url(#grid)" opacity=".72"/>
  <rect x="24" y="24" width="1152" height="452" rx="22" fill="{p['panel']}" stroke="{p['border']}" filter="url(#shadow)"/>

  <circle cx="52" cy="49" r="5" fill="#FF6B68"/>
  <circle cx="70" cy="49" r="5" fill="{p['amber']}"/>
  <circle cx="88" cy="49" r="5" fill="{p['green']}"/>
  <text x="112" y="54" class="mono" font-size="14" font-weight="700" letter-spacing="2" fill="{p['muted']}">CHAI_OPS / CONTROL ROOM</text>
  <circle class="pulse" cx="1084" cy="42" r="10" fill="{p['green']}" opacity=".24"/>
  <circle cx="1084" cy="42" r="5" fill="{p['green']}"/>
  <text x="1100" y="47" class="mono" font-size="12" font-weight="700" fill="{p['green']}">OBSERVABLE</text>

  <text x="62" y="124" class="mono" font-size="15" font-weight="700" letter-spacing="3" fill="{p['orange']}">DEVASHISH BHAT</text>
  <text x="62" y="180" class="sans" font-size="42" font-weight="800" fill="{p['text']}">Backend systems for when</text>
  <text x="62" y="230" class="sans" font-size="42" font-weight="800" fill="{p['text']}">the happy path leaves the building.</text>
  <text x="62" y="274" class="mono" font-size="15" fill="{p['muted']}">distributed systems  /  applied AI  /  measurable reliability</text>

  <path d="M 66 316 C 215 294, 375 335, 518 313 S 740 294, 858 315" fill="none" stroke="{p['border']}" stroke-width="2"/>
  <circle class="packet" r="5" fill="{p['orange']}">
    <animateMotion dur="4.8s" repeatCount="indefinite" path="M 66 316 C 215 294, 375 335, 518 313 S 740 294, 858 315"/>
  </circle>

  <g transform="translate(62 338)">
    <rect width="246" height="96" rx="14" fill="{p['panel2']}" stroke="{p['border']}"/>
    <text x="18" y="27" class="mono" font-size="11" font-weight="700" letter-spacing="1.4" fill="{p['muted']}">SEARCH RELEVANCE</text>
    <text x="18" y="64" class="mono" font-size="27" font-weight="800" fill="{p['text']}">0.61 → 0.84</text>
    <text x="18" y="84" class="mono" font-size="10" fill="{p['green']}">TOP-5 / LABELED SET</text>
  </g>
  <g transform="translate(323 338)">
    <rect width="246" height="96" rx="14" fill="{p['panel2']}" stroke="{p['border']}"/>
    <text x="18" y="27" class="mono" font-size="11" font-weight="700" letter-spacing="1.4" fill="{p['muted']}">CITATION VALIDITY</text>
    <text x="18" y="64" class="mono" font-size="27" font-weight="800" fill="{p['text']}">100%</text>
    <text x="18" y="84" class="mono" font-size="10" fill="{p['green']}">CODE-VERIFIED / LEDGER</text>
  </g>
  <g transform="translate(584 338)">
    <rect width="274" height="96" rx="14" fill="{p['panel2']}" stroke="{p['border']}"/>
    <text x="18" y="27" class="mono" font-size="11" font-weight="700" letter-spacing="1.4" fill="{p['muted']}">BATCH RECOVERY</text>
    <text x="18" y="64" class="mono" font-size="27" font-weight="800" fill="{p['text']}">50K / 20 min</text>
    <text x="18" y="84" class="mono" font-size="10" fill="{p['green']}">RESTART-SAFE PAYMENTS</text>
  </g>

  <rect x="898" y="78" width="252" height="310" rx="29" fill="{p['orange']}" opacity=".28"/>
  <image href="data:image/jpeg;base64,{cat}" x="906" y="86" width="236" height="294" preserveAspectRatio="xMidYMid slice" clip-path="url(#catClip)"/>
  <rect x="906" y="86" width="236" height="294" rx="24" fill="none" stroke="{p['orange']}" stroke-width="2"/>
  <path class="steam" d="M 1015 295 C 994 270, 1036 255, 1014 226" fill="none" stroke="{p['text']}" stroke-width="3" stroke-linecap="round" opacity=".7"/>
  <path class="steam" d="M 1040 300 C 1063 273, 1029 255, 1050 236" fill="none" stroke="{p['text']}" stroke-width="2" stroke-linecap="round" opacity=".45" style="animation-delay:-1.4s"/>
  <rect x="932" y="354" width="184" height="48" rx="12" fill="{p['panel']}" stroke="{p['border']}"/>
  <circle cx="952" cy="378" r="5" fill="{p['green']}"/>
  <text x="966" y="382" class="mono" font-size="12" font-weight="700" fill="{p['text']}">CALM MODE: ACTIVE</text>
</svg>
"""


def project_card(
    number: str,
    project: str,
    eyebrow: str,
    signal: tuple[str, str],
    system: tuple[str, str],
    result: tuple[str, str],
    accent: str,
) -> str:
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="224" viewBox="0 0 1200 224" role="img" aria-labelledby="title desc">
  <title id="title">{project} project incident card</title>
  <desc id="desc">Signal: {signal[0]} {signal[1]}. System: {system[0]} {system[1]}. Result: {result[0]} {result[1]}.</desc>
  <defs>
    <pattern id="dots" width="18" height="18" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#2B333D"/>
    </pattern>
    <style>
      .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
      .sans {{ font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
    </style>
  </defs>
  <rect width="1200" height="224" rx="22" fill="#10151A"/>
  <rect width="1200" height="224" rx="22" fill="url(#dots)"/>
  <rect x="1" y="1" width="1198" height="222" rx="21" fill="none" stroke="#303945" stroke-width="2"/>
  <rect width="184" height="224" rx="22" fill="{accent}"/>
  <path d="M 162 0 H 184 V 224 H 162 C 177 188, 177 36, 162 0Z" fill="#10151A" opacity=".16"/>

  <text x="28" y="38" class="mono" font-size="11" font-weight="700" letter-spacing="2" fill="#17120F">INCIDENT {number}</text>
  <text x="28" y="92" class="sans" font-size="27" font-weight="900" fill="#17120F">{project}</text>
  <text x="28" y="120" class="mono" font-size="11" font-weight="700" fill="#3E2B20">{eyebrow}</text>
  <rect x="28" y="162" width="126" height="34" rx="9" fill="#17120F"/>
  <text x="45" y="184" class="mono" font-size="11" font-weight="700" fill="#FFF4E7">OPEN REPO ↗</text>

  <line x1="214" y1="42" x2="214" y2="184" stroke="#303945"/>
  <line x1="540" y1="42" x2="540" y2="184" stroke="#303945"/>
  <line x1="866" y1="42" x2="866" y2="184" stroke="#303945"/>

  <text x="242" y="58" class="mono" font-size="12" font-weight="700" letter-spacing="2" fill="{accent}">SIGNAL</text>
  <text x="242" y="98" class="sans" font-size="18" font-weight="700" fill="#FFF4E7">{signal[0]}</text>
  <text x="242" y="126" class="sans" font-size="18" font-weight="700" fill="#FFF4E7">{signal[1]}</text>

  <text x="568" y="58" class="mono" font-size="12" font-weight="700" letter-spacing="2" fill="{accent}">SYSTEM</text>
  <text x="568" y="98" class="sans" font-size="17" font-weight="700" fill="#FFF4E7">{system[0]}</text>
  <text x="568" y="126" class="sans" font-size="17" font-weight="700" fill="#FFF4E7">{system[1]}</text>

  <text x="894" y="58" class="mono" font-size="12" font-weight="700" letter-spacing="2" fill="{accent}">RESULT</text>
  <text x="894" y="98" class="sans" font-size="17" font-weight="800" fill="#FFF4E7">{result[0]}</text>
  <text x="894" y="126" class="sans" font-size="17" font-weight="800" fill="#FFF4E7">{result[1]}</text>
  <circle cx="894" cy="166" r="5" fill="#48D597"/>
  <text x="908" y="170" class="mono" font-size="11" font-weight="700" fill="#A6B0BB">SYSTEM DOCUMENTED</text>
</svg>
"""


def hero_mobile(theme: str) -> str:
    palettes = {
        "dark": {
            "bg": "#0B0E11",
            "panel": "#12171D",
            "panel2": "#171E25",
            "border": "#303944",
            "text": "#FFF4E7",
            "muted": "#A6B0BB",
            "grid": "#202832",
            "orange": "#F39A45",
            "green": "#48D597",
        },
        "light": {
            "bg": "#F3EDE4",
            "panel": "#FFF9F0",
            "panel2": "#F8EFE3",
            "border": "#D6C8B7",
            "text": "#29241F",
            "muted": "#6D645B",
            "grid": "#E5D9CA",
            "orange": "#C96720",
            "green": "#187B50",
        },
    }
    p = palettes[theme]
    cat = base64.b64encode((ASSETS / "chai-cat.jpg").read_bytes()).decode("ascii")
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="720" height="650" viewBox="0 0 720 650" role="img" aria-labelledby="title desc">
  <title id="title">Devashish Bhat's mobile ChaiOps console</title>
  <desc id="desc">A compact reliability dashboard with a calm orange cat drinking chai and three measured engineering outcomes.</desc>
  <defs>
    <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="{p['grid']}" stroke-width="1"/>
    </pattern>
    <clipPath id="catClip"><rect x="478" y="308" width="180" height="230" rx="22"/></clipPath>
    <style>
      .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
      .sans {{ font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
      .pulse {{ transform-origin: 611px 47px; animation: pulse 2.6s ease-out infinite; }}
      .steam {{ stroke-dasharray: 18 16; animation: steam 3.8s ease-in-out infinite; }}
      @keyframes pulse {{ 0%, 60%, 100% {{ transform: scale(1); opacity: .95; }} 75% {{ transform: scale(1.8); opacity: .18; }} }}
      @keyframes steam {{ 0%, 100% {{ stroke-dashoffset: 0; opacity: .18; }} 50% {{ stroke-dashoffset: -28; opacity: .85; }} }}
      @media (prefers-reduced-motion: reduce) {{ .pulse, .steam {{ animation: none !important; }} }}
    </style>
  </defs>
  <rect width="720" height="650" rx="28" fill="{p['bg']}"/>
  <rect width="720" height="650" rx="28" fill="url(#grid)" opacity=".72"/>
  <rect x="20" y="20" width="680" height="610" rx="22" fill="{p['panel']}" stroke="{p['border']}"/>

  <circle cx="48" cy="48" r="5" fill="#FF6B68"/>
  <circle cx="66" cy="48" r="5" fill="#F4C15D"/>
  <circle cx="84" cy="48" r="5" fill="{p['green']}"/>
  <text x="108" y="53" class="mono" font-size="14" font-weight="700" letter-spacing="2" fill="{p['muted']}">CHAI_OPS</text>
  <circle class="pulse" cx="611" cy="47" r="9" fill="{p['green']}" opacity=".24"/>
  <circle cx="611" cy="47" r="4" fill="{p['green']}"/>
  <text x="625" y="52" class="mono" font-size="11" font-weight="700" fill="{p['green']}">LIVE</text>

  <text x="48" y="105" class="mono" font-size="15" font-weight="700" letter-spacing="3" fill="{p['orange']}">DEVASHISH BHAT</text>
  <text x="48" y="157" class="sans" font-size="40" font-weight="800" fill="{p['text']}">Backend systems</text>
  <text x="48" y="204" class="sans" font-size="40" font-weight="800" fill="{p['text']}">for when the happy path</text>
  <text x="48" y="251" class="sans" font-size="40" font-weight="800" fill="{p['text']}">leaves the building.</text>
  <text x="48" y="282" class="mono" font-size="13" fill="{p['muted']}">distributed systems / applied AI / reliability</text>

  <g transform="translate(48 308)">
    <rect width="400" height="82" rx="13" fill="{p['panel2']}" stroke="{p['border']}"/>
    <text x="16" y="24" class="mono" font-size="11" font-weight="700" letter-spacing="1.2" fill="{p['muted']}">SEARCH RELEVANCE</text>
    <text x="16" y="58" class="mono" font-size="24" font-weight="800" fill="{p['text']}">0.61 → 0.84</text>
    <text x="218" y="57" class="mono" font-size="10" fill="{p['green']}">TOP-5 / LABELED</text>
  </g>
  <g transform="translate(48 402)">
    <rect width="400" height="82" rx="13" fill="{p['panel2']}" stroke="{p['border']}"/>
    <text x="16" y="24" class="mono" font-size="11" font-weight="700" letter-spacing="1.2" fill="{p['muted']}">CITATION VALIDITY</text>
    <text x="16" y="58" class="mono" font-size="24" font-weight="800" fill="{p['text']}">100%</text>
    <text x="124" y="57" class="mono" font-size="10" fill="{p['green']}">CODE-VERIFIED / LEDGER</text>
  </g>
  <g transform="translate(48 496)">
    <rect width="400" height="82" rx="13" fill="{p['panel2']}" stroke="{p['border']}"/>
    <text x="16" y="24" class="mono" font-size="11" font-weight="700" letter-spacing="1.2" fill="{p['muted']}">BATCH RECOVERY</text>
    <text x="16" y="58" class="mono" font-size="24" font-weight="800" fill="{p['text']}">50K / 20 min</text>
    <text x="232" y="57" class="mono" font-size="10" fill="{p['green']}">RESTART-SAFE</text>
  </g>

  <rect x="470" y="300" width="196" height="246" rx="27" fill="{p['orange']}" opacity=".28"/>
  <image href="data:image/jpeg;base64,{cat}" x="478" y="308" width="180" height="230" preserveAspectRatio="xMidYMid slice" clip-path="url(#catClip)"/>
  <rect x="478" y="308" width="180" height="230" rx="22" fill="none" stroke="{p['orange']}" stroke-width="2"/>
  <path class="steam" d="M 558 475 C 540 454, 573 441, 556 417" fill="none" stroke="{p['text']}" stroke-width="3" stroke-linecap="round" opacity=".65"/>
  <rect x="493" y="520" width="150" height="42" rx="11" fill="{p['panel']}" stroke="{p['border']}"/>
  <circle cx="510" cy="541" r="5" fill="{p['green']}"/>
  <text x="523" y="545" class="mono" font-size="11" font-weight="700" fill="{p['text']}">CALM: ACTIVE</text>
</svg>
"""


def project_card_mobile(
    number: str,
    project: str,
    eyebrow: str,
    signal: tuple[str, str],
    system: tuple[str, str],
    result: tuple[str, str],
    accent: str,
) -> str:
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="720" height="520" viewBox="0 0 720 520" role="img" aria-labelledby="title desc">
  <title id="title">{project} mobile project incident card</title>
  <desc id="desc">Signal: {signal[0]} {signal[1]}. System: {system[0]} {system[1]}. Result: {result[0]} {result[1]}.</desc>
  <defs>
    <pattern id="dots" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#2B333D"/></pattern>
    <style>
      .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
      .sans {{ font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
    </style>
  </defs>
  <rect width="720" height="520" rx="22" fill="#10151A"/>
  <rect width="720" height="520" rx="22" fill="url(#dots)"/>
  <rect x="1" y="1" width="718" height="518" rx="21" fill="none" stroke="#303945" stroke-width="2"/>
  <rect width="720" height="124" rx="22" fill="{accent}"/>
  <rect y="100" width="720" height="24" fill="{accent}"/>
  <text x="28" y="36" class="mono" font-size="12" font-weight="700" letter-spacing="2" fill="#17120F">INCIDENT {number} / {eyebrow}</text>
  <text x="28" y="88" class="sans" font-size="32" font-weight="900" fill="#17120F">{project}</text>
  <rect x="536" y="42" width="152" height="48" rx="11" fill="#17120F"/>
  <text x="560" y="72" class="mono" font-size="13" font-weight="700" fill="#FFF4E7">OPEN REPO ↗</text>

  <text x="32" y="166" class="mono" font-size="16" font-weight="700" letter-spacing="2" fill="{accent}">SIGNAL</text>
  <text x="32" y="204" class="sans" font-size="27" font-weight="700" fill="#FFF4E7">{signal[0]} {signal[1]}</text>
  <line x1="32" y1="234" x2="688" y2="234" stroke="#303945"/>

  <text x="32" y="278" class="mono" font-size="16" font-weight="700" letter-spacing="2" fill="{accent}">SYSTEM</text>
  <text x="32" y="316" class="sans" font-size="27" font-weight="700" fill="#FFF4E7">{system[0]}</text>
  <text x="32" y="350" class="sans" font-size="27" font-weight="700" fill="#FFF4E7">{system[1]}</text>
  <line x1="32" y1="378" x2="688" y2="378" stroke="#303945"/>

  <text x="32" y="422" class="mono" font-size="16" font-weight="700" letter-spacing="2" fill="{accent}">RESULT</text>
  <text x="32" y="460" class="sans" font-size="27" font-weight="800" fill="#FFF4E7">{result[0]} · {result[1]}</text>
  <circle cx="32" cy="494" r="5" fill="#48D597"/>
  <text x="47" y="499" class="mono" font-size="12" font-weight="700" fill="#A6B0BB">SYSTEM DOCUMENTED</text>
</svg>
"""


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    write("chaiops-hero-dark.svg", hero("dark"))
    write("chaiops-hero-light.svg", hero("light"))
    write("chaiops-hero-mobile-dark.svg", hero_mobile("dark"))
    write("chaiops-hero-mobile-light.svg", hero_mobile("light"))
    write(
        "project-ledger.svg",
        project_card(
            "01",
            "LEDGER",
            "TRUSTWORTHY AI",
            ("Answers sounded right.", "Evidence was optional."),
            ("LangGraph + hybrid search", "+ code-verified quotes"),
            ("100% valid citations", "recall@5  0.70 → 0.91"),
            "#F39A45",
        ),
    )
    write(
        "project-jirassic.svg",
        project_card(
            "02",
            "JIRASSIC",
            "MEETINGS → WORK",
            ("Standups ended.", "Action items evaporated."),
            ("Whisper → Gemini", "→ story-pointed Jira tasks"),
            ("2nd Prize", "Hack@Davidson 2025"),
            "#E7B557",
        ),
    )
    write(
        "project-wmaps.svg",
        project_card(
            "03",
            "WMAPS",
            "ROUTE EXPLORER",
            ("Fastest route.", "Forgettable drive."),
            ("Route-aware discovery", "+ AI stories + voice"),
            ("5 explore modes", "hands-free stories"),
            "#72C7A1",
        ),
    )
    write(
        "project-ledger-mobile.svg",
        project_card_mobile(
            "01",
            "LEDGER",
            "TRUSTWORTHY AI",
            ("Answers sounded right.", "Evidence was optional."),
            ("LangGraph + hybrid search", "+ code-verified quotes"),
            ("100% valid citations", "recall@5  0.70 → 0.91"),
            "#F39A45",
        ),
    )
    write(
        "project-jirassic-mobile.svg",
        project_card_mobile(
            "02",
            "JIRASSIC",
            "MEETINGS → WORK",
            ("Standups ended.", "Action items evaporated."),
            ("Whisper → Gemini", "→ story-pointed Jira tasks"),
            ("2nd Prize", "Hack@Davidson 2025"),
            "#E7B557",
        ),
    )
    write(
        "project-wmaps-mobile.svg",
        project_card_mobile(
            "03",
            "WMAPS",
            "ROUTE EXPLORER",
            ("Fastest route.", "Forgettable drive."),
            ("Route-aware discovery", "+ AI stories + voice"),
            ("5 explore modes", "hands-free stories"),
            "#72C7A1",
        ),
    )


if __name__ == "__main__":
    main()
