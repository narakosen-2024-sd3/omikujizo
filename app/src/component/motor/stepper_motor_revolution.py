from typing import Final, Literal, TypeAlias, get_args

StepperMotorRevolutionType: TypeAlias = Literal[2048, 4096]


class StepperMotorRevolution:
  __AVAILABLE_VALUES: Final[list[StepperMotorRevolutionType]] = list(
    get_args(StepperMotorRevolutionType)
  )

  @staticmethod
  def is_valid(value: StepperMotorRevolutionType) -> bool:
    return value in StepperMotorRevolution.__AVAILABLE_VALUES

  def __init__(self, value: StepperMotorRevolutionType) -> None:
    if not StepperMotorRevolution.is_valid(value):
      raise ValueError("Stepper motor revolution is not valid: {}".format(value))

    self.__value: Final[StepperMotorRevolutionType] = value

  def get_value(self) -> StepperMotorRevolutionType:
    return self.__value

  def equals(self, other: "StepperMotorRevolution") -> bool:
    return self.__value == other.__value
