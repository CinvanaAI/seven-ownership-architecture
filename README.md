# The Seven Ownership Architecture

A documented method for reviewing who owns what in a software system. It separates a component’s identity, observed current structure and future direction so planned behavior does not quietly become an implementation claim.

## Try it

Start with the small [CSV import example](examples/csv-import/README.md), then copy the [three templates](TEMPLATES/WHAT-IT-IS.md) for a component in your own system. No runtime or external service is required.

The CSV example begins with validation and saving mixed into a button handler. Its completed records identify ownership pressure, propose a boundary, and explicitly mark the change as proposed. The seven categories help ask responsibility questions; they do not require seven deployed services or an agent in every application.

## How it works

Keeping identity, current implementation and future intent separate prevents architectural documents from claiming planned behavior already exists. Read the [mechanism and implementation notes](docs/MECHANISM.md) for the specific boundaries and source links.

## Scope

This is a proposed architecture method, not a theorem that seven is the optimal number of components. Record absent responsibilities as absent. The CSV example is a designed teaching scenario, not a claim that an external application was audited or refactored.

## Verify

`python scripts/check_docs.py` checks the documented local links.

MIT licensed; see [LICENSE.md](LICENSE.md). Origin and release boundaries are documented in [ORIGIN.md](ORIGIN.md) and [SECURITY.md](SECURITY.md).
## Inspect the example result

Open the [worked assessment](examples/csv-import/CURRENT-STRUCTURE.md) alongside its [input and demonstration](examples/csv-import/README.md). This is an authored teaching scenario, not a claim about an external application.
