from ..type.jewel_interface import JewelInterface


class JewelDummy(JewelInterface):
  def turn_on(self) -> None:
    print("Jewel.turn_on()")

  def turn_off(self) -> None:
    print("Jewel.turn_off()")
