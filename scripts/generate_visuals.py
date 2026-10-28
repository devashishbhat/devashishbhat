#!/usr/bin/env python3
"""Generate the bright, responsive artwork used by the profile README."""

from __future__ import annotations

import base64
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def write(name: str, content: str) -> None:
    (ASSETS / name).write_text(content.strip() + "\n", encoding="utf-8")


def embedded_cat() -> str:
    return base64.b64encode((ASSETS / "chai-cat.jpg").read_bytes()).decode("ascii")


def hero(theme: str, mobile: bool = False) -> str:
    palettes = {
        "light": {
            "bg1": "#FFF7FA",
            "bg2": "#EEF7FF",
            "text": "#17162B",
            "muted": "#55536D",
            "panel": "#FFFFFF",
            "line": "#D9D8EA",
            "blue": "#287BFF",
            "coral": "#FF5C7A",
            "violet": "#8B5CF6",
            "mint": "#22CDB2",
        },
        "dark": {
            "bg1": "#11142A",
            "bg2": "#181E3D",
            "text": "#FFF8FC",
            "muted": "#C4C7DF",
            "panel": "#20264A",
            "line": "#3B426A",
            "blue": "#5B9CFF",
            "coral": "#FF6F8B",
            "violet": "#A882FF",
            "mint": "#42E2C5",
        },
    }
    p = palettes[theme]
    cat = embedded_cat()

    if mobile:
        return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="720" height="920" viewBox="0 0 720 920" role="img" aria-labelledby="title desc">
  <title id="title">Devashish Bhat's portfolio introduction</title>
  <desc id="desc">A bright introduction to Devashish Bhat, a recent UNC Charlotte computer science graduate who builds backend systems and AI products.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="{p['bg1']}"/>
      <stop offset="1" stop-color="{p['bg2']}"/>
    </linearGradient>
    <clipPath id="catClip"><rect x="160" y="474" width="400" height="332" rx="66"/></clipPath>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="150%">
      <feDropShadow dx="0" dy="16" stdDeviation="20" flood-color="#17162B" flood-opacity=".18"/>
    </filter>
    <style>
      .sans {{ font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
      .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
      .float-a {{ animation: floatA 5s ease-in-out infinite; transform-origin: center; }}
      .float-b {{ animation: floatB 6s ease-in-out infinite; transform-origin: center; }}
      .steam {{ stroke-dasharray: 22 18; animation: steam 4s ease-in-out infinite; }}
      @keyframes floatA {{ 0%,100% {{ transform: translateY(0) rotate(0); }} 50% {{ transform: translateY(-10px) rotate(3deg); }} }}
      @keyframes floatB {{ 0%,100% {{ transform: translateY(0); }} 50% {{ transform: translateY(9px); }} }}
      @keyframes steam {{ 0%,100% {{ stroke-dashoffset: 0; opacity: .2; }} 50% {{ stroke-dashoffset: -34; opacity: .85; }} }}
      @media (prefers-reduced-motion: reduce) {{ .float-a,.float-b,.steam {{ animation: none !important; }} }}
    </style>
  </defs>
  <rect width="720" height="920" rx="34" fill="url(#bg)"/>
  <circle class="float-a" cx="650" cy="95" r="46" fill="{p['coral']}" opacity=".22"/>
  <path class="float-b" d="M40 356 C120 314, 172 398, 252 350 S386 312, 452 352" fill="none" stroke="{p['mint']}" stroke-width="10" stroke-linecap="round" opacity=".65"/>
  <rect x="46" y="46" width="178" height="42" rx="21" fill="{p['blue']}"/>
  <text x="68" y="73" class="mono" font-size="15" font-weight="800" letter-spacing="2" fill="#FFFFFF">HELLO, I'M</text>

  <text x="46" y="166" class="sans" font-size="68" font-weight="900" fill="{p['text']}">Devashish</text>
  <text x="46" y="238" class="sans" font-size="68" font-weight="900" fill="{p['text']}">Bhat.</text>
  <text x="46" y="293" class="sans" font-size="24" font-weight="750" fill="{p['violet']}">Recent M.S. Computer Science graduate</text>
  <text x="46" y="327" class="sans" font-size="23" font-weight="700" fill="{p['text']}">UNC Charlotte · 4.0 GPA</text>
  <text x="46" y="397" class="sans" font-size="25" font-weight="650" fill="{p['muted']}">I build useful backend systems and AI</text>
  <text x="46" y="430" class="sans" font-size="25" font-weight="650" fill="{p['muted']}">products, with curiosity and good chai.</text>

  <rect x="144" y="458" width="432" height="364" rx="80" fill="{p['violet']}" opacity=".22" transform="rotate(-3 360 640)"/>
  <image href="data:image/jpeg;base64,{cat}" x="160" y="474" width="400" height="332" preserveAspectRatio="xMidYMid slice" clip-path="url(#catClip)" filter="url(#shadow)"/>
  <rect x="160" y="474" width="400" height="332" rx="66" fill="none" stroke="{p['coral']}" stroke-width="6"/>
  <path class="steam" d="M 350 710 C 316 671, 376 644, 344 606" fill="none" stroke="#FFF8FC" stroke-width="6" stroke-linecap="round"/>

  <g class="float-a">
    <rect x="60" y="575" width="138" height="48" rx="24" fill="{p['blue']}"/>
    <text x="88" y="606" class="mono" font-size="15" font-weight="800" fill="#FFFFFF">BACKEND</text>
  </g>
  <g class="float-b">
    <rect x="508" y="545" width="154" height="48" rx="24" fill="{p['coral']}"/>
    <text x="535" y="576" class="mono" font-size="15" font-weight="800" fill="#FFFFFF">APPLIED AI</text>
  </g>
  <g class="float-a">
    <rect x="466" y="765" width="196" height="48" rx="24" fill="{p['mint']}"/>
    <text x="489" y="796" class="mono" font-size="14" font-weight="800" fill="#102B2A">DISTRIBUTED</text>
  </g>
  <text x="360" y="872" text-anchor="middle" class="mono" font-size="14" font-weight="700" letter-spacing="2" fill="{p['muted']}">BUILD · LEARN · MAKE IT USEFUL</text>
</svg>
"""

    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="620" viewBox="0 0 1200 620" role="img" aria-labelledby="title desc">
  <title id="title">Devashish Bhat's portfolio introduction</title>
  <desc id="desc">A bright introduction to Devashish Bhat, a recent UNC Charlotte computer science graduate who builds backend systems and AI products.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="{p['bg1']}"/>
      <stop offset="1" stop-color="{p['bg2']}"/>
    </linearGradient>
    <clipPath id="catClip"><rect x="835" y="92" width="290" height="410" rx="68"/></clipPath>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="150%">
      <feDropShadow dx="0" dy="18" stdDeviation="24" flood-color="#17162B" flood-opacity=".2"/>
    </filter>
    <style>
      .sans {{ font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
      .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
      .float-a {{ animation: floatA 5s ease-in-out infinite; transform-origin: center; }}
      .float-b {{ animation: floatB 6s ease-in-out infinite; transform-origin: center; }}
      .steam {{ stroke-dasharray: 22 18; animation: steam 4s ease-in-out infinite; }}
      @keyframes floatA {{ 0%,100% {{ transform: translateY(0) rotate(0); }} 50% {{ transform: translateY(-10px) rotate(3deg); }} }}
      @keyframes floatB {{ 0%,100% {{ transform: translateY(0); }} 50% {{ transform: translateY(9px); }} }}
      @keyframes steam {{ 0%,100% {{ stroke-dashoffset: 0; opacity: .2; }} 50% {{ stroke-dashoffset: -34; opacity: .85; }} }}
      @media (prefers-reduced-motion: reduce) {{ .float-a,.float-b,.steam {{ animation: none !important; }} }}
    </style>
  </defs>
  <rect width="1200" height="620" rx="34" fill="url(#bg)"/>
  <circle class="float-a" cx="1120" cy="78" r="54" fill="{p['coral']}" opacity=".25"/>
  <circle class="float-b" cx="760" cy="548" r="34" fill="{p['blue']}" opacity=".22"/>
  <path d="M58 532 C170 482, 246 570, 356 520 S548 476, 656 528" fill="none" stroke="{p['mint']}" stroke-width="12" stroke-linecap="round" opacity=".72"/>
  <rect x="64" y="58" width="178" height="42" rx="21" fill="{p['blue']}"/>
  <text x="86" y="85" class="mono" font-size="15" font-weight="800" letter-spacing="2" fill="#FFFFFF">HELLO, I'M</text>

  <text x="64" y="184" class="sans" font-size="72" font-weight="900" fill="{p['text']}">Devashish Bhat.</text>
  <text x="64" y="239" class="sans" font-size="25" font-weight="750" fill="{p['violet']}">Recent M.S. Computer Science graduate</text>
  <text x="64" y="275" class="sans" font-size="24" font-weight="700" fill="{p['text']}">UNC Charlotte · 4.0 GPA</text>
  <text x="64" y="352" class="sans" font-size="29" font-weight="650" fill="{p['muted']}">I build useful backend systems and AI products</text>
  <text x="64" y="393" class="sans" font-size="29" font-weight="650" fill="{p['muted']}">with curiosity, careful engineering, and good chai.</text>

  <g class="float-a">
    <rect x="64" y="445" width="150" height="50" rx="25" fill="{p['blue']}"/>
    <text x="93" y="477" class="mono" font-size="15" font-weight="800" fill="#FFFFFF">BACKEND</text>
  </g>
  <g class="float-b">
    <rect x="228" y="445" width="164" height="50" rx="25" fill="{p['coral']}"/>
    <text x="257" y="477" class="mono" font-size="15" font-weight="800" fill="#FFFFFF">APPLIED AI</text>
  </g>
  <g class="float-a">
    <rect x="406" y="445" width="214" height="50" rx="25" fill="{p['mint']}"/>
    <text x="431" y="477" class="mono" font-size="14" font-weight="800" fill="#102B2A">DISTRIBUTED SYSTEMS</text>
  </g>

  <rect x="815" y="72" width="330" height="450" rx="86" fill="{p['violet']}" opacity=".22" transform="rotate(4 980 297)"/>
  <image href="data:image/jpeg;base64,{cat}" x="835" y="92" width="290" height="410" preserveAspectRatio="xMidYMid slice" clip-path="url(#catClip)" filter="url(#shadow)"/>
  <rect x="835" y="92" width="290" height="410" rx="68" fill="none" stroke="{p['coral']}" stroke-width="6"/>
  <path class="steam" d="M 968 410 C 936 374, 990 346, 960 311" fill="none" stroke="#FFF8FC" stroke-width="6" stroke-linecap="round"/>
  <g class="float-b">
    <circle cx="803" cy="150" r="44" fill="{p['mint']}"/>
    <path d="M785 151 l12 12 24-28" fill="none" stroke="#102B2A" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <g class="float-a">
    <rect x="1018" y="474" width="140" height="48" rx="24" fill="{p['blue']}"/>
    <text x="1043" y="505" class="mono" font-size="14" font-weight="800" fill="#FFFFFF">SHIP IT</text>
  </g>
  <text x="64" y="581" class="mono" font-size="14" font-weight="700" letter-spacing="2" fill="{p['muted']}">BUILD · LEARN · MAKE IT USEFUL</text>
</svg>
"""


def project_art(kind: str, accent: str, accent2: str) -> str:
    if kind == "ledger":
        return f"""
  <g transform="translate(925 44)">
    <rect x="38" y="18" width="170" height="150" rx="24" fill="{accent2}" transform="rotate(8 123 93)"/>
    <rect x="10" y="8" width="170" height="150" rx="24" fill="#FFFFFF" stroke="#17162B" stroke-width="4" transform="rotate(-5 95 83)"/>
    <text x="45" y="83" class="sans" font-size="64" font-weight="900" fill="{accent}">“</text>
    <path d="M76 72 H150 M76 96 H142 M76 120 H126" stroke="#17162B" stroke-width="8" stroke-linecap="round"/>
  </g>"""
    if kind == "jirassic":
        return f"""
  <g transform="translate(930 38)">
    <rect x="0" y="0" width="224" height="174" rx="34" fill="{accent2}"/>
    <rect x="32" y="28" width="48" height="72" rx="24" fill="{accent}" stroke="#17162B" stroke-width="4"/>
    <path d="M22 82 C22 126, 92 126, 92 82 M57 121 V146 M34 146 H80" fill="none" stroke="#17162B" stroke-width="7" stroke-linecap="round"/>
    <rect x="118" y="36" width="20" height="20" rx="5" fill="#FFFFFF" stroke="#17162B" stroke-width="4"/>
    <path d="M122 45 l5 5 9-12" fill="none" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>
    <path d="M150 46 H198 M150 76 H198 M118 106 H198 M118 136 H180" stroke="#17162B" stroke-width="7" stroke-linecap="round"/>
  </g>"""
    return f"""
  <g transform="translate(925 34)">
    <rect x="0" y="0" width="230" height="184" rx="40" fill="{accent2}"/>
    <path d="M36 142 C54 76, 98 154, 128 84 S184 40, 200 72" fill="none" stroke="{accent}" stroke-width="12" stroke-linecap="round" stroke-dasharray="10 15"/>
    <circle cx="36" cy="142" r="16" fill="#FFFFFF" stroke="#17162B" stroke-width="5"/>
    <path d="M200 42 C177 42, 169 69, 200 105 C231 69, 223 42, 200 42Z" fill="#FFFFFF" stroke="#17162B" stroke-width="5"/>
    <circle cx="200" cy="66" r="8" fill="{accent}"/>
  </g>"""


def project_card(
    number: str,
    name: str,
    description: tuple[str, str],
    tags: str,
    accent: str,
    accent2: str,
    kind: str,
    mobile: bool = False,
) -> str:
    art = project_art(kind, accent, accent2)
    if mobile:
        art = art.replace('transform="translate(925 44)"', 'transform="translate(440 36) scale(.78)"')
        art = art.replace('transform="translate(930 38)"', 'transform="translate(440 32) scale(.78)"')
        art = art.replace('transform="translate(925 34)"', 'transform="translate(438 28) scale(.78)"')
        return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="720" height="470" viewBox="0 0 720 470" role="img" aria-labelledby="title desc">
  <title id="title">{name} project</title>
  <desc id="desc">{description[0]} {description[1]}</desc>
  <defs>
    <linearGradient id="card" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{accent2}"/><stop offset="1" stop-color="#FFFFFF"/></linearGradient>
    <style>
      .sans {{ font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
      .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
    </style>
  </defs>
  <rect width="720" height="470" rx="34" fill="url(#card)"/>
  <rect x="1.5" y="1.5" width="717" height="467" rx="32.5" fill="none" stroke="{accent}" stroke-width="3"/>
  <rect x="36" y="34" width="150" height="38" rx="19" fill="{accent}"/>
  <text x="58" y="59" class="mono" font-size="13" font-weight="800" letter-spacing="2" fill="#FFFFFF">PROJECT {number}</text>
  <text x="36" y="142" class="sans" font-size="52" font-weight="900" fill="#17162B">{name}</text>
{art}
  <text x="36" y="226" class="sans" font-size="27" font-weight="700" fill="#34324A">{description[0]}</text>
  <text x="36" y="262" class="sans" font-size="27" font-weight="700" fill="#34324A">{description[1]}</text>
  <rect x="36" y="310" width="648" height="58" rx="20" fill="#FFFFFF" opacity=".82"/>
  <text x="60" y="346" class="mono" font-size="16" font-weight="750" fill="#55536D">{tags}</text>
  <rect x="36" y="392" width="206" height="52" rx="26" fill="#17162B"/>
  <text x="66" y="425" class="sans" font-size="17" font-weight="800" fill="#FFFFFF">VIEW PROJECT  ↗</text>
</svg>
"""

    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-labelledby="title desc">
  <title id="title">{name} project</title>
  <desc id="desc">{description[0]} {description[1]}</desc>
  <defs>
    <linearGradient id="card" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{accent2}"/><stop offset="1" stop-color="#FFFFFF"/></linearGradient>
    <style>
      .sans {{ font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
      .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
    </style>
  </defs>
  <rect width="1200" height="300" rx="34" fill="url(#card)"/>
  <rect x="1.5" y="1.5" width="1197" height="297" rx="32.5" fill="none" stroke="{accent}" stroke-width="3"/>
  <rect x="46" y="38" width="150" height="38" rx="19" fill="{accent}"/>
  <text x="68" y="63" class="mono" font-size="13" font-weight="800" letter-spacing="2" fill="#FFFFFF">PROJECT {number}</text>
  <text x="46" y="130" class="sans" font-size="48" font-weight="900" fill="#17162B">{name}</text>
  <text x="46" y="181" class="sans" font-size="25" font-weight="700" fill="#34324A">{description[0]}</text>
  <text x="46" y="214" class="sans" font-size="25" font-weight="700" fill="#34324A">{description[1]}</text>
  <text x="48" y="263" class="mono" font-size="15" font-weight="750" fill="#55536D">{tags}</text>
{art}
  <rect x="946" y="228" width="208" height="48" rx="24" fill="#17162B"/>
  <text x="978" y="259" class="sans" font-size="16" font-weight="800" fill="#FFFFFF">VIEW PROJECT  ↗</text>
</svg>
"""


PROJECTS = [
    (
        "01",
        "Ledger",
        ("An AI research assistant for SEC filings that", "grounds every answer in exact source citations."),
        "PYTHON · LANGGRAPH · QDRANT · FASTAPI",
        "#287BFF",
        "#DDEBFF",
        "ledger",
    ),
    (
        "02",
        "Jirassic",
        ("Turns standup recordings into structured,", "story-pointed Jira tasks your team can use."),
        "TYPESCRIPT · NEXT.JS · WHISPER · GEMINI",
        "#FF4F7B",
        "#FFE1E9",
        "jirassic",
    ),
    (
        "03",
        "Wmaps",
        ("Finds hidden places along your route and tells", "their stories hands-free while you drive."),
        "JAVASCRIPT · GOOGLE MAPS · CLAUDE · VOICE",
        "#10BFA4",
        "#D8FAF3",
        "wmaps",
    ),
]


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    write("portfolio-hero-light.svg", hero("light"))
    write("portfolio-hero-dark.svg", hero("dark"))
    write("portfolio-hero-mobile-light.svg", hero("light", mobile=True))
    write("portfolio-hero-mobile-dark.svg", hero("dark", mobile=True))
    for number, name, description, tags, accent, accent2, kind in PROJECTS:
        slug = name.lower()
        write(
            f"project-{slug}.svg",
            project_card(number, name, description, tags, accent, accent2, kind),
        )
        write(
            f"project-{slug}-mobile.svg",
            project_card(
                number,
                name,
                description,
                tags,
                accent,
                accent2,
                kind,
                mobile=True,
            ),
        )


if __name__ == "__main__":
    main()
