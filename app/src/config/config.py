from pydantic_settings import BaseSettings, SettingsConfigDict

from .bow_detector_config import BowDetectorConfig
from .door_config import LeftDoorConfig, RightDoorConfig
from .halo_config import HaloConfig
from .jewel_config import JewelConfig
from .omikuji_config import BottomOmikujiConfig, TopOmikujiConfig


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
