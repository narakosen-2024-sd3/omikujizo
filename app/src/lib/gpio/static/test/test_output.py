# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false
# pyright: reportArgumentType=false


import pigpio
import pytest

from src.lib.gpio.gpio_number import GpioNumber
from src.lib.gpio.static.output import StaticOutput


@pytest.mark.skip(reason="Due to hardware dependence")
@pytest.mark.parametrize(
  "input",
  [i for i in range(2, 28)],
)
def test_set_high(input: int):
  gpio_number = GpioNumber(input)
  static_output = StaticOutput(gpio_number)
  static_output.set_high()

  pi = pigpio.pi()
  assert pi.read(gpio=gpio_number.get_value()) == 1


@pytest.mark.skip(reason="Due to hardware dependence")
@pytest.mark.parametrize(
  "input",
  [i for i in range(2, 28)],
)
def test_set_low(input: int):
  gpio_number = GpioNumber(input)
  static_output = StaticOutput(gpio_number)
  static_output.set_low()

  pi = pigpio.pi()
  assert pi.read(gpio=gpio_number.get_value()) == 0
