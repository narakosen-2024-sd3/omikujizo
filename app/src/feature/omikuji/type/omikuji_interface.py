from typing import LiteralString, Protocol


class IOmikuji[ROLL_TYPE: LiteralString](Protocol):
  async def start(self) -> None:
    raise NotImplementedError()

  async def stop(self, roll: ROLL_TYPE) -> None:
    raise NotImplementedError()
