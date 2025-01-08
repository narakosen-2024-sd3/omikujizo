from typing import Final


class StepperMotorRpm:
  __MIN_VALUE: Final[float] = 0
  __MAX_VALUE: Final[float] = 10

  @staticmethod
  def is_valid(value: float) -> bool:
    return StepperMotorRpm.__MIN_VALUE <= value <= StepperMotorRpm.__MAX_VALUE

  def __init__(self, value: float) -> None:
    if not StepperMotorRpm.is_valid(value):
      raise ValueError(f"STEPPER_MOTOR_RPM_INVALID: {value}")

    self.__value: Final[float] = value

  def get_value(self) -> float:
    return self.__value
