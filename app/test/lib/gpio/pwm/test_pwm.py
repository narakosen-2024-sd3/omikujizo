# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false

import pigpio
import pytest

from src.lib.gpio.gpio_number import GpioNumber
from src.lib.gpio.pwm.duty_cycle import DutyCycle
from src.lib.gpio.pwm.frequency import Frequency
from src.lib.gpio.pwm.pwm import PwmWrapper


@pytest.mark.parametrize(
  "input,expected",
  [
    ((Frequency(50), DutyCycle(0.5)), (50, 0.5)),
  ],
)
def test_set(input: tuple[Frequency, DutyCycle], expected: tuple[float, float]):
  input_1, input_2 = input
  expected_1, expected_2 = expected

  gpio_number = GpioNumber(2)
  pwm = PwmWrapper(gpio_number)
  pwm.set(input_1, input_2)

  pi = pigpio.pi()
  assert pi.get_PWM_frequency(gpio_number.get_value()) == expected_1
  assert pi.get_PWM_dutycycle(gpio_number.get_value()) == expected_2
