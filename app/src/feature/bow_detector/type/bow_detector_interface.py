from typing import Protocol


class IBowDetector(Protocol):
  def detect(self) -> bool:
    raise NotImplementedError()
