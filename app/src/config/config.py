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
  bow_detector = BowDetectorConfig()
  left_door = LeftDoorConfig()
  right_door = RightDoorConfig()
  halo = HaloConfig()
  jewel = JewelConfig()
  bottom_omikuji = BottomOmikujiConfig()
  top_omikuji = TopOmikujiConfig()


config = __Config()
