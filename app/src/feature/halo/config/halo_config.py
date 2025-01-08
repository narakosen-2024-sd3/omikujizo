from pydantic import BaseModel

from src.lib.gpio.gpio_number import GpioNumberType


class HaloConfig(BaseModel):
  ANODE_PIN: GpioNumberType = 16
  BLINK_INTERVAL: float = 0.25
  BLINK_TIMES: int = 10
