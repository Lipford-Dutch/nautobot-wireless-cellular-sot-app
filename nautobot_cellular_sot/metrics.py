"""Bounded-cardinality Prometheus metrics for cellular app health."""

from prometheus_client.metrics_core import GaugeMetricFamily

from nautobot_cellular_sot.models import CellularRouter, SIMCard
from nautobot_cellular_sot.services import get_cellular_summary

METRIC_NAMES = [
    "nautobot_cellular_routers_total",
    "nautobot_cellular_sim_cards_total",
    "nautobot_cellular_registered_routers_total",
    "nautobot_cellular_assignment_conflicts_total",
]


def app_inventory_metrics():
    """Yield aggregate cellular inventory and health counts."""
    summary = get_cellular_summary()
    gauges = (
        ("nautobot_cellular_routers_total", "Number of cellular routers.", CellularRouter.objects.count()),
        ("nautobot_cellular_sim_cards_total", "Number of SIM cards.", SIMCard.objects.count()),
        (
            "nautobot_cellular_registered_routers_total",
            "Number of routers with a registered latest snapshot.",
            summary["registered_count"],
        ),
        (
            "nautobot_cellular_assignment_conflicts_total",
            "Number of desired and observed SIM assignment conflicts.",
            summary["conflict_count"],
        ),
    )
    for name, description, value in gauges:
        gauge = GaugeMetricFamily(name, description)
        gauge.add_metric([], value)
        yield gauge


metrics = [app_inventory_metrics]
