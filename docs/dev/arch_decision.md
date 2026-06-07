# Architecture Decision Records

## ADR-0001: Nautobot Owns Cellular Desired State

- **Decision:** Store router, SIM assignment, carrier, APN, and provisioning lifecycle state in Nautobot.
- **Reason:** These fields drive provisioning and compliance automation.

## ADR-0002: External Systems Own High-Frequency Telemetry

- **Decision:** Store only the latest normalized operational snapshot in Nautobot.
- **Reason:** Historical RSSI, RSRP, RSRQ, SINR, traffic, and latency data belong in a telemetry database.

## ADR-0003: Conflicts Require Explicit Review

- **Decision:** Never silently replace desired SIM assignment from observed collector state.
- **Reason:** Unexpected SIM changes can have billing, security, and outage impact.
