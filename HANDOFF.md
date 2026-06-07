# Cellular SoT Handoff

## Current Scope

This repository is the standalone `nautobot-cellular-sot` project for the Nautobot Wireless Cellular SoT App.

## Branch Model

- `main`: stable release branch
- `development`: integration branch
- `initial-dev`: first implementation branch

## Implemented

- `CarrierProfile`
- `CellularRouter`
- `SIMCard`
- `CellularOperationalSnapshot`
- Wireless Infrastructure dashboard and CRUD pages
- Device detail panel
- REST, GraphQL, summary, and Prometheus endpoints
- Pydantic payload normalization
- DiffSync adapter scaffolding
- Tests, docs, issue templates, CI workflows, and release automation

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
