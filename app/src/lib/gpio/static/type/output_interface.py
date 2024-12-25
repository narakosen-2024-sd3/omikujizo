from abc import ABCMeta, abstractmethod

from ..value.logic_level import LogicLevel


class StaticOutputInterface(metaclass=ABCMeta):
  @abstractmethod
  def set(self, logic_level: LogicLevel) -> None:
    raise NotImplementedError()
