#!/usr/bin/env python3
"""Normalize data/operators.csv into the directory page's table rows plus a
machine-readable assets/data/operators.json. Read-only against data/ --
never edits the source CSV. Run standalone (python scripts/export_data.py)
or imported by build.py.
"""
from __future__ import annotations

import csv
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT.parent / "data"
OUT_DIR = ROOT / "assets" / "data"

DASH = "—"


def read_operators() -> list[dict]:
    path = DATA_DIR / "operators.csv"
    with path.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return sorted(rows, key=lambda r: r["name"].lower())


def _esc(v) -> str:
    return html.escape(str(v)) if v not in (None, "") else DASH


def render_rows(operators: list[dict]) -> str:
    rows = []
    for o in operators:
        search_blob = html.escape(f"{o['name']} {o['hq_regions']}").lower()
        rows.append(
            "  <tr data-search=\"{search}\">"
            "<th scope=\"row\" id=\"{slug}\">{name}</th>"
            "<td>{hq}</td>"
            "<td>{fleet}</td>"
            "<td>{shows} <a href=\"{shows_src}\" target=\"_blank\" rel=\"noopener\">source</a></td>"
            "<td>{waiver}</td>"
            "<td><a href=\"{website}\" target=\"_blank\" rel=\"noopener\">website</a></td>"
            "</tr>".format(
                search=search_blob,
                slug=html.escape(o["slug"]),
                name=_esc(o["name"]),
                hq=_esc(o["hq_regions"]),
                fleet=_esc(o["fleet_scale_claim"]),
                shows=_esc(o["notable_shows"]),
                shows_src=html.escape(o["notable_shows_source"]),
                waiver=_esc(o["waiver_status"]),
                website=html.escape(o["website"]),
            )
        )
    return "\n".join(rows)


def build_substitutions() -> dict:
    operators = read_operators()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "operators.json").write_text(
        json.dumps(operators, indent=1), encoding="utf-8")
    return {
        "[[ROWS]]": render_rows(operators),
        "[[TOTAL]]": str(len(operators)),
    }


def main() -> None:
    subs = build_substitutions()
    print(f"exported {subs['[[TOTAL]]']} operators -> {OUT_DIR / 'operators.json'}")


if __name__ == "__main__":
    main()
