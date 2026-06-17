"""Template extensions for core Nautobot objects."""

from nautobot.apps.ui import TemplateExtension


class DeviceCellularExtension(TemplateExtension):
    """Add cellular desired and operational state to Device detail pages."""

    model = "dcim.device"

    def buttons(self):
        """No custom Device detail buttons are added."""
        return ""

    def list_buttons(self):
        """No custom Device list buttons are added."""
        return ""

    def left_page(self):
        """No left-side Device detail panel is added."""
        return ""

    def full_width_page(self):
        """No full-width Device detail panel is added."""
        return ""

    def detail_tabs(self):
        """No custom Device detail tabs are added."""
        return ""

    def right_page(self):
        """Render the cellular panel when the device is a cellular router."""
        router = getattr(self.context["object"], "cellular_router", None)
        if router is None:
            return ""
        return self.render(
            "nautobot_cellular_sot/inc/device_cellular_panel.html",
            extra_context={"cellular_router": router},
        )


template_extensions = [DeviceCellularExtension]
