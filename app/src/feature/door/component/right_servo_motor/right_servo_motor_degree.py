from typing import Final

from src.component.motor.servo.servo_motor_degree import ServoMotorDegree


class RightServoMotorDegree(ServoMotorDegree):
  __MIN_VALUE: Final[float] = 30
  __MAX_VALUE: Final[float] = 180

  @staticmethod
  def is_valid(value: float) -> bool:
    return (
      RightServoMotorDegree.__MIN_VALUE <= value <= RightServoMotorDegree.__MAX_VALUE
    )

  def __init__(self, value: float) -> None:
    if not RightServoMotorDegree.is_valid(value):
      raise ValueError(f"RIGHT_SERVO_MOTOR_DEGREE_INVALID: {value}")

    self.__value: Final[float] = value
