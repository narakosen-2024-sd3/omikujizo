import subprocess
from typing import Final

import cv2
import numpy as np

from src.component.camera.image import Image

from .type.camera_interface import ICamera


class PiCamera(ICamera):
  __FRAME_WIDTH = 640
  __FRAME_HEIGHT = 480
  __COMMAND = [
    "libcamera-vid",
    "--timeout",
    "0",
    "--nopreview",
    "--width",
    str(__FRAME_WIDTH),
    "--height",
    str(__FRAME_HEIGHT),
    "--framerate",
    "30",
    "--codec",
    "mjpeg",
    "-o",
    "-",
  ]

  def __init__(self) -> None:
    self.__process: Final[subprocess.Popen[bytes]] = subprocess.Popen(
      PiCamera.__COMMAND, stdout=subprocess.PIPE, bufsize=10**8
    )

  def capture(self) -> Image:
    frame_buffer = bytearray()

    while True:
      if self.__process.stdout is None:
        raise RuntimeError("PI_CAMERA_STDOUT_NULL")

      data = self.__process.stdout.read(4096)
      frame_buffer += data

      a = frame_buffer.find(b"\xff\xd8")
      b = frame_buffer.find(b"\xff\xd9")

      if a != -1 and b != -1 and b > a:
        jpg = frame_buffer[a : b + 2]
        frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
        return Image(frame)

  def cleanup(self) -> None:
    self.__process.terminate()
