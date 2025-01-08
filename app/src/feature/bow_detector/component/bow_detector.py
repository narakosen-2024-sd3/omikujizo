from ..type.bow_detector_interface import IBowDetector


class BowDetector(IBowDetector):
  def __init__(self) -> None:
    pass

  def detect(self) -> bool:
    return True
