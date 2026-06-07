# Installing the App

## Prerequisites

- Nautobot `>=3.1.0,<4.0.0`
- Python `>=3.10,<3.15`
- PostgreSQL or MySQL

## Install

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
sudo systemctl restart nautobot nautobot-worker nautobot-scheduler
```

## Verification

1. Run `nautobot-server check`.
2. Confirm `nautobot-server migrate --check` reports no pending migrations.
3. Open **Wireless Infrastructure > Cellular > Dashboard**.
4. Verify the summary and Prometheus API endpoints with an authenticated token.
