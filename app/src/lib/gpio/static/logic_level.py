from typing import Final, Literal, TypeAlias, get_args

LogicLevelType: TypeAlias = Literal["HIGH", "LOW"]


class LogicLevel:
  __AVAILABLE_VALUES: Final[list[LogicLevelType]] = list(get_args(LogicLevelType))

  @staticmethod
  def is_valid(value: LogicLevelType) -> bool:
    return value in LogicLevel.__AVAILABLE_VALUES

  def __init__(self, value: LogicLevelType) -> None:
    if not LogicLevel.is_valid(value):
      raise ValueError(f"LOGIC_LEVEL_INVALID: {value}")

    self.__value: Final[LogicLevelType] = value

  def is_high(self) -> bool:
    return self.__value == "HIGH"

  def is_low(self) -> bool:
    return self.__value == "LOW"

  def equals(self, other: "LogicLevel") -> bool:
    return self.__value == other.__value
