import time

from .type.time_interface import ITime


class Time(ITime):
  def time(self) -> float:
    return time.time()
