from pydantic import BaseModel

from src.lib.gpio.gpio_number import GpioNumberType


class LeftDoorConfig(BaseModel):
  PWM_PIN: GpioNumberType = 13
  ANGLE_ON_CLOSE: float = 90
  ANGLE_ON_OPEN: float = -30
  SPEED_ON_CLOSE: int = 10
  SPEED_ON_OPEN: int = 10


class RightDoorConfig(BaseModel):
  PWM_PIN: GpioNumberType = 26
  ANGLE_ON_CLOSE: float = -90
  ANGLE_ON_OPEN: float = 30
  SPEED_ON_CLOSE: int = 10
  SPEED_ON_OPEN: int = 10
