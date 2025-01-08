from ..type.human_detector_interface import IHumanDetector


class HumanDetectorDummy(IHumanDetector):
  def detect(self) -> bool:
    print("HumanDetector.detect()")
    return True
