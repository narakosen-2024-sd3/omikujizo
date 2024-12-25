# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false

from typing import Literal

import pigpio
import pytest

from src.lib.gpio.static.output import StaticOutputWrapper
from src.lib.gpio.static.value.logic_level import LogicLevel
from src.lib.gpio.value.gpio_number import GpioNumber


@pytest.mark.parametrize(
  "input,expected",
  [
    (LogicLevel("HIGH"), 1),
    (LogicLevel("LOW"), 0),
  ],
)
def test_set(input: LogicLevel, expected: Literal[0, 1]):
  gpio_number = GpioNumber(2)
  static_output = StaticOutputWrapper(gpio_number)
  static_output.set(input)
  pi = pigpio.pi()
  assert pi.read(gpio=gpio_number.get_value()) == expected
