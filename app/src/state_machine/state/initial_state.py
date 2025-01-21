from typing import Final, LiteralString

from src.feature.bow_detector.type.bow_detector_interface import IBowDetector
from src.feature.door.type.door_interface import IDoor
from src.feature.halo.type.halo_interface import IHalo
from src.feature.human_detector.type.human_detector_interface import (
  IHumanDetector,
)
from src.feature.jewel.type.jewel_interface import IJewel
from src.feature.omikuji.type.omikuji_interface import IOmikuji

from ..disposable import Disposable
from ..type.disposable_interface import IDisposable
from ..type.state_interface import EventHandler, IState


class InitialState[
  TOP_OMIKUJI_ROLL_TYPE: LiteralString,
  BOTTOM_OMIKUJI_ROLL_TYPE: LiteralString,
](IState):
  def __init__(
    self,
    bow_detector: IBowDetector,
    human_detector: IHumanDetector,
    door: IDoor,
    halo: IHalo,
    jewel: IJewel,
    top_omikuji: IOmikuji[TOP_OMIKUJI_ROLL_TYPE],
    bottom_omikuji: IOmikuji[BOTTOM_OMIKUJI_ROLL_TYPE],
  ):
    self.__bow_detector: Final[IBowDetector] = bow_detector
    self.__human_detector: Final[IHumanDetector] = human_detector
    self.__door: Final[IDoor] = door
    self.__halo: Final[IHalo] = halo
    self.__jewel: Final[IJewel] = jewel
    self.__top_omikuji: Final[IOmikuji[TOP_OMIKUJI_ROLL_TYPE]] = top_omikuji
    self.__bottom_omikuji: Final[IOmikuji[BOTTOM_OMIKUJI_ROLL_TYPE]] = bottom_omikuji
    self.__state_change_event_listeners: list[EventHandler]

  def entry(self):
    pass

  def do(self):
    pass

  def exit(self):
    pass

  def subscribe_state_change_event(self, handler: EventHandler) -> IDisposable:
    def remove():
      self.__state_change_event_listeners.remove(handler)

    self.__state_change_event_listeners.append(handler)

    return Disposable(remove)
