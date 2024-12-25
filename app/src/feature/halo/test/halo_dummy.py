from ..type.halo_interface import HaloInterface


class HaloDummy(HaloInterface):
  def turn_on(self) -> None:
    print("Halo.turn_on()")

  def turn_off(self) -> None:
    print("Halo.turn_off()")

  def perform_special(self) -> None:
    print("Halo.perform_special()")
