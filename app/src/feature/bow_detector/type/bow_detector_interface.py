from abc import ABCMeta, abstractmethod


class BowDetectorInterface(metaclass=ABCMeta):
  @abstractmethod
  def detect(self) -> bool:
    raise NotImplementedError()
