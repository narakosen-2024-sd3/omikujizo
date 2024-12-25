from src.lib.gpio.pwm.type.pwm_interface import PwmInterface
from src.lib.gpio.pwm.value.duty_cycle import DutyCycle
from src.lib.gpio.pwm.value.frequency import Frequency
from src.lib.gpio.value.gpio_number import GpioNumber


class PwmDummy(PwmInterface):
  def __init__(self, gpio_number: GpioNumber) -> None:
    self.__gpio_number = gpio_number

  def set(self, frequency: Frequency, duty_cycle: DutyCycle) -> None:
    pass

  def off(self) -> None:
    pass
