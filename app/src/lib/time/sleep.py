import asyncio

from .type.sleep_interface import ISleep


class Sleep(ISleep):
  async def sleep(self, time_sec: float) -> None:
    await asyncio.sleep(time_sec)
