# A small CSV import review

This is a designed teaching scenario. It shows how to use the method; no application is claimed to have been changed.

An import screen currently reads a CSV file, decides which columns are acceptable, converts amounts, writes records and shows success from one button callback. A headless importer would need to copy that callback. This duplication pressure is the finding.

| Responsibility | Current place | Proposed owner |
| --- | --- | --- |
| Application startup | Main program | Framework |
| Read an explicitly selected external CSV | Button callback | Integration |
| Define column rules and transformations | Button callback | Capability Platform |
| Order validate → import → report | Button callback | Coordination |
| Run one approved import and report its outcome | Button callback | Execution Environment |
| Persist imported records | Button callback | Storage |
| Autonomous actor behavior | Absent | Agents: absent; no agent is required |

The UI remains the host-facing surface for selecting a file and showing a result. A boundary does not require another repository or another process.

Read [WHAT-IT-IS.md](WHAT-IT-IS.md), [CURRENT-STRUCTURE.md](CURRENT-STRUCTURE.md) and [FUTURE-DIRECTION.md](FUTURE-DIRECTION.md) in that order. Compare the words “current” and “proposed”: the record should make it impossible to confuse them.

To try the method yourself, replace this scenario with one actual workflow and point each observation to a source file or test. Leave responsibilities empty when they do not exist.
