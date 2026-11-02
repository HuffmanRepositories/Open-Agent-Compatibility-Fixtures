# Fixture review checklist

Use this checklist before changing a fixture's status. A status is a record of evidence, not a badge.

## Draft → reviewed

- [ ] Protocol names, exact versions/revisions, and source links are correct.
- [ ] Source links resolve to authoritative version-pinned material.
- [ ] Input is deterministic and contains no secrets, real credentials, or personal data.
- [ ] Expected outcome follows from the cited source, not from an assumption.
- [ ] Direction (source → target) and transformation/loss are explicit.
- [ ] Unsupported behavior is not represented as successful compatibility.
- [ ] Limitations and untested dimensions are listed.
- [ ] A reviewer other than the author is identified in the review record.

## Reviewed → validated

- [ ] Validation method is named (schema/static check, implementation test, etc.).
- [ ] Implementation names, versions, environment, and reproduction steps are recorded.
- [ ] Positive and negative expectations are exercised where applicable.
- [ ] Test output or artifact is linked and reproducible.
- [ ] Failure, timeout, retry, cancellation, and security boundaries are addressed where relevant.
- [ ] Validation scope is narrow and does not imply broad certification.

## Status meanings

- **draft** — proposed example; not independently reviewed.
- **reviewed** — source and expected behavior reviewed by a second person; not necessarily executed.
- **validated** — the stated test was actually run and reproducible evidence is recorded.

Fixture status never certifies an entire protocol pair, implementation, or deployment. Security review is separate.

## Review record

Record reviewer, date, commit, sources checked, outcome, unresolved comments, and the exact scope of review in the PR or adjacent review notes.
