from typing import LiteralString

from ..type.omikuji_interface import IOmikuji


class OmikujiDummy[ROLL_TYPE: LiteralString](IOmikuji[ROLL_TYPE]):
  def start(self) -> None:
    print("Omikuji.start()")

  def stop(self, roll: ROLL_TYPE) -> None:
    print("Omikuji.stop()")
