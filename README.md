# The Seven Ownership Architecture

A documented method for reviewing who owns what in a software system. It separates a component’s identity, observed current structure and future direction so planned behavior does not quietly become an implementation claim.

## Try it

Start with the small [CSV import example](examples/csv-import/README.md), then its [completed design decision](examples/csv-import/DECISION-RECORD.md). Copy the [review worksheet](TEMPLATES/REVIEW-WORKSHEET.md) and the component records for your own workflow. No runtime or external service is required.

The CSV example begins with validation and saving mixed into a button handler. Its completed records identify ownership pressure, propose a boundary, and explicitly mark the change as proposed. The seven categories help ask responsibility questions; they do not require seven deployed services or an agent in every application.

## How it works

Keeping identity, current implementation and future intent separate prevents architectural documents from claiming planned behavior already exists. Read the [mechanism and implementation notes](docs/MECHANISM.md) for the specific boundaries and source links.

Use the records in this order:

1. [WHAT-IT-IS](TEMPLATES/WHAT-IT-IS.md): the component's responsibility and boundary.
2. [CURRENT-STRUCTURE](TEMPLATES/CURRENT-STRUCTURE.md): what the inspected implementation actually does, with evidence and unknowns.
3. [FUTURE-DIRECTION](TEMPLATES/FUTURE-DIRECTION.md): the smallest justified change and how to test it.

The worked CSV decision includes concrete input, expected validation results, persistence failure behavior and an alternative that extracts only a validator. These are proposed acceptance criteria, not captured runtime results.

## Use the method without adopting a platform

Begin with one awkward workflow, such as two callers duplicating a validation rule. Trace its real entrypoint, decisions and effects. Use the ownership categories to ask who should decide each rule; do not create services merely to fill a category. Stop once the chosen boundary and its acceptance evidence are clear.

The [pressure signals](PRESSURE-SIGNALS.md) and [state categories](STATE-CATEGORIES.md) help distinguish a real boundary problem from a preference. The [historical rebuild ledger](CASE-STUDY/REBUILD_LEDGER.md) retains partial and deferred states from Skeleton's rebuild; it is not a statement that today's separate repository implements every proposed step. [Origin](ORIGIN.md)

## Scope

This is a proposed architecture method, not a theorem that seven is the optimal number of components. Record absent responsibilities as absent. The CSV example is a designed teaching scenario, not a claim that an external application was audited or refactored.

## Verify

`python scripts/check_docs.py` checks the documented local links.

MIT licensed; see [LICENSE.md](LICENSE.md). Origin and release boundaries are documented in [ORIGIN.md](ORIGIN.md) and [SECURITY.md](SECURITY.md).
## Inspect the example result

Open the [worked assessment](examples/csv-import/CURRENT-STRUCTURE.md) alongside its [input and demonstration](examples/csv-import/README.md). This is an authored teaching scenario, not a claim about an external application.
