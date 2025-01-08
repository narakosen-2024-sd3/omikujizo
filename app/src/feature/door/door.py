from typing import Final

from src.component.motor.servo.servo_motor_degree import ServoMotorDegree
from src.component.motor.servo.type.servo_motor_interface import (
  IServoMotor,
)

from .type.door_interface import IDoor


class Door(IDoor):
  def __init__(
    self,
    left_servo_motor: IServoMotor,
    right_servo_motor: IServoMotor,
  ) -> None:
    self.__left_servo_motor: Final[IServoMotor] = left_servo_motor
    self.__right_servo_motor: Final[IServoMotor] = right_servo_motor

  def open(self) -> None:
    self.__left_servo_motor.move_to(ServoMotorDegree(-30), Rpm(5))
    self.__right_servo_motor.move_to(ServoMotorDegree(30), Rpm(5))

  def close(self) -> None:
    self.__left_servo_motor.move_to(ServoMotorDegree(90), Rpm(5))
    self.__right_servo_motor.move_to(ServoMotorDegree(-90), Rpm(5))
