from typing import Protocol


class ILight(Protocol):
  def turn_on(self) -> None:
    raise NotImplementedError()

  def turn_off(self) -> None:
    raise NotImplementedError()
