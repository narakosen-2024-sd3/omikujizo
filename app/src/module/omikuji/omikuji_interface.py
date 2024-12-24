from abc import ABCMeta, abstractmethod
from typing import LiteralString


class OmikujiInterface[ROLL_TYPE: LiteralString](metaclass=ABCMeta):
  @abstractmethod
  def start(self) -> None:
    raise NotImplementedError()

  @abstractmethod
  def stop(self, roll: ROLL_TYPE) -> None:
    raise NotImplementedError()
