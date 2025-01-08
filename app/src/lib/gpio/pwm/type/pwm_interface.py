from typing import Protocol

from ..duty_cycle import DutyCycle
from ..frequency import Frequency


class IPwmOutput(Protocol):
  def set(self, frequency: Frequency, duty_cycle: DutyCycle) -> None:
    raise NotImplementedError()

  def off(self) -> None:
    raise NotImplementedError()
