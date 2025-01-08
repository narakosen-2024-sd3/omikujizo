from typing import Protocol


class IHumanDetector(Protocol):
  def detect(self) -> bool:
    raise NotImplementedError()
