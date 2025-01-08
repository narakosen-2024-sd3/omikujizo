from ..type.human_detector_interface import IHumanDetector


class HumanDetector(IHumanDetector):
  def __init__(self) -> None:
    pass

  def detect(self) -> bool:
    return True
