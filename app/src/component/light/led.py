from src.lib.gpio.static.type.output_interface import IStaticOutput

from .type.light_interface import ILight


class Led(ILight):
  def __init__(self, anode_pin: IStaticOutput) -> None:
    self.__anode_pin = anode_pin

  def turn_on(self) -> None:
    self.__anode_pin.set_high()

  def turn_off(self) -> None:
    self.__anode_pin.set_low()
