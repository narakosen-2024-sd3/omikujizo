import sys

import pytest

from ..frequency import Frequency

epsilon = sys.float_info.epsilon


@pytest.mark.parametrize(
  "input,expected",
  [
    (0 - epsilon, False),
    (0, True),
    (float("inf"), True),
  ],
)
def test_is_valid(input: float, expected: bool):
  assert Frequency.is_valid(input) == expected
