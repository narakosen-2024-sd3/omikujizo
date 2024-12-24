from typing import Final


class Rpm:
  __MIN_VALUE: Final[int] = 0
  __MAX_VALUE: Final[int] = 60

  @staticmethod
  def is_valid(value: int) -> bool:
    return Rpm.__MIN_VALUE <= value and value <= Rpm.__MAX_VALUE

  def __init__(self, value: int) -> None:
    if not Rpm.is_valid(value):
      raise ValueError("Rpm is not valid: {}".format(value))

    self.__value = value

  def get_value(self) -> int:
    return self.__value

  def equals(self, other: "Rpm") -> bool:
    return self.__value == other.__value
