# Open Agent Compatibility Fixtures: Reproducible Evidence

**Author:** Robert Huffman  
**Status:** Fixture whitepaper, version 0.1

## Abstract

This repository provides small, versioned, synthetic fixtures that make protocol compatibility questions reproducible. It complements Open Agent Compatibility (OAC): OAC owns the analysis and mapping methodology; this repository owns reusable examples and expected outcomes.

## Why fixtures matter

Compatibility claims are difficult to review when examples are informal, unversioned, or mixed with implementation-specific behavior. A fixture should make one question visible: what input was considered, which source specification/version applies, what behavior is expected, and what ambiguity or information loss remains.

## Fixture model

A useful fixture is minimal, deterministic, synthetic, and independently understandable. It should include a stable identifier, source/version context, purpose, assumptions, expected outcome, and review status. The corpus separates fixture data from expected outcomes and validation support.

## How to use this repository

Read [START-HERE.md](START-HERE.md), [docs/fixture-format.md](docs/fixture-format.md), and [docs/review-checklist.md](docs/review-checklist.md). Inspect the fixture index before adding a case. Run python scripts/validate_fixtures.py after changes. Put cross-protocol analysis in OAC and link the relevant mapping profile from each fixture.

## What validation means

The validator checks structural rules and selected metadata constraints. It does not run real agent implementations, prove semantic equivalence, or certify security or conformance. A fixture can be structurally valid and still contain a mistaken expectation; human review remains essential.

## Governance

Keep all cases synthetic and offline. Never add secrets, personal data, customer payloads, or live service traces. Preserve upstream ownership and cite authoritative source versions.

— Robert Huffman