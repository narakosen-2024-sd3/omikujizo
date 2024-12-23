from typing import Final


class StepperMotorDegree:
  __MIN_VALUE: Final[float] = -float("inf")
  __MAX_VALUE: Final[float] = float("inf")

  @staticmethod
  def is_valid(value: float) -> bool:
    return (
      StepperMotorDegree.__MIN_VALUE <= value
      and value <= StepperMotorDegree.__MAX_VALUE
    )

  def __init__(self, value: float) -> None:
    if not StepperMotorDegree.is_valid(value):
      raise ValueError("StepperMotorDegree is not valid: {}".format(value))

    self.__value = value

  def get_value(self) -> float:
    return self.__value
