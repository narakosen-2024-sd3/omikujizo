from typing import Final

from src.feature.bow_detector.type.bow_detector_interface import IBowDetector
from src.feature.human_detector.type.human_detector_interface import (
  IHumanDetector,
)
from src.feature.jewel.type.jewel_interface import IJewel

from ..type.state_interface import IState


class BowDetectingState(IState):
  def __init__(
    self,
    bow_detector: IBowDetector,
    human_detector: IHumanDetector,
    jewel: IJewel,
  ):
    self.__bow_detector: Final[IBowDetector] = bow_detector
    self.__human_detector: Final[IHumanDetector] = human_detector
    self.__jewel: Final[IJewel] = jewel

  def entry(self):
    pass

  def do(self):
    pass

  def exit(self):
    pass
