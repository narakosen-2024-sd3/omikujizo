from abc import ABCMeta, abstractmethod


class LcdDriverInterface(metaclass=ABCMeta):
  @abstractmethod
  def display(self, text: str) -> None:
    raise NotImplementedError()
