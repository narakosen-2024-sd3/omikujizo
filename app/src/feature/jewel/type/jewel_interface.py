from typing import Protocol


class IJewel(Protocol):
  def turn_on(self) -> None:
    raise NotImplementedError()

  def turn_off(self) -> None:
    raise NotImplementedError()
