# Contributing

Thanks for contributing fixture data or test methodology.

## Before submitting

1. Check whether an equivalent fixture already exists.
2. Prefer a small, deterministic fixture that isolates one behavior.
3. Cite the relevant protocol/specification and version or commit.
4. Explain expected behavior and any known ambiguity or semantic loss.
5. Avoid secrets, personal data, copyrighted payloads copied beyond what is necessary, and real production traffic.

## Pull requests

Include:
- purpose and issue/behavior covered;
- source protocol(s), version(s), and references;
- expected outcome and rationale;
- validation command and result;
- limitations or unresolved interpretation.

Fixtures should be neutral: do not label an implementation compatible merely because it accepts a JSON document. Schema validity, semantic equivalence, runtime behavior, and security are separate questions.

## Review

A reviewer should verify source/version references, deterministic expected outcomes, and that the fixture does not silently erase meaningful semantics.
