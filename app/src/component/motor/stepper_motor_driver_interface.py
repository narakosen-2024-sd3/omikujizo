from abc import ABCMeta, abstractmethod

from src.lib.gpio.pwm.duty_cycle import DutyCycle

from .rpm import Rpm
from .stepper_motor_degree import StepperMotorDegree
from .stepper_motor_revolution import StepperMotorRevolution


class StepperMotorDriverInterface(metaclass=ABCMeta):
  @abstractmethod
  def move_to(
    self,
    angle: StepperMotorDegree,
    speed: Rpm,
    duty_cycle: DutyCycle = DutyCycle(0.5),
    revolution: StepperMotorRevolution = StepperMotorRevolution(4096),
  ) -> None:
    raise NotImplementedError()
