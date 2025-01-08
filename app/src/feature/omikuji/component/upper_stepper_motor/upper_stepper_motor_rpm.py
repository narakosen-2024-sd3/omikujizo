from typing import Final

from src.component.motor.stepper.stepper_motor_rpm import StepperMotorRpm


class UpperStepperMotorRpm(StepperMotorRpm):
  __MIN_VALUE: Final[int] = 0
  __MAX_VALUE: Final[int] = 0

  pass
