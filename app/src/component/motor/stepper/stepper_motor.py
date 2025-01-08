from typing import Final

from src.lib.gpio.static.logic_level import LogicLevel
from src.lib.gpio.static.type.output_interface import IStaticOutput
from src.lib.time.type.sleep_interface import ISleep

from .stepper_motor_degree import StepperMotorDegree
from .stepper_motor_rpm import StepperMotorRpm
from .type.stepper_motor_interface import IStepperMotor


class StepperMotor(IStepperMotor):
  __GEAR_REDUCTION_RATIO: Final[float] = 1 / 64
  __STEP_NUM_OF_ROTOR: Final[int] = 8
  __STEP_RESOLUTION: Final[int] = 8
  __INPUTS_SEQUENCE: Final[list[list[LogicLevel]]] = [
    [LogicLevel("LOW"), LogicLevel("LOW"), LogicLevel("LOW"), LogicLevel("HIGH")],
    [LogicLevel("LOW"), LogicLevel("LOW"), LogicLevel("HIGH"), LogicLevel("HIGH")],
    [LogicLevel("LOW"), LogicLevel("LOW"), LogicLevel("HIGH"), LogicLevel("LOW")],
    [LogicLevel("LOW"), LogicLevel("HIGH"), LogicLevel("HIGH"), LogicLevel("LOW")],
    [LogicLevel("LOW"), LogicLevel("HIGH"), LogicLevel("LOW"), LogicLevel("LOW")],
    [LogicLevel("HIGH"), LogicLevel("HIGH"), LogicLevel("LOW"), LogicLevel("LOW")],
    [LogicLevel("HIGH"), LogicLevel("LOW"), LogicLevel("LOW"), LogicLevel("LOW")],
    [LogicLevel("HIGH"), LogicLevel("LOW"), LogicLevel("LOW"), LogicLevel("HIGH")],
  ]

  @staticmethod
  def calc_steps_per_full_rotation() -> float:
    return (
      StepperMotor.__STEP_NUM_OF_ROTOR
      * StepperMotor.__STEP_RESOLUTION
      / StepperMotor.__GEAR_REDUCTION_RATIO
    )

  @staticmethod
  def calc_steps(angle: StepperMotorDegree) -> float:
    return (
      StepperMotor.calc_steps_per_full_rotation() * angle.calc_full_rotation_ratio()
    )

  @staticmethod
  def get_signal(step: int) -> list[LogicLevel]:
    index = step % StepperMotor.__STEP_RESOLUTION
    return StepperMotor.__INPUTS_SEQUENCE[index]

  def __init__(
    self,
    in1_pin: IStaticOutput,
    in2_pin: IStaticOutput,
    in3_pin: IStaticOutput,
    in4_pin: IStaticOutput,
    sleep: ISleep,
    current_step: int = 0,
  ) -> None:
    self.__in1_pin: Final[IStaticOutput] = in1_pin
    self.__in2_pin: Final[IStaticOutput] = in2_pin
    self.__in3_pin: Final[IStaticOutput] = in3_pin
    self.__in4_pin: Final[IStaticOutput] = in4_pin
    self.__sleep: Final[ISleep] = sleep
    self.__current_step: int = current_step

  def input_signal(
    self,
    in1_level: LogicLevel,
    in2_level: LogicLevel,
    in3_level: LogicLevel,
    in4_level: LogicLevel,
  ) -> None:
    self.__in1_pin.set_high() if in1_level.is_high() else self.__in1_pin.set_low()
    self.__in2_pin.set_high() if in2_level.is_high() else self.__in2_pin.set_low()
    self.__in3_pin.set_high() if in3_level.is_high() else self.__in3_pin.set_low()
    self.__in4_pin.set_high() if in4_level.is_high() else self.__in4_pin.set_low()

  async def move(self, angle: StepperMotorDegree, speed: StepperMotorRpm) -> None:
    remain_steps = StepperMotor.calc_steps(angle)
    while remain_steps > 0:
      step = self.__current_step % StepperMotor.__STEP_RESOLUTION
      INPUTS = StepperMotor.__INPUTS_SEQUENCE[step]
      self.input_signal(INPUTS[0], INPUTS[1], INPUTS[2], INPUTS[3])
      self.__current_step += 1
      remain_steps -= 1
      await self.__sleep.sleep(
        60 / speed.get_value() / StepperMotor.calc_steps_per_full_rotation()
      )
