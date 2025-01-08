from typing import Final


class ServoMotorRpm:
  __MIN_VALUE: Final[int] = 0
  __MAX_VALUE: Final[int] = 120

  @staticmethod
  def is_valid(value: int) -> bool:
    return ServoMotorRpm.__MIN_VALUE <= value <= ServoMotorRpm.__MAX_VALUE

  def __init__(self, value: int) -> None:
    if not ServoMotorRpm.is_valid(value):
      raise ValueError(f"SERVO_MOTOR_RPM_INVALID: {value}")

    self.__value = value

  def get_value(self) -> int:
    return self.__value
