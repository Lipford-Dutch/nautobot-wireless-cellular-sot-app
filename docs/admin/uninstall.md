# Uninstall the App from Nautobot

Use this guide to remove Nautobot Cellular SoT App from a Nautobot environment.

## Database Cleanup

Prior to removing the app from the `nautobot_config.py`, run the following command to roll back any migration specific to this app.

```shell
nautobot-server migrate nautobot_cellular_sot zero
```

This removes app-owned carrier, router, SIM, and operational snapshot tables. Export any data that must be retained before running the migration rollback.

## Remove App configuration

Remove the configuration you added in `nautobot_config.py` from `PLUGINS` and `PLUGINS_CONFIG`.

## Uninstall the package

```shell
pip uninstall nautobot-cellular-sot
```
