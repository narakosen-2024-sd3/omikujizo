# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false

from typing import Final

import pigpio

from ..gpio_number import GpioNumber
from .duty_cycle import DutyCycle
from .frequency import Frequency
from .pwm_interface import PwmInterface


class PwmWrapper(PwmInterface):
  def __init__(self, gpio_number: GpioNumber):
    self.__gpio_number: Final[GpioNumber] = gpio_number
    self.__gpio: Final[pigpio.pi] = pigpio.pi()

  def set(self, frequency: Frequency, duty_cycle: DutyCycle) -> None:
    self.__gpio.set_PWM_frequency(
      user_gpio=self.__gpio_number.get_value(),
      frequency=frequency.get_value(),
    )
    self.__gpio.set_PWM_dutycycle(
      user_gpio=self.__gpio_number.get_value(),
      dutycycle=int(duty_cycle.get_value() * 255),
    )

  def off(self) -> None:
    self.set(Frequency(0), DutyCycle(0))
