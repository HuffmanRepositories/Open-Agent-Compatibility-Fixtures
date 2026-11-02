# Open Agent Compatibility Fixtures

Versioned, reproducible fixtures for evaluating interoperability between existing agent protocols and implementations.

This repository supports [Open Agent Compatibility (OAC)](https://github.com/HuffmanRepositories/Open-Agent-Compatibility). It is a test-data and evidence repository—not a protocol, runtime, adapter, or certification program.

## Goals

- Store small, deterministic examples for protocol concepts and edge cases.
- Pin each fixture to source specifications and versions.
- Make expected mappings, transformations, losses, and unsupported behavior explicit.
- Enable repeatable validation and future implementation-level tests.
- Keep fixture content neutral and reviewable.

## Non-goals

- Define a universal agent protocol or canonical message format.
- Replace MCP, A2A, OIX, upstream adapter projects, or schema registries.
- Claim compatibility, security, or certification from fixture validation alone.
- Store secrets, production credentials, personal data, or live customer payloads.

## Repository layout

- `fixtures/` — protocol-specific and cross-protocol sample data.
- `expected/` — expected outcomes or mapping notes for fixtures.
- `schemas/` — only schemas needed to validate this repository's fixture metadata; not protocol schemas.
- `docs/` — contribution and fixture authoring guidance.
- `scripts/` — lightweight deterministic validation.

## Fixture status

Fixtures are evidence artifacts, not compatibility claims. Each fixture should identify its source/version, purpose, assumptions, and expected result. Status should distinguish draft, reviewed, and validated.

## Start here

- [Fixture format](docs/fixture-format.md)
- [Contribution guide](CONTRIBUTING.md)
- [Governance](GOVERNANCE.md)
- [Current fixture index](fixtures/README.md)

## Relationship to OAC

OAC documents compatibility concepts, mappings, and methodology. This repository holds reusable test fixtures. Any mapping claim must link to the relevant OAC profile and source specifications. Keep implementation-specific tests in their upstream project unless a shared, neutral fixture is clearly useful.

## License

MIT. See [LICENSE](LICENSE).
