from typing import Final, LiteralString

from src.feature.door.type.door_interface import IDoor
from src.feature.halo.type.halo_interface import IHalo
from src.feature.omikuji.type.omikuji_interface import IOmikuji

from .state import State


class ResultState[
  TOP_OMIKUJI_ROLL_TYPE: LiteralString,
  BOTTOM_OMIKUJI_ROLL_TYPE: LiteralString,
](State):
  def __init__(
    self,
    door: IDoor,
    halo: IHalo,
    top_omikuji: IOmikuji[TOP_OMIKUJI_ROLL_TYPE],
    bottom_omikuji: IOmikuji[BOTTOM_OMIKUJI_ROLL_TYPE],
  ):
    self.__door: Final[IDoor] = door
    self.__halo: Final[IHalo] = halo
    self.__top_omikuji: Final[IOmikuji[TOP_OMIKUJI_ROLL_TYPE]] = top_omikuji
    self.__bottom_omikuji: Final[IOmikuji[BOTTOM_OMIKUJI_ROLL_TYPE]] = bottom_omikuji

  def entry(self):
    pass

  def do(self):
    pass

  def exit(self):
    pass
