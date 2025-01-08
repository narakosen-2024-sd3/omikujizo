# pyright: reportArgumentType=false


import pytest

from ..gpio_number import GpioNumber


@pytest.mark.parametrize(
  "input,expected",
  [
    (0, False),
    (1, False),
    (2, True),
    (27, True),
    (28, False),
  ],
)
def test_is_valid(input: int, expected: bool):
  assert GpioNumber.is_valid(input) == expected
