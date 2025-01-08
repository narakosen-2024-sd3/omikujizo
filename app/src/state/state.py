from typing import Protocol

from component.camera.image import Image
from lib.gpio.static.logic_level import LogicLevel
from src.lib.gpio.gpio_number import GpioNumber


class State(Protocol):
  def entry(self) -> None:
    raise NotImplementedError()

  def do(self) -> None:
    raise NotImplementedError()

  def exit(self) -> None:
    raise NotImplementedError()

  def on_gpio_changed(
    self,
    gpio_number: GpioNumber,
    logic_level: LogicLevel,
  ) -> None:
    raise NotImplementedError()

  def on_camera_captured(
    self,
    image: Image,
  ) -> None:
    raise NotImplementedError()
