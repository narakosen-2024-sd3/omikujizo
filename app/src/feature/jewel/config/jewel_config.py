from pydantic import BaseModel

from lib.gpio.value.gpio_number import GpioNumberType


class JewelConfig(BaseModel):
  ANODE_PIN: GpioNumberType = 27
