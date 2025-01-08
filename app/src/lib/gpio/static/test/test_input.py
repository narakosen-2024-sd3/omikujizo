# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false
# pyright: reportArgumentType=false


import pigpio
import pytest

from src.lib.gpio.gpio_number import GpioNumber
from src.lib.gpio.static.input import StaticInput


@pytest.mark.skip(reason="Due to hardware dependence")
@pytest.mark.parametrize(
  "input",
  [i for i in range(2, 28)],
)
def test_is_high(input: int):
  gpio_number = GpioNumber(input)
  static_input = StaticInput(gpio_number)
  pi = pigpio.pi()

  pi.write(gpio=gpio_number.get_value(), level=1)
  assert static_input.is_high() is True

  pi.write(gpio=gpio_number.get_value(), level=0)
  assert static_input.is_high() is False


@pytest.mark.skip(reason="Due to hardware dependence")
@pytest.mark.parametrize(
  "input",
  [i for i in range(2, 28)],
)
def test_is_low(input: int):
  gpio_number = GpioNumber(input)
  static_input = StaticInput(gpio_number)
  pi = pigpio.pi()

  pi.write(gpio=gpio_number.get_value(), level=1)
  assert static_input.is_low() is False

  pi.write(gpio=gpio_number.get_value(), level=0)
  assert static_input.is_low() is True
