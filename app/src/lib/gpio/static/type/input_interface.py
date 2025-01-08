from typing import Protocol


class IStaticInput(Protocol):
  def is_high(self) -> bool:
    raise NotImplementedError()

  def is_low(self) -> bool:
    raise NotImplementedError()
