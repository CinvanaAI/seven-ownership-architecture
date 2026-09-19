# CSV importer: future direction

Proposed: extract a pure `validate_rows(rows, rules)` capability and a bounded `import_csv(source, destination, rules)` entrypoint. Keep the interface as a caller. These are function/module boundaries first, not a requirement to create services or repositories.

Acceptance example: a synthetic CSV contains two valid rows and one missing amount. Both UI and command-line callers receive the same two accepted rows and one reasoned rejection. A storage failure reports failure and does not show a successful import.

Evidence to collect after implementation: the shared call path, the synthetic input, both results, and a storage-failure test. Until then, this document remains proposed and CURRENT-STRUCTURE remains unchanged.

Deliberately deferred: an agent, remote database, background scheduling and automatic source discovery. None is required to repair the identified duplication pressure.
