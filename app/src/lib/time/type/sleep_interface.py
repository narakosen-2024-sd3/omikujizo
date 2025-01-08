from typing import Protocol


class ISleep(Protocol):
  async def sleep(self, time_sec: float) -> None:
    raise NotImplementedError()
