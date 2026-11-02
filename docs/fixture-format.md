# Fixture Format

Fixtures should be JSON or another machine-readable format only when it materially improves reproducibility. Keep explanatory context in adjacent Markdown.

## Required metadata

Each fixture should record:

- stable fixture ID;
- short title and intent;
- source protocol(s) and exact version/revision;
- source links;
- status (`draft`, `reviewed`, `validated`);
- input/sample payload;
- expected outcome;
- rationale and known limitations.

## Outcomes

Use OAC's vocabulary where applicable: `direct`, `transformed`, `partial`, `lossy`, `ambiguous`, `unsupported`, or `not-tested`. These are descriptive findings, not certification grades.

## Naming

Use lowercase kebab-case filenames. Keep fixtures minimal and deterministic. Avoid time-dependent values, random IDs, network calls, and environment-dependent expectations unless the test specifically targets those behaviors.

## Security and privacy

Never include credentials, tokens, private keys, personal data, or real user/customer content. Use clearly fake values such as `example-token-not-real`.

## Validation

JSON fixtures must parse. Parsing alone does not establish protocol conformance or semantic correctness. Human review should check references and expected outcomes.
