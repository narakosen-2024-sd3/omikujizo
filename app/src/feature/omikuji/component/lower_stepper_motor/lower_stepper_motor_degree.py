from typing import Final

from src.component.motor.stepper.stepper_motor_degree import StepperMotorDegree


class LowerStepperMotorDegree(StepperMotorDegree):
  __MIN_VALUE: Final[float] = 0
  __MAX_VALUE: Final[float] = 0

  @staticmethod
  def is_valid(value: float) -> bool:
    return (
      LowerStepperMotorDegree.__MIN_VALUE
      <= value
      <= LowerStepperMotorDegree.__MAX_VALUE
    )

  def __init__(self, value: float) -> None:
    if not LowerStepperMotorDegree.is_valid(value):
      raise ValueError(f"LOWER_STEPPER_MOTOR_DEGREE_INVALID: {value}")

    super().__init__(value)
