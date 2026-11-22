"""Cellular columns available to Nautobot core device tables."""

import django_tables2 as tables
from nautobot.apps.tables import TableExtension


class DeviceCellularTableExtension(TableExtension):
    """Expose cellular provisioning state as an optional Device column."""

    model = "dcim.device"
    table_columns = {
        "nautobot_cellular_sot_provisioning_state": tables.Column(
            accessor="cellular_router__provisioning_state",
            verbose_name="Cellular State",
            default="—",
        ),
    }

    @classmethod
    def alter_queryset(cls, queryset):
        """Avoid per-row lookups when the optional column is selected."""
        return queryset.select_related("cellular_router")


table_extensions = [DeviceCellularTableExtension]
