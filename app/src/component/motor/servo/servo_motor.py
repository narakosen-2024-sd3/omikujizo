from src.lib.gpio.pwm.duty_cycle import DutyCycle
from src.lib.gpio.pwm.frequency import Frequency
from src.lib.gpio.pwm.type.pwm_interface import IPwmOutput
from src.lib.time.type.sleep_interface import ISleep

from .servo_motor_degree import ServoMotorDegree
from .servo_motor_rpm import ServoMotorRpm
from .type.servo_motor_interface import IServoMotor


class ServoMotor[ANGLE_TYPE: ServoMotorDegree, SPEED_TYPE: ServoMotorRpm](
  IServoMotor[ANGLE_TYPE, SPEED_TYPE]
):
  @staticmethod
  def calc_duty_cycle() -> float:
    return 0

  def __init__(
    self,
    control_pin: IPwmOutput,
    sleep: ISleep,
  ) -> None:
    self.__control_pin = control_pin
    self.__sleep = sleep

  async def move_to(self, angle: ANGLE_TYPE, speed: SPEED_TYPE) -> None:
    self.__control_pin.set(Frequency(50), DutyCycle(0))
