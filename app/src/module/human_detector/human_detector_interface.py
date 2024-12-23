from abc import ABCMeta, abstractmethod


class HumanDetectorInterface(metaclass=ABCMeta):
  @abstractmethod
  def detect(self) -> bool:
    raise NotImplementedError()
