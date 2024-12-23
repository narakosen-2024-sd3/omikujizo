import time
from typing import Final

from src.lib.gpio.pwm.duty_cycle import DutyCycle
from src.lib.gpio.pwm.frequency import Frequency
from src.lib.gpio.pwm.pwm_interface import PwmInterface

from .rpm import Rpm
from .stepper_motor_degree import StepperMotorDegree
from .stepper_motor_driver_interface import StepperMotorDriverInterface
from .stepper_motor_revolution import StepperMotorRevolution


class StepperMotorDriver(StepperMotorDriverInterface):
  @staticmethod
  def calc_frequency(speed: Rpm, revolution: StepperMotorRevolution) -> float:
    return revolution.get_value() * speed.get_value()

  @staticmethod
  def calc_duration(speed: Rpm, angle: StepperMotorDegree) -> float:
    return angle.get_value() / 360 / speed.get_value()

  def __init__(self, step_pin: PwmInterface) -> None:
    self.__step_pin: Final[PwmInterface] = step_pin

  def move_to(
    self,
    angle: StepperMotorDegree,
    speed: Rpm,
    duty_cycle: DutyCycle = DutyCycle(0.5),
    revolution: StepperMotorRevolution = StepperMotorRevolution(4096),
  ) -> None:
    frequency = StepperMotorDriver.calc_frequency(speed, revolution)
    duration = StepperMotorDriver.calc_duration(speed, angle)

    self.__step_pin.set(Frequency(frequency), duty_cycle)
    time.sleep(duration)
    self.__step_pin.set_zero()
