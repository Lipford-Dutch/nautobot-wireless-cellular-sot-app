# Cellular SoT Handoff

## Current Scope

This repository is the standalone `nautobot-cellular-sot` project for the Nautobot Wireless Cellular SoT App.

## Branch Model

- `main`: production branch and default GitHub target
- `development`: integration branch
- `initial-dev`: first implementation branch

Current public status: Alpha. Treat `main` as the deployable branch, and use pull requests for all documentation, workflow, and app changes.

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
- Alpha marketing page and static docs copy with UI sneak-peek assets

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
