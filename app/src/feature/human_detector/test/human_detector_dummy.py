from ..type.human_detector_interface import HumanDetectorInterface


class HumanDetectorDummy(HumanDetectorInterface):
  def detect(self) -> bool:
    print("HumanDetector.detect()")
    return True
