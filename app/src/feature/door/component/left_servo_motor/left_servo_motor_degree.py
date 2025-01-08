from typing import Final

from src.component.motor.servo.servo_motor_degree import ServoMotorDegree


class LeftServoMotorDegree(ServoMotorDegree):
  __MIN_VALUE: Final[float] = 0
  __MAX_VALUE: Final[float] = 150

  @staticmethod
  def is_valid(value: float) -> bool:
    return LeftServoMotorDegree.__MIN_VALUE <= value <= LeftServoMotorDegree.__MAX_VALUE

  def __init__(self, value: float) -> None:
    if not LeftServoMotorDegree.is_valid(value):
      raise ValueError(f"LEFT_SERVO_MOTOR_DEGREE_INVALID: {value}")

    self.__value: Final[float] = value
