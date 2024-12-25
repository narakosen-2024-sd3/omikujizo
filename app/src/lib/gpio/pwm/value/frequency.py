from typing import Annotated, Final


class Frequency:
  __MIN_VALUE: Final[float] = 0
  __MAX_VALUE: Final[float] = float("inf")

  @staticmethod
  def is_valid(value_hz: Annotated[float, "Hz"]) -> bool:
    return Frequency.__MIN_VALUE <= value_hz and value_hz <= Frequency.__MAX_VALUE

  def __init__(self, value_hz: float) -> None:
    if not Frequency.is_valid(value_hz):
      raise ValueError("Frequency is not valid: {}".format(value_hz))

    self.__value_hz: Final[float] = value_hz

  def get_value(self) -> float:
    return self.__value_hz

  def equals(self, other: "Frequency") -> bool:
    return self.__value_hz == other.__value_hz
