"""Cross-entry validation for cellular operational data."""

import re

from nautobot.apps.models import CustomValidator


class SnapshotPayloadHashValidator(CustomValidator):
    """Require canonical SHA-256 identifiers for normalized snapshots."""

    model = "nautobot_cellular_sot.cellularoperationalsnapshot"

    def clean(self):
        """Validate that the snapshot payload hash is lowercase SHA-256."""
        obj = self.context["object"]
        if not re.fullmatch(r"[0-9a-f]{64}", obj.payload_hash or ""):
            self.validation_error({"payload_hash": "Payload hash must be a 64-character lowercase SHA-256 digest."})


custom_validators = [SnapshotPayloadHashValidator]
