from abc import ABCMeta, abstractmethod

from ...rpm import Rpm
from ..value.servo_motor_degree import ServoMotorDegree


class ServoMotorDriverInterface(metaclass=ABCMeta):
  @abstractmethod
  def move_to(self, angle: ServoMotorDegree, speed: Rpm) -> None:
    raise NotImplementedError()
