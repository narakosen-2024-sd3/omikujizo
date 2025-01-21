from typing import Final, Literal, TypeAlias, get_args

StateLabelType: TypeAlias = Literal[
  "INITIAL",
  "HUMAN_DETECTABLE",
  "HUMAN_DETECTING",
  "BOW_DETECTING",
  "SPIN",
  "RE_SPIN",
  "RESULT",
  "END",
]


class StateLabel:
  __AVAILABLE_VALUES: Final[list[StateLabelType]] = list(get_args(StateLabelType))

  @staticmethod
  def is_valid(value: StateLabelType) -> bool:
    return value in StateLabel.__AVAILABLE_VALUES

  def __init__(self, value: StateLabelType) -> None:
    if not StateLabel.is_valid(value):
      raise ValueError(f"STATE_LABEL_INVALID: {value}")

    self.__value: Final[StateLabelType] = value

  def equals(self, other: "StateLabel") -> bool:
    return self.__value == other.__value
