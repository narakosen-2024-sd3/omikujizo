# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false

from typing import Literal

import pigpio
import pytest

from src.lib.gpio.gpio_number import GpioNumber
from src.lib.gpio.static.input import StaticInputWrapper
from src.lib.gpio.static.logic_level import LogicLevel


@pytest.mark.parametrize(
  "input,expected",
  [
    (1, LogicLevel("HIGH")),
    (0, LogicLevel("LOW")),
  ],
)
def test_read(input: Literal[0, 1], expected: LogicLevel):
  gpio_number = GpioNumber(2)
  pi = pigpio.pi()
  pi.write(gpio=gpio_number.get_value(), level=input)
  static_input = StaticInputWrapper(gpio_number)
  assert static_input.read() == expected
