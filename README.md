# Nautobot Wireless Cellular SoT App

[![Nautobot](https://img.shields.io/badge/Nautobot-3.1%2B-blue)](https://www.networktocode.com/nautobot/)
[![Python](https://img.shields.io/badge/Python-3.10--3.14-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache--2.0-green)](https://github.com/Lipford-Dutch/nautobot-wireless-cellular-sot-app/blob/main/LICENSE)
[![Status](https://img.shields.io/badge/Status-Alpha-orange)](https://github.com/Lipford-Dutch/nautobot-wireless-cellular-sot-app/discussions)

Nautobot Wireless Cellular SoT App is an Alpha Nautobot app that turns cellular routers, SIM cards, carrier profiles, and normalized latest-state observations into one operator-owned Source of Truth. Nautobot owns desired state while external collectors own high-frequency polling and telemetry history.

## Repository Metadata

- Package: `nautobot-cellular-sot`
- Python module: `nautobot_cellular_sot`
- GitHub repository: `Lipford-Dutch/nautobot-wireless-cellular-sot-app`
- Production branch: `main`
- Development branches: `development`, `initial-dev`
- License: Apache-2.0

## Alpha Focus

- Production target: Nautobot `>=3.1.0,<4.0.0` with Python `>=3.10,<3.15`, including Python 3.14 compatibility metadata.
- Current rollout: model, UI, REST, GraphQL, summary, Prometheus, and SSoT scaffolding are in place for operator validation.
- Feedback lanes: [Roadmap Discussion](https://github.com/Lipford-Dutch/nautobot-wireless-cellular-sot-app/discussions/2) and [Field Reports](https://github.com/Lipford-Dutch/nautobot-wireless-cellular-sot-app/discussions/3).

## Features

- Device-native cellular router extensions using Nautobot `Device`, `Interface`, and `InventoryItem`.
- SIM assignment, slot uniqueness, lifecycle state, ICCID masking, and protected relationships.
- Carrier and APN desired-state profiles.
- Latest-only operational snapshots for registration and signal state.
- Wireless Infrastructure dashboard, CRUD pages, filters, tables, and Device detail panel.
- REST API, GraphQL types, summary endpoint, and bounded-cardinality Prometheus export.
- Pydantic normalization and DiffSync adapter scaffolding.
- Transaction-safe SIM assignment and stale snapshot rejection.
- Nautobot cookiecutter CI, security workflows, release automation, docs, issue templates, and Towncrier.
- Standalone high-energy marketing page with UI sneak-peek screenshots from the documentation assets.

## Installation

```shell
pip install nautobot-cellular-sot
```

```python
PLUGINS = ["nautobot_cellular_sot"]

PLUGINS_CONFIG = {
    "nautobot_cellular_sot": {
        "operational_snapshot_ttl_seconds": 900,
        "sync_batch_size": 500,
        "prometheus_export_enabled": True,
    }
}
```

```shell
nautobot-server post_upgrade
```

## API

| Endpoint | Purpose |
| --- | --- |
| `/api/plugins/cellular-sot/carrier-profiles/` | Carrier profile CRUD |
| `/api/plugins/cellular-sot/cellular-routers/` | Cellular router CRUD |
| `/api/plugins/cellular-sot/sim-cards/` | SIM card CRUD |
| `/api/plugins/cellular-sot/operational-snapshots/` | Latest operational snapshot CRUD |
| `/api/plugins/cellular-sot/summary/` | Aggregate cellular state |
| `/api/plugins/cellular-sot/prometheus/` | Prometheus text export |

## Development

```powershell
.\.venv\Scripts\poetry.exe install
.\.venv\Scripts\poetry.exe run invoke start
.\.venv\Scripts\poetry.exe run invoke unittest
.\.venv\Scripts\poetry.exe run invoke ruff
.\.venv\Scripts\poetry.exe run mkdocs build --strict
```

The standalone marketing page is available at [`cellular.html`](https://github.com/Lipford-Dutch/nautobot-wireless-cellular-sot-app/blob/main/cellular.html).

The documentation copy is available at [`docs/cellular.html`](https://github.com/Lipford-Dutch/nautobot-wireless-cellular-sot-app/blob/main/docs/cellular.html) for static publishing workflows.
