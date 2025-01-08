from typing import Protocol


class IDoor(Protocol):
  def open(self) -> None:
    raise NotImplementedError()

  def close(self) -> None:
    raise NotImplementedError()
