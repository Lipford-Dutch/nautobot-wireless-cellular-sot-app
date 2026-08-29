# Upgrading the App

Use this guide when upgrading Nautobot Cellular SoT App in an existing Nautobot environment.

## Upgrade Guide

1. Review the release notes for compatibility or migration notes.
2. Back up the Nautobot database.
3. Upgrade the package in the Nautobot environment:

    ```shell
    pip install --upgrade nautobot-cellular-sot
    ```

4. Run Nautobot post-upgrade tasks:

    ```shell
    nautobot-server post_upgrade
    ```

5. Restart Nautobot services, workers, and schedulers.
6. Confirm the app loads under Installed Apps and that `/plugins/cellular-sot/` renders.

The `v1.0.0` release has no new Django schema migration. Upgrading from
`v0.1.0` registers the production UI integrations, Operational Snapshot views,
Jobs, runtime configuration, validators, Device extensions, and app metrics
during `post_upgrade` and service restart.
