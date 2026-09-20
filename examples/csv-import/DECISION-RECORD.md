# CSV importer: completed design decision

This is a worked application of the method to the [designed scenario](README.md). It is **not an executed refactor or test result**. Its current evidence is the scenario statement, not a fabricated source repository.

## The question

A second, headless caller needs the same CSV import behavior. Today the button callback reads the source, chooses rules, validates rows, persists accepted rows and renders feedback. Copying the callback would copy the rules too.

The proposed boundary is one pure validator plus one import coordinator. Keep file selection and result rendering in the UI. No additional process, repository or agent is justified by this scenario.

| Decision | Responsibility | Proposed contract |
| --- | --- | --- |
| Read only the selected source | Integration | Selected CSV source → rows or read error |
| Decide acceptable columns/amounts | Capability Platform | Rows + explicit rules → accepted rows and reasoned rejections |
| Order the operation | Coordination | Read → validate → request persistence → report |
| Carry one requested run and its outcome | Execution Environment | Approved inputs → terminal success/failure evidence |
| Store accepted rows | Storage | Accepted rows → confirmed saved count or failure |
| Start the application | Framework | Configuration → initialized callers/services |
| Autonomous behavior | Agents | Absent; leave absent |

These are responsibilities. A small program can implement several as functions in one module.

## Concrete proposed acceptance case

Synthetic input:

```csv
name,amount
alpha,12.50
beta,8.00
gamma,
```

For this scenario, the proposed rules require a nonempty name and a decimal amount. Expected validation result: alpha and beta accepted, gamma rejected with “amount is required.” Expected save request: exactly the two accepted records.

The UI and a headless caller should call the same validator/coordinator and receive equivalent structured results. A storage exception must return a failed outcome; neither caller should show a successful import. Whether partial writes are allowed must be specified by the storage contract before claiming all-or-nothing behavior.

## Alternatives and uncertainty

Keeping the callback is reasonable if no second caller or rule divergence actually exists. Extracting only the validator may be enough if callers legitimately have different save policies. The larger coordinator is justified here only by the shared read/validate/save sequence described in the scenario.

A real audit could invalidate this decision by finding an existing shared importer, a transaction boundary elsewhere, or materially different caller requirements. Inspect those paths before naming a missing owner.

## Finish line

The design decision is complete when its inputs, owner decisions, effects and failure behavior can be reviewed. Implementation remains proposed. After implementation, collect both caller results and a storage-failure test, then update [CURRENT-STRUCTURE](CURRENT-STRUCTURE.md) with actual source evidence. [FUTURE-DIRECTION](FUTURE-DIRECTION.md) must remain proposed until then.
