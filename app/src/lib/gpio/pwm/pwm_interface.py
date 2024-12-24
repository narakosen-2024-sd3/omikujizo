from abc import ABCMeta, abstractmethod

from .duty_cycle import DutyCycle
from .frequency import Frequency


class PwmInterface(metaclass=ABCMeta):
  @abstractmethod
  def set(self, frequency: Frequency, duty_cycle: DutyCycle) -> None:
    raise NotImplementedError()

  @abstractmethod
  def off(self) -> None:
    raise NotImplementedError()
