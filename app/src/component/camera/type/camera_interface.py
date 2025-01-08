from typing import Protocol

from ..image import Image


class ICamera(Protocol):
  def capture(self) -> Image:
    raise NotImplementedError()
