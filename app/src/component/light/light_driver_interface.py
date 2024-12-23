from abc import ABCMeta, abstractmethod


class LightDriverInterface(metaclass=ABCMeta):
  @abstractmethod
  def turn_on(self) -> None:
    raise NotImplementedError()

  @abstractmethod
  def turn_off(self) -> None:
    raise NotImplementedError()
