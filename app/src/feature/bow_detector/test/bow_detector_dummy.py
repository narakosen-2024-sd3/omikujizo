from ..type.bow_detector_interface import BowDetectorInterface


class BowDetectorDummy(BowDetectorInterface):
  def detect(self) -> bool:
    print("BowDetector.detect()")
    return True
