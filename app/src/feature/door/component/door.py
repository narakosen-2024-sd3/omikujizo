from typing import Final

from src.component.motor.rpm import Rpm
from src.component.motor.servo.type.servo_motor_driver_interface import (
  ServoMotorDriverInterface,
)
from src.component.motor.servo.value.servo_motor_degree import ServoMotorDegree

from ..type.door_interface import DoorInterface


class Door(DoorInterface):
  def __init__(
    self,
    left_servo_motor: ServoMotorDriverInterface,
    right_servo_motor: ServoMotorDriverInterface,
  ) -> None:
    self.__left_servo_motor: Final[ServoMotorDriverInterface] = left_servo_motor
    self.__right_servo_motor: Final[ServoMotorDriverInterface] = right_servo_motor

  def open(self) -> None:
    self.__left_servo_motor.move_to(ServoMotorDegree(-30), Rpm(5))
    self.__right_servo_motor.move_to(ServoMotorDegree(30), Rpm(5))

  def close(self) -> None:
    self.__left_servo_motor.move_to(ServoMotorDegree(90), Rpm(5))
    self.__right_servo_motor.move_to(ServoMotorDegree(-90), Rpm(5))
