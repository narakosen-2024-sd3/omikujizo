from src.lib.gpio.pwm.type.pwm_interface import PwmInterface
from src.lib.gpio.pwm.value.duty_cycle import DutyCycle
from src.lib.gpio.pwm.value.frequency import Frequency
from src.lib.time.sleep_interface import SleepInterface

from ..rpm import Rpm
from .type.servo_motor_driver_interface import ServoMotorDriverInterface
from .value.servo_motor_degree import ServoMotorDegree


class ServoMotorDriver(ServoMotorDriverInterface):
  @staticmethod
  def calc_duty_cycle() -> float:
    return 0

  def __init__(
    self,
    control_pin: PwmInterface,
    sleep: SleepInterface,
  ) -> None:
    self.__control_pin = control_pin
    self.__sleep = sleep

  def move_to(self, angle: ServoMotorDegree, speed: Rpm) -> None:
    # TODO: Implements
    raise NotImplementedError()
    self.__control_pin.set(Frequency(50), DutyCycle(0))
