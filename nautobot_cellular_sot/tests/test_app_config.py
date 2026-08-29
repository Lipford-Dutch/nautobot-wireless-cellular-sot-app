"""App integration configuration tests."""

from django.test import SimpleTestCase
from django.test.client import RequestFactory

from nautobot_cellular_sot import NautobotCellularSoTConfig, config
from nautobot_cellular_sot.banner import banner
from nautobot_cellular_sot.jobs import ReconcileCellularInventory, jobs
from nautobot_cellular_sot.metrics import METRIC_NAMES
from nautobot_cellular_sot.navigation import menu_items


class AppConfigTestCase(SimpleTestCase):
    """Validate Nautobot integration hooks."""

    def test_config_export_points_to_app_config(self):
        """The package exports its Nautobot app configuration."""
        self.assertIs(config, NautobotCellularSoTConfig)

    def test_navigation_uses_nautobot_menu_items_hook(self):
        """The app registers navigation through Nautobot's menu_items hook."""
        self.assertEqual(config.menu_items, "navigation.menu_items")

    def test_integration_paths_are_relative_to_the_app(self):
        """Nautobot resolves integration hook paths relative to the app package."""
        self.assertEqual(config.jobs, "jobs.jobs")
        self.assertEqual(config.graphql_types, "graphql.types.graphql_types")
        self.assertEqual(config.template_extensions, "template_content.template_extensions")

    def test_all_cellular_models_are_searchable(self):
        """Global search includes every cellular data model."""
        self.assertEqual(
            set(config.searchable_models),
            {"CarrierProfile", "CellularRouter", "SIMCard", "CellularOperationalSnapshot"},
        )

    def test_production_navigation_and_jobs(self):
        """Production navigation and reconciliation Job are registered."""
        self.assertEqual(menu_items[0].name, "Cellular")
        self.assertEqual(menu_items[0].groups[0].name, "Operations")
        self.assertEqual(jobs, [ReconcileCellularInventory])

    def test_production_ui_and_metrics_integrations(self):
        """Production UI and metric integrations expose stable registrations."""
        request = RequestFactory().get("/plugins/cellular-sot/")

        self.assertIsNotNone(banner({"request": request}))
        self.assertEqual(len(METRIC_NAMES), 4)
        self.assertEqual(
            set(config.constance_config),
            {"operational_snapshot_ttl_seconds", "sync_batch_size", "prometheus_export_enabled"},
        )
