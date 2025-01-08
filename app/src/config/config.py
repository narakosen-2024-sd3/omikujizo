from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict

from src.feature.bow_detector.config.bow_detector_config import BowDetectorConfig
from src.feature.door.config.door_config import LeftDoorConfig, RightDoorConfig
from src.feature.halo.config.halo_config import HaloConfig
from src.feature.jewel.config.jewel_config import JewelConfig
from src.feature.omikuji.config.omikuji_config import (
  BottomOmikujiConfig,
  TopOmikujiConfig,
)


class __Config(BaseSettings):
  model_config = SettingsConfigDict(env_nested_delimiter="__")
  bow_detector: ClassVar[BowDetectorConfig] = BowDetectorConfig()
  left_door: ClassVar[LeftDoorConfig] = LeftDoorConfig()
  right_door: ClassVar[RightDoorConfig] = RightDoorConfig()
  halo: ClassVar[HaloConfig] = HaloConfig()
  jewel: ClassVar[JewelConfig] = JewelConfig()
  bottom_omikuji: ClassVar[BottomOmikujiConfig] = BottomOmikujiConfig()
  top_omikuji: ClassVar[TopOmikujiConfig] = TopOmikujiConfig()


config = __Config()
