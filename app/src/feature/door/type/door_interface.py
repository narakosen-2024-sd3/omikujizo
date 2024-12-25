from abc import ABCMeta, abstractmethod


class DoorInterface(metaclass=ABCMeta):
  @abstractmethod
  def open(self) -> None:
    raise NotImplementedError()

  @abstractmethod
  def close(self) -> None:
    raise NotImplementedError()
