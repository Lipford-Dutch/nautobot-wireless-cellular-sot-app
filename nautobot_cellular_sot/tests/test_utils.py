"""Tests for shared Cellular SoT helpers."""

from django.test import SimpleTestCase

from nautobot_cellular_sot.utils import is_registered_state


class RegistrationStateTestCase(SimpleTestCase):
    """Validate shared registration-state classification."""

    def test_registered_and_roaming_states_are_connected(self):
        """Registered and roaming states represent connectivity."""
        self.assertTrue(is_registered_state("registered"))
        self.assertTrue(is_registered_state("roaming"))

    def test_other_states_are_not_connected(self):
        """Unknown and absent states do not represent connectivity."""
        self.assertFalse(is_registered_state("unknown"))
        self.assertFalse(is_registered_state(None))
