from typing import Protocol

from src.component.camera.image import Image


class IPoseEstimator(Protocol):
  def estimate(self, image: Image) -> None:
    raise NotImplementedError()
