# test_controller.py
import pytest
from stellar_controller import StellarArray

@pytest.fixture
def controller():
    """Provides a StellarArray instance for testing."""
    return StellarArray("Test Array MK1")

def test_initial_state(controller: StellarArray):
    """Tests the initial state of the controller."""
    assert controller.alignment_degrees == 0
    assert controller.power_output_gw == 100

def test_align_array(controller: StellarArray):
    """Tests the array alignment functionality."""
    target_degrees = 45.0
    alignment_message = controller.align(target_degrees)
    assert controller.alignment_degrees == target_degrees
    assert f"aligned to {target_degrees} degrees" in alignment_message.lower()
    assert f"current power: {controller.power_output_gw} gw" in alignment_message.lower()

def test_adjust_power(controller: StellarArray):
    """Tests power adjustment functionality."""
    initial_power = controller.power_output_gw
    adjustment = 20.5
    controller.adjust_power(adjustment)
    expected_power = initial_power + adjustment
    assert controller.power_output_gw == expected_power
    # Test the message from adjust_power directly
    status_after_adjustment = controller.get_status() # Get status to check final power value
    assert f"power: {expected_power} gw" in status_after_adjustment.lower()


def test_get_status(controller: StellarArray):
    """Tests the status reporting."""
    controller.align(30.0)
    controller.adjust_power(-5.0)
    status_message = controller.get_status()
    assert "alignment at 30.0 degrees" in status_message.lower()
    assert "power: 95.0 gw" in status_message.lower()
