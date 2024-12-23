from lib.gpio.pwm.pwm_interface import PwmInterface

from .rpm import Rpm
from .servo_motor_degree import ServoMotorDegree
from .servo_motor_driver_interface import ServoMotorDriverInterface


class ServoMotorDriver(ServoMotorDriverInterface):
  @staticmethod
  def calc_duty_cycle() -> float:
    return 0

  def __init__(self, control_pin: PwmInterface) -> None:
    self.__control_pin = control_pin

  def move_to(self, angle: ServoMotorDegree, speed: Rpm) -> None:
    pass
