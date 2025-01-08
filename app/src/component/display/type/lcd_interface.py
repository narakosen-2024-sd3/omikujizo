from typing import Protocol


class ILcd(Protocol):
  def display(self, text: str) -> None:
    raise NotImplementedError()
