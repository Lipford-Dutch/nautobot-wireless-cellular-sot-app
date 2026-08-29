"""Nautobot home-page content for cellular operations."""

from nautobot.apps.ui import HomePageItem, HomePagePanel

from nautobot_cellular_sot.models import CarrierProfile, CellularOperationalSnapshot, CellularRouter, SIMCard

layout = (
    HomePagePanel(
        name="Cellular",
        weight=825,
        items=(
            HomePageItem(
                name="Cellular Routers",
                link="plugins:nautobot_cellular_sot:cellularrouter_list",
                model=CellularRouter,
                description="Desired state for cellular-enabled devices",
                permissions=["nautobot_cellular_sot.view_cellularrouter"],
                weight=100,
            ),
            HomePageItem(
                name="SIM Cards",
                link="plugins:nautobot_cellular_sot:simcard_list",
                model=SIMCard,
                description="Physical SIM and eSIM assignments",
                permissions=["nautobot_cellular_sot.view_simcard"],
                weight=200,
            ),
            HomePageItem(
                name="Carrier Profiles",
                link="plugins:nautobot_cellular_sot:carrierprofile_list",
                model=CarrierProfile,
                description="Reusable carrier and APN configuration",
                permissions=["nautobot_cellular_sot.view_carrierprofile"],
                weight=300,
            ),
            HomePageItem(
                name="Operational Snapshots",
                link="plugins:nautobot_cellular_sot:cellularoperationalsnapshot_list",
                model=CellularOperationalSnapshot,
                description="Latest normalized cellular observations",
                permissions=["nautobot_cellular_sot.view_cellularoperationalsnapshot"],
                weight=400,
            ),
        ),
    ),
)
