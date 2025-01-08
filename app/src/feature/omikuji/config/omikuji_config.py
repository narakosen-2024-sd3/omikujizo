from typing import Annotated, Literal

from annotated_types import Len
from pydantic import BaseModel

from src.lib.gpio.gpio_number import GpioNumberType


class BottomOmikujiConfig(BaseModel):
  type ROLL_TYPE = Literal["Kichi", "Kyo"]
  IN1_PIN: GpioNumberType = 25
  IN2_PIN: GpioNumberType = 8
  IN3_PIN: GpioNumberType = 7
  IN4_PIN: GpioNumberType = 16
  FLAP_NUM: int = 20
  SEQUENCE: Annotated[
    list[ROLL_TYPE],
    Len(min_length=FLAP_NUM, max_length=FLAP_NUM),
  ] = [
    "Kichi",
    "Kichi",
    "Kichi",
    "Kyo",
    "Kyo",
    "Kyo",
    "Kichi",
    "Kichi",
    "Kyo",
    "Kyo",
    "Kichi",
    "Kichi",
    "Kichi",
    "Kyo",
    "Kyo",
    "Kyo",
    "Kyo",
    "Kichi",
    "Kyo",
    "Kichi",
  ]
  INITIAL_SEQUENCE_INDEX: int = 0
  SPEED_WHEN_SPIN: int = 15


class TopOmikujiConfig(BaseModel):
  type ROLL_TYPE = Literal["Dai", "Sho", ""]
  IN1_PIN: GpioNumberType = 14
  IN2_PIN: GpioNumberType = 15
  IN3_PIN: GpioNumberType = 23
  IN4_PIN: GpioNumberType = 24
  FLAP_NUM: int = 20
  SEQUENCE: Annotated[
    list[ROLL_TYPE], Len(min_length=FLAP_NUM, max_length=FLAP_NUM)
  ] = [
    "Sho",
    "Dai",
    "Sho",
    "Sho",
    "",
    "Dai",
    "Dai",
    "Sho",
    "Sho",
    "",
    "Dai",
    "Dai",
    "Sho",
    "",
    "Dai",
    "",
    "Dai",
    "Sho",
    "Sho",
    "Sho",
  ]
  INITIAL_SEQUENCE_INDEX: int = 0
  SPEED_WHEN_SPIN: int = 15
