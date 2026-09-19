# Audit Pressure Signals

Pressure signals are not the same as defects.
They are recurring patterns that suggest architectural strain, likely drift, or upcoming rebuild pressure.

## Core Signals

### `bloat`

One file, module, surface, or owner is carrying too much size or too many concerns.

### `responsibility-fusion`

Multiple responsibilities with different ownership logic are fused into one place.

### `owner-drift`

Meaning appears to be settling in the wrong ownership area.

### `seam-density`

Too many handoffs, adapters, route seams, or cross-boundary touches are concentrated in one place.

### `contract-ambiguity`

It is not clear what the stable contract is, what can change safely, or who owns the contract.

### `custody-ambiguity`

It is unclear whether a thing is merely stored, semantically owned, projected, or transported.

### `shape-pressure`

Accumulated subsystem growth is pushing against the current top-level host or product shape.

### `hardening-pressure`

The thing functions, but secrets, resilience, recoverability, validation, or operational discipline are too weak.

### `cutover-pressure`

The replacement exists, but old paths still shape behavior, routing, or user expectations.

### `strategy-hotspot`

This area frequently triggers repeated architecture questions or rebuild-strategy debates.

## Recommended Recording Pattern

For each signal, record:

- `signal`
- `strength`: low / medium / high
- `where`
- `why`
- `what it threatens`

Example:

```text
- signal: seam-density
  strength: high
  where: host runtime route registration
  why: multiple owners are mounted and translated through one file
  what it threatens: owner purity and maintainable extension
```

## Use Rules

- Put pressure signals in `CURRENT-STRUCTURE` unless they are purely future risks.
- Put future risks in `FUTURE-DIRECTION`.
- Do not use pressure language as a substitute for state categories.
- Do not over-record low-signal cosmetic issues.
