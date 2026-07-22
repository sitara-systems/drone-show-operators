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
| `data/operators.csv` | 10 | Each operator's own site + independent public coverage (news, FAA waiver records) |

Columns: `slug, name, hq_regions, fleet_scale_claim, notable_shows,
notable_shows_source, website, waiver_status`.

## Known caveats

- Fleet-scale and show-count figures are as claimed by the operator or a
  named source — not independently audited by this directory.
- FAA waiver status is reported in three states: confirmed (a docket
  number or documented incident record was found), claimed-not-verified
  (the operator asserts compliance without a checkable number), or not
  publicly stated. Absence of a public claim is not evidence of
  non-compliance.
- Verge Aero and UVify were researched and excluded — both primarily sell
  or lease drone-show platforms to other operators rather than operating
  their own fleet for client shows.
- Companies searched but not verifiable via a live public source (several
  named in the original research brief) were dropped rather than padded
  into the list.

## License

Compilation released under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution:
"The Fleet Operator Directory."
