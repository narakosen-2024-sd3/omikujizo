from typing import Final

from src.feature.human_detector.type.human_detector_interface import (
  IHumanDetector,
)

from ..type.state_interface import IState


class HumanDetectableState(IState):
  def __init__(self, human_detector: IHumanDetector):
    self.__human_detector: Final[IHumanDetector] = human_detector

  def entry(self):
    pass

  def do(self):
    pass

  def exit(self):
    pass
