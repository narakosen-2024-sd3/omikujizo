from ..type.bow_detector_interface import IBowDetector


class BowDetectorDummy(IBowDetector):
  def detect(self) -> bool:
    print("BowDetector.detect()")
    return True
