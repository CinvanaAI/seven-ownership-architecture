# Completion And Audit State Categories

Use these categories to describe present state honestly.

## Primary States

### `healthy`

The thing exists and is correctly shaped enough for its current scope.
It may still have future work, but its current structure is not materially lying about what it is.

### `partial`

The thing exists, but only part of its intended structure or behavior is implemented.
The current shape may still be correct as far as it goes.

### `wrong-shaped`

The thing exists, but its structure, boundary, or ownership is materially incorrect.
This is not the same as "unfinished."

### `not-yet-built`

The thing does not meaningfully exist yet in implementation.
Do not use this for code that exists but is bad.

### `deferred`

The thing is intentionally not being built yet because a prerequisite, higher-priority layer, or sequencing constraint comes first.

### `blocked`

The thing cannot be completed responsibly until another dependency or decision lands.

### `reference-only`

The thing exists as legacy, evidence, or source material, but is not yet re-homed as authoritative structure in the intended architecture.

### `productization-pending`

The design or implementation exists, but packaging, installability, operability, or end-user readiness is still incomplete.

### `hardening-pending`

The thing works functionally, but durability, security, resilience, access control, or operational robustness is not sufficient yet.

### `cutover-pending`

The replacement exists, but the platform has not yet switched authoritative use to it or removed the legacy path.

### `uncertain`

The audit does not have enough evidence yet to state the condition confidently.

## Usage Rules

- A thing may carry more than one state if that is the honest description.
- `wrong-shaped` should be used only when structure or ownership is materially incorrect.
- `partial` should not be used as a polite substitute for `wrong-shaped`.
- `deferred` should name the dependency or sequencing reason.
- `reference-only` should identify the authoritative source it is still standing in for.
- `productization-pending`, `hardening-pending`, and `cutover-pending` are not substitutes for architectural completion.

## Recommended Recording Pattern

In `CURRENT-STRUCTURE`, record:

- `overall state`
- `supporting states`
- `confidence`
- `reason`

Example:

```text
- overall state: partial
- supporting states:
  - hardening-pending
  - cutover-pending
- confidence: medium
- reason: Owner boundaries are clearer than legacy, but the subsystem is not yet the authoritative product path.
```

## Anti-Drift Rule

If a thing sits in `deferred`, `reference-only`, or `cutover-pending` for long enough that it begins shaping the system anyway, open an architecture-pressure note.
