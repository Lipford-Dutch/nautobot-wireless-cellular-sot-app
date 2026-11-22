"""Nautobot Cellular SoT app."""

from nautobot.apps import ConstanceConfigItem, NautobotAppConfig


class NautobotCellularSoTConfig(NautobotAppConfig):
    """App configuration for Nautobot Cellular SoT."""

    name = "nautobot_cellular_sot"
    verbose_name = "Cellular SoT"
    version = "1.0.0"
    author = "Lipford Dutch"
    description = "Authoritative source of truth for cellular routers, SIM cards, and carrier profiles."
    base_url = "cellular-sot"
    api_urls = "nautobot_cellular_sot.api.urls"
    graphql_types = "graphql.types.graphql_types"
    menu_items = "navigation.menu_items"
    template_extensions = "template_content.template_extensions"
    required_settings = []
    min_version = "3.1.0"
    max_version = "4.0.0"
    default_settings = {
        "operational_snapshot_ttl_seconds": 900,
        "sync_batch_size": 500,
        "prometheus_export_enabled": True,
    }
    constance_config = {
        "operational_snapshot_ttl_seconds": ConstanceConfigItem(
            900, "Age in seconds after which an operational snapshot is stale.", int
        ),
        "sync_batch_size": ConstanceConfigItem(500, "Maximum routers processed in one synchronization batch.", int),
        "prometheus_export_enabled": ConstanceConfigItem(
            True, "Enable the authenticated cellular Prometheus export.", bool
        ),
    }
    caching_config = {}
    searchable_models = [
        "CarrierProfile",
        "CellularRouter",
        "SIMCard",
        "CellularOperationalSnapshot",
    ]

    def ready(self):
        """Register the app and expose stable metric names in long-lived web processes."""
        super().ready()
        from nautobot_cellular_sot.metrics import METRIC_NAMES

        if "metrics" in self.features and not self.features["metrics"]:
            self.features["metrics"] = METRIC_NAMES.copy()


config = NautobotCellularSoTConfig
