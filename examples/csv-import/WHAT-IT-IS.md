# CSV importer: what it is

Purpose: turn a deliberately selected CSV into validated local transaction rows and an import report.

Input: a CSV with `date, description, amount`. Output: accepted rows, rejected rows with reasons, and a saved import report. Success means the chosen rules were applied and persistence completed; opening a file alone is not success.

Authority: the user selects the source and destination. The importer cannot discover and ingest arbitrary personal folders. This example has no autonomous agents.

The stable contract is the input/rules/result boundary. Storage format and interface style may change without changing that purpose.
