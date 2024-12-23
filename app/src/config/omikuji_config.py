from typing import Annotated, Literal

from annotated_types import Len
from pydantic import BaseModel

from src.lib.gpio.gpio_number import GpioNumberType


class BottomOmikujiConfig(BaseModel):
  type ROLL_TYPE = Literal["Kichi", "Kyo"]
  DIR_PIN: GpioNumberType = 23
  ENABLE_PIN: GpioNumberType = 14
  STEP_PIN: GpioNumberType = 25
  SEQUENCE: Annotated[list[ROLL_TYPE], Len(min_length=20, max_length=20)] = [
    "Kichi",
    "Kichi",
    "Kyo",
    "Kyo",
    "Kyo",
    "Kyo",
    "Kichi",
    "Kichi",
    "Kyo",
    "Kichi",
    "Kichi",
    "Kyo",
    "Kyo",
    "Kichi",
    "Kichi",
    "Kichi",
    "Kichi",
    "Kyo",
    "Kyo",
    "Kyo",
  ]
  SPEED_ON_SPIN: int = 15


class TopOmikujiConfig(BaseModel):
  type ROLL_TYPE = Literal["Dai", "Sho", ""]
  DIR_PIN: GpioNumberType = 8
  ENABLE_PIN: GpioNumberType = 24
  STEP_PIN: GpioNumberType = 15
  SEQUENCE: Annotated[list[ROLL_TYPE], Len(min_length=20, max_length=20)] = [
    "Dai",
    "Sho",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
  ]
  SPEED_ON_SPIN: int = 15
