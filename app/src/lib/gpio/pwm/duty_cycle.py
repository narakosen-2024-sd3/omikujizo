from typing import Final


class DutyCycle:
  __MIN_VALUE: Final[float] = 0
  __MAX_VALUE: Final[float] = 1

  @staticmethod
  def is_valid(value_ratio: float) -> bool:
    return DutyCycle.__MIN_VALUE <= value_ratio and value_ratio <= DutyCycle.__MAX_VALUE

  def __init__(self, value_ratio: float) -> None:
    if not DutyCycle.is_valid(value_ratio):
      raise ValueError("Duty cycle is not valid: {}".format(value_ratio))

    self.__value_ratio: Final[float] = value_ratio

  def get_value(self) -> float:
    return self.__value_ratio

  def equals(self, other: "DutyCycle") -> bool:
    return self.__value_ratio == other.__value_ratio
