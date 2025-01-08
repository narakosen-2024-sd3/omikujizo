# pyright: reportArgumentType=false


import pytest

from ..value.stepper_motor_revolution import StepperMotorRevolution


@pytest.mark.parametrize(
  "input,expected",
  [
    (2047, False),
    (2048, True),
    (2049, False),
    (4095, False),
    (4096, True),
    (4097, False),
  ],
)
def test_is_valid(input: int, expected: bool):
  assert StepperMotorRevolution.is_valid(input) == expected
