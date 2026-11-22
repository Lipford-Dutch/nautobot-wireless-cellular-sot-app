"""Shared, domain-neutral helpers for Nautobot Cellular SoT."""

REGISTERED_REGISTRATION_STATES = frozenset({"registered", "roaming"})


def is_registered_state(registration_state: str | None) -> bool:
    """Return whether a registration state represents cellular connectivity."""
    return registration_state in REGISTERED_REGISTRATION_STATES
