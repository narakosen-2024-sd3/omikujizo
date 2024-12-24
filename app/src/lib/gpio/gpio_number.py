from typing import Final, Literal, get_args

type GpioNumberType = Literal[
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  10,
  11,
  12,
  13,
  14,
  15,
  16,
  17,
  18,
  19,
  20,
  21,
  22,
  23,
  24,
  25,
  26,
  27,
]


class GpioNumber:
  __AVAILABLE_VALUES: Final[list[GpioNumberType]] = list(get_args(GpioNumberType))

  @staticmethod
  def is_valid(value: GpioNumberType) -> bool:
    return value in GpioNumber.__AVAILABLE_VALUES

  def __init__(self, value: GpioNumberType) -> None:
    if not GpioNumber.is_valid(value):
      raise ValueError("Gpio number is not valid: {}".format(value))

    self.__value: Final[GpioNumberType] = value

  def get_value(self) -> GpioNumberType:
    return self.__value

  def equals(self, other: object) -> bool:
    if not isinstance(other, GpioNumber):
      return False
    return self.__value == other.__value
