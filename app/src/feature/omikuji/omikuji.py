from typing import Final, LiteralString

from component.motor.stepper.stepper_motor_rpm import StepperMotorRpm
from component.motor.stepper.type.stepper_motor_interface import (
  IStepperMotor,
)
from src.component.motor.stepper.stepper_motor_degree import StepperMotorDegree

from .type.omikuji_interface import IOmikuji


class Omikuji[ROLL_TYPE: LiteralString](IOmikuji[ROLL_TYPE]):
  def __init__(
    self,
    stepper_motor: IStepperMotor,
    sequence: list[ROLL_TYPE],
  ) -> None:
    self.__stepper_motor: Final[IStepperMotor] = stepper_motor
    self.__sequence: Final[list[ROLL_TYPE]] = sequence

  async def start(self) -> None:
    await self.__stepper_motor.move(
      StepperMotorDegree(float("inf")), StepperMotorRpm(15)
    )

  async def stop(self, roll: ROLL_TYPE) -> None:
    await self.__stepper_motor.move(StepperMotorDegree(0), StepperMotorRpm(15))
