from typing import Final, Literal, TypeAlias, get_args

LuckType: TypeAlias = Literal[
  "Dai-kichi",
  "Sho-kichi",
  "Kichi",
  "Dai-kyo",
  "Sho-kyo",
  "Kyo",
]


class Luck:
  __AVAILABLE_VALUES: Final[list[LuckType]] = list(get_args(LuckType))

  @staticmethod
  def is_valid(value: LuckType) -> bool:
    return value in Luck.__AVAILABLE_VALUES

  def __init__(self, value: LuckType) -> None:
    if not Luck.is_valid(value):
      raise ValueError("Luck is not valid: {}".format(value))

    self.__value: Final[LuckType] = value

  def equals(self, other: "Luck") -> bool:
    return self.__value == other.__value
