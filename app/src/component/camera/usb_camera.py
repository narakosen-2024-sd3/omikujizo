from typing import Final

import cv2

from .image import Image
from .type.camera_interface import ICamera


class UsbCamera(ICamera):
  def __init__(self, device_id: int) -> None:
    self.__device_id: Final[int] = device_id
    self.__context = cv2.VideoCapture(device_id)

  def capture(self) -> Image:
    is_available, frame = self.__context.read()
    if not is_available:
      raise RuntimeError(f"USB_CAMERA_UNAVAILABLE: {self.__device_id}")

    return Image(frame)
