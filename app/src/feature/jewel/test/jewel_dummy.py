from ..type.jewel_interface import IJewel


class JewelDummy(IJewel):
  def turn_on(self) -> None:
    print("Jewel.turn_on()")

  def turn_off(self) -> None:
    print("Jewel.turn_off()")
