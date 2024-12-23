from typing import Final


class ServoMotorDegree:
  __MIN_VALUE: Final[float] = -90
  __MAX_VALUE: Final[float] = 90

  @staticmethod
  def is_valid(value: float) -> bool:
    return (
      ServoMotorDegree.__MIN_VALUE <= value and value <= ServoMotorDegree.__MAX_VALUE
    )

  def __init__(self, value: float) -> None:
    if not ServoMotorDegree.is_valid(value):
      raise ValueError("ServoMotorDegree is not valid: {}".format(value))

    self.__value = value

  def get_value(self) -> float:
    return self.__value
