from typing import Protocol


class IHalo(Protocol):
  def turn_on(self) -> None:
    raise NotImplementedError()

  def turn_off(self) -> None:
    raise NotImplementedError()

  async def perform_special(self) -> None:
    raise NotImplementedError()
