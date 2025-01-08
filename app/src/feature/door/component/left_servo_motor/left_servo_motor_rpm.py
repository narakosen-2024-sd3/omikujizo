from typing import Final

from component.motor.servo.servo_motor_rpm import Rpm


class LeftServoMotorRpm(Rpm):
  __MIN_VALUE: Final[int] = 0
  # Refer to operating speed section of sg92r datasheet
  __MAX_VALUE: Final[int] = 36_000

  @staticmethod
  def is_valid(value: int) -> bool:
    return LeftServoMotorRpm.__MIN_VALUE <= value <= LeftServoMotorRpm.__MAX_VALUE

  def __init__(self, value: int) -> None:
    if not LeftServoMotorRpm.is_valid(value):
      raise ValueError(f"LEFT_SERVO_MOTOR_RPM_INVALID: {value}")

    self.__value: Final[int] = value

  def get_value(self) -> int:
    return self.__value
