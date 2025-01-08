# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownVariableType=false

import mediapipe as mp

from src.component.camera.image import Image

from .type.pose_estimator_interface import IPoseEstimator

mp.tasks.vision.PoseLandmarkerResult


class PoseEstimator(IPoseEstimator):
  def __init__(self) -> None:
    self.__base_options = mp.tasks.BaseOptions
    self.__pose_landmarker = mp.tasks.vision.PoseLandmarker
    self.__pose_landmarker_options = mp.tasks.vision.PoseLandmarkerOptions
    self.__vision_running_mode = mp.tasks.vision.RunningMode

  def estimate(self, image: Image) -> None:
    options = self.__pose_landmarker_options(
      base_options=self.__base_options(
        model_asset_path="",
        running_mode=self.__vision_running_mode.IMAGE,
      )
    )
    with self.__pose_landmarker.create_from_options(options) as landmarker:
      mp_image = mp.Image(image.get_value())
      pose_landmarker_result = landmarker.detect(mp_image)
