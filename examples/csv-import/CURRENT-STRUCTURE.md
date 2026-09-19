# CSV importer: current structure

Audit snapshot: **designed scenario**, not observed external software. Confidence applies only to the stated example. Evidence anchor: the callback described in README.md.

The button callback performs external reading, rule decisions, orchestration, persistence and rendering. No separate headless entrypoint exists in the scenario. Files are not yet separated into the proposed owners.

Pressure signal: a command-line import would duplicate column validation. Strength: strong within this scenario. Risk: the desktop and command-line paths could accept different schemas while both say “valid.”

Correctly placed: selecting a file and rendering user feedback belong to the interface. Fused responsibility: choosing the rules and persisting the accepted rows do not need to depend on that interface.

Open question for a real audit: is a separate import runner already present elsewhere? Inspect the call path before claiming it is missing.
