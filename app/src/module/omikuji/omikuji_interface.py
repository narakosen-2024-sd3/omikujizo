from abc import ABCMeta, abstractmethod


class OmikujiInterface[ROLL_TYPE](metaclass=ABCMeta):
  @abstractmethod
  def start(self) -> None:
    raise NotImplementedError()

  @abstractmethod
  def stop(self, roll: ROLL_TYPE) -> None:
    raise NotImplementedError()
