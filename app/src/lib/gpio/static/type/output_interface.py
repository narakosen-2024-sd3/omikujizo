from typing import Protocol


class IStaticOutput(Protocol):
  def set_high(self) -> None:
    raise NotImplementedError()

  def set_low(self) -> None:
    raise NotImplementedError()
