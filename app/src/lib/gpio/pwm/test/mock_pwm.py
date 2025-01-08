from src.lib.gpio.gpio_number import GpioNumber
from src.lib.gpio.pwm.duty_cycle import DutyCycle
from src.lib.gpio.pwm.frequency import Frequency
from src.lib.gpio.pwm.type.pwm_interface import IPwmOutput


class MockPwmOutput(IPwmOutput):
  def __init__(self, gpio_number: GpioNumber) -> None:
    self.__gpio_number = gpio_number

  def set(self, frequency: Frequency, duty_cycle: DutyCycle) -> None:
    pass

  def off(self) -> None:
    pass
