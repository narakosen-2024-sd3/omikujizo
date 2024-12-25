from src.lib.gpio.static.type.output_interface import StaticOutputInterface
from src.lib.gpio.static.value.logic_level import LogicLevel

from .type.light_driver_interface import LightDriverInterface


class LedDriver(LightDriverInterface):
  def __init__(self, anode_pin: StaticOutputInterface) -> None:
    self.__anode_pin = anode_pin

  def turn_on(self) -> None:
    self.__anode_pin.set(LogicLevel("HIGH"))

  def turn_off(self) -> None:
    self.__anode_pin.set(LogicLevel("LOW"))
