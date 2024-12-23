import time

from .sleep_interface import SleepInterface


class Sleep(SleepInterface):
  def sleep(self, time_sec: float) -> None:
    time.sleep(time_sec)
