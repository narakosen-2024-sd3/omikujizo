from abc import ABCMeta, abstractmethod

from .logic_level import LogicLevel


class StaticInputInterface(metaclass=ABCMeta):
  @abstractmethod
  def read(self) -> LogicLevel:
    raise NotImplementedError()
