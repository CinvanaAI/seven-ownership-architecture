# One workflow ownership review

Copy this worksheet beside the three component records. Fill it from a real call path; “unknown” is a useful answer. The categories do not dictate repository or process count.

## Observation

- Workflow and concrete trigger:
- Source revision or evidence snapshot:
- Call path (entry → decisions → effects → result):
- Source file/test supporting each step:
- Responsibility currently absent:
- What is observed, inferred, or proposed:

## Pressure and alternatives

- What actual change or failure exposes a boundary problem?
- Who currently decides the rule?
- Who should own the rule, and why can other callers reuse it?
- Alternative: keep the current boundary. What would that cost?
- Alternative: extract one function/module. What would that solve?
- What evidence would disprove this diagnosis?

## Decision

- Smallest chosen change:
- Input/output contract:
- Who may cause each effect?
- Failure result and partially completed effects:
- What remains deliberately unchanged:
- Why a new repository/process/agent is or is not justified:

## Acceptance and stopping point

- One representative input and expected result:
- One failure input and expected effects:
- Existing behavior to preserve:
- Evidence to collect after implementation:
- Status now: proposed / implemented / verified (choose only what evidence supports)
- Stop when:
- Update CURRENT-STRUCTURE only after:
