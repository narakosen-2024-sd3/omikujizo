from pydantic import BaseModel

from src.lib.gpio.gpio_number import GpioNumberType


class JewelConfig(BaseModel):
  ANODE_PIN: GpioNumberType = 27
