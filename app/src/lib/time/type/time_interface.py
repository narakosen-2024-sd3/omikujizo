from typing import Protocol


class ITime(Protocol):
  def time(self) -> float:
    raise NotImplementedError()
