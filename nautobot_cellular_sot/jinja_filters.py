"""Reusable Jinja filters for safe cellular displays."""

from django_jinja import library


@library.filter
def mask_iccid(value):
    """Mask an ICCID while retaining enough digits for operator identification."""
    value = str(value or "")
    if len(value) <= 8:
        return value
    return f"{value[:4]}...{value[-4:]}"


@library.filter
def cellular_signal_quality(rsrp_dbm):
    """Return an operator-friendly RSRP quality classification."""
    if rsrp_dbm is None:
        return "Unknown"
    value = float(rsrp_dbm)
    if value >= -80:
        return "Excellent"
    if value >= -90:
        return "Good"
    if value >= -100:
        return "Fair"
    return "Poor"
