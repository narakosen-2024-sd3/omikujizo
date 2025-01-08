from typing import Protocol

from ..stepper_motor_degree import StepperMotorDegree
from ..stepper_motor_rpm import StepperMotorRpm


class IStepperMotor(Protocol):
  async def move(self, angle: StepperMotorDegree, speed: StepperMotorRpm) -> None:
    raise NotImplementedError()
