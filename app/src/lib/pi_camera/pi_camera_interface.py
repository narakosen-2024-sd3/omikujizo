from abc import ABCMeta, abstractmethod


class PiCameraInterface(metaclass=ABCMeta):
  @abstractmethod
  def capture(self) -> None:
    raise NotImplementedError()
