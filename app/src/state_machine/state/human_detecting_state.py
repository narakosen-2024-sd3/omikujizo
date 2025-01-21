from typing import Final

from src.feature.human_detector.type.human_detector_interface import (
  IHumanDetector,
)
from src.feature.jewel.type.jewel_interface import IJewel

from ..type.state_interface import IState


class HumanDetectingState(IState):
  def __init__(
    self,
    human_detector: IHumanDetector,
    jewel: IJewel,
  ):
    self.__human_detector: Final[IHumanDetector] = human_detector
    self.__jewel: Final[IJewel] = jewel

  def entry(self):
    pass

  def do(self):
    pass

  def exit(self):
    pass
