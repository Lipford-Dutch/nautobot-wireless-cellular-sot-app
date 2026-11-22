"""Cellular filters added to Nautobot core device views."""

import django_filters
from django import forms
from nautobot.apps.filters import FilterExtension


def _filter_has_cellular(queryset, _name, value):
    """Filter devices by the presence of a cellular desired-state record."""
    if value is None:
        return queryset
    return queryset.filter(cellular_router__isnull=not value)


class DeviceCellularFilterExtension(FilterExtension):
    """Add a cellular-enabled selector to Device filters."""

    model = "dcim.device"
    filterset_fields = {
        "nautobot_cellular_sot_has_cellular": django_filters.BooleanFilter(method=_filter_has_cellular),
    }
    filterform_fields = {
        "nautobot_cellular_sot_has_cellular": forms.NullBooleanField(
            label="Has cellular configuration", required=False
        ),
    }


filter_extensions = [DeviceCellularFilterExtension]
