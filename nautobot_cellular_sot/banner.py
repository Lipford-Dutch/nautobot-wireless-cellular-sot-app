"""Contextual UI banner for cellular operations."""

from nautobot.apps.ui import Banner


def banner(context):
    """Explain the current vendor-collector boundary on cellular pages."""
    request = context["request"]
    if request.path.startswith("/plugins/cellular-sot/"):
        return Banner(
            "Cellular desired state is active. Vendor polling remains disabled until a vendor collector is configured.",
            banner_class="info",
        )
    return None
