from typing import Final

from ..gpio_number import GpioNumber
from .duty_cycle import DutyCycle
from .frequency import Frequency
from .pwm_interface import PwmInterface


class PwmWrapper(PwmInterface):
  def __init__(self, gpio_number: GpioNumber):
    self.__gpio_number: Final[GpioNumber] = gpio_number

  def set(self, frequency: Frequency, duty_cycle: DutyCycle) -> None:
    pass

  def set_zero(self) -> None:
    pass
