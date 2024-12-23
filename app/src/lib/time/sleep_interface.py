from abc import ABCMeta, abstractmethod


class SleepInterface(metaclass=ABCMeta):
  @abstractmethod
  def sleep(self, time_sec: float) -> None:
    raise NotImplementedError()
