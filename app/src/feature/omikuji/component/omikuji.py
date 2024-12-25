from typing import Final, LiteralString

from src.component.motor.rpm import Rpm
from src.component.motor.stepper.type.stepper_motor_driver_interface import (
  StepperMotorDriverInterface,
)
from src.component.motor.stepper.value.stepper_motor_degree import StepperMotorDegree

from ..type.omikuji_interface import OmikujiInterface


class Omikuji[ROLL_TYPE: LiteralString](OmikujiInterface[ROLL_TYPE]):
  def __init__(
    self,
    stepper_motor: StepperMotorDriverInterface,
    sequence: list[ROLL_TYPE],
  ) -> None:
    self.__stepper_motor: Final[StepperMotorDriverInterface] = stepper_motor
    self.__sequence: Final[list[ROLL_TYPE]] = sequence

  def start(self) -> None:
    self.__stepper_motor.move_to(StepperMotorDegree(float("inf")), Rpm(15))

  def stop(self, roll: ROLL_TYPE) -> None:
    self.__stepper_motor.move_to(StepperMotorDegree(0), Rpm(15))