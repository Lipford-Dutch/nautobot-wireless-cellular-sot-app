# Cellular SoT Handoff

## Current Scope

This repository is the standalone `nautobot-cellular-sot` project for the
Production v1 Nautobot Cellular SoT App.

## Branch Model

- `main`: stable release branch
- `development`: integration branch
- `initial-dev`: first implementation branch

## Implemented

- `CarrierProfile`
- `CellularRouter`
- `SIMCard`
- `CellularOperationalSnapshot`
- Cellular dashboard and CRUD pages
- Operational Snapshot UI, Installed App feature integrations, runtime
  configuration, validation, Jobs, Device extensions, and native app metrics
- Device detail panel
- REST, GraphQL, summary, and Prometheus endpoints
- Pydantic payload normalization
- DiffSync adapter scaffolding
- Tests, docs, issue templates, CI workflows, and release automation

## Release Planning

- Current production release: `v1.0.0`
- V2 specification and planning due: October 1, 2026
- V2 target release window: end of 2026

## Validation

Run:

```shell
poetry run ruff check nautobot_cellular_sot
poetry run ruff format --check nautobot_cellular_sot
poetry run mkdocs build --strict
poetry build
nautobot-server check
nautobot-server test nautobot_cellular_sot.tests
```
