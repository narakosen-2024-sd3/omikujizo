import sys

import pytest

from ..duty_cycle import DutyCycle

epsilon = sys.float_info.epsilon


@pytest.mark.parametrize(
  "input,expected",
  [
    (0 - epsilon, False),
    (0, True),
    (1, True),
    (1 + epsilon, False),
  ],
)
def test_is_valid(input: float, expected: bool):
  assert DutyCycle.is_valid(input) == expected
