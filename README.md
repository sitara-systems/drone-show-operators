# The Fleet Operator Directory

*A neutral, alphabetical directory of outdoor drone light show operators
meeting published inclusion criteria — no ranking, every claim attributed
to the operator's own site or a named public source.*

## What this is

Producers and venues booking an outdoor drone light show need a starting
list of who operates a fleet — not a ranked "best of," a factual directory
of operators meeting a published bar for inclusion. Published by
[Sitara Skies](https://skies.sitara.systems/), an aerial show design
studio, as one of the R-track records alongside The Drone Show Cost
Record, The Show-File Compatibility Matrix, and The Indoor Aerial
Permitting Record.

See `docs/methodology.md` for the full inclusion criteria and correction
process.

## Data

| File | Rows | Source |
|---|---|---|
| `data/operators.csv` | 15 | Each operator's own site + independent public coverage (news, FAA waiver records, one federal court filing) |

Columns: `slug, name, hq_regions, fleet_scale_claim, fleet_scale_short,
notable_shows, notable_shows_source, website, waiver_status,
waiver_short`. The `_short` columns are compact display strings for the
browse table; the full attributed text lives in the long-form columns
and surfaces as a hover tooltip on the operator's name.

## Known caveats

- Fleet-scale and show-count figures are as claimed by the operator or a
  named source — not independently audited by this directory.
- FAA waiver status is reported in several states: confirmed (a docket
  number or documented incident record was found), expired/lapsed
  (a real waiver found but its term has passed), claimed-not-verified
  (the operator asserts compliance without a checkable number), not
  publicly stated, or not applicable (non-US operator, no FAA
  jurisdiction). Absence of a public claim is not evidence of
  non-compliance.
- **Verge Aero** is included despite primarily selling a hardware+
  software platform to other operators — its own site documents it
  directly flying client shows (Rice University, historically the
  Philadelphia Eagles) under its own name. The dual role is noted in its
  entry, not hidden. **UVify** remains excluded — no evidence found of
  it flying shows under its own brand, only renting fleet capacity to
  others.
- Companies searched but not verifiable via a live public source were
  dropped rather than padded into the list.

## License

Compilation released under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution:
"The Fleet Operator Directory."
