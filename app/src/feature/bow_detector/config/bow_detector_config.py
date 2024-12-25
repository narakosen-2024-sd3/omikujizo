from pydantic import BaseModel

from ..type.bow_respin_mapping_type import BowRespinMappingType


class BowDetectorConfig(BaseModel):
  BOW_RESPIN_MAPPING: list[BowRespinMappingType] = [
    {
      "bow_min_ratio": 0.9,
      "bow_max_ratio": 1,
      "respin_probability": 0.1,
    },
    {
      "bow_min_ratio": 0.6,
      "bow_max_ratio": 0.9,
      "respin_probability": 0.8,
    },
    {
      "bow_min_ratio": 0.3,
      "bow_max_ratio": 0.6,
      "respin_probability": 0.5,
    },
    {
      "bow_min_ratio": 0.1,
      "bow_max_ratio": 0.3,
      "respin_probability": 0.4,
    },
    {
      "bow_min_ratio": 0,
      "bow_max_ratio": 0.1,
      "respin_probability": 0.3,
    },
  ]
