# Fixture Index

These fixtures are **draft mapping examples**, not compatibility evidence or certification.

| Fixture | Status | Intended finding |
|---|---|---|
| [OIX task request ↔ A2A message](oix-a2a-text-request.json) | Draft | Partial mapping; bridge must validate/authenticate and track correlation separately |
| [A2A cancellation unsupported in OIX core](oix-a2a-cancel-unsupported.json) | Draft | Unsupported in OIX v0.1 core; do not invent a core message type |
| [Capability label ↔ Agent Card skill](oix-a2a-capability-mapping.json) | Draft | Partial; explicit reviewed mapping is required |
| [Artifact output ↔ provenance evidence](oix-a2a-artifact-evidence.json) | Draft | Partial; task output is not automatically provenance evidence |
| [Task lifecycle and bridge correlation](oix-a2a-task-state.json) | Draft | Partial; A2A lifecycle state is bridge-mapped, not native OIX semantics |
| [Protocol error vs task failure](oix-a2a-error-mapping.json) | Draft | Partial; preserve error layer, correlation and retryability semantics |
| [Streaming and push updates](oix-a2a-streaming.json) | Draft | Lossy/unsupported without an explicit bridge profile |

Sources:
- OIX v0.1 pinned at [commit 8c25c3b](https://github.com/HuffmanMainNode/Open-Intelligence-Exchange/blob/8c25c3b014eddaf074d5c86f0244e22140617728/protocol/oix-v0.1.md)
- [A2A v1.0.0 specification](https://a2a-protocol.org/v1.0.0/specification)

Fixtures are illustrative static cases only. They do not validate signatures, call protocol endpoints, test implementations, or establish semantic conformance. Review source pins and expected outcomes before promoting status beyond draft.
