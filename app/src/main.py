from config.config import config
from src.component.light.light_driver import LedDriver
from src.component.motor.servo_motor_driver import ServoMotorDriver
from src.component.motor.stepper_motor_driver import StepperMotorDriver
from src.lib.gpio.gpio_number import GpioNumber
from src.lib.gpio.pwm.pwm import PwmWrapper
from src.lib.gpio.static.output import StaticOutputWrapper
from src.lib.time.sleep import Sleep
from src.module.door.door import Door
from src.module.halo.halo import Halo
from src.module.jewel.jewel import Jewel
from src.module.omikuji.omikuji import Omikuji

door = Door(
  ServoMotorDriver(
    PwmWrapper(
      GpioNumber(config.left_door.PWM_PIN),
    ),
  ),
  ServoMotorDriver(
    PwmWrapper(
      GpioNumber(config.right_door.PWM_PIN),
    ),
  ),
)

halo = Halo(
  LedDriver(
    StaticOutputWrapper(
      GpioNumber(config.halo.ANODE_PIN),
    ),
  ),
  Sleep(),
)

jewel = Jewel(
  LedDriver(
    StaticOutputWrapper(
      GpioNumber(config.jewel.ANODE_PIN),
    ),
  ),
)

omikuji_top = Omikuji[config.top_omikuji.ROLL_TYPE](
  StepperMotorDriver(
    PwmWrapper(
      GpioNumber(config.top_omikuji.STEP_PIN),
    ),
  ),
  config.top_omikuji.SEQUENCE,
)

omikuji_bottom = Omikuji[config.bottom_omikuji.ROLL_TYPE](
  StepperMotorDriver(
    PwmWrapper(
      GpioNumber(config.bottom_omikuji.STEP_PIN),
    ),
  ),
  config.bottom_omikuji.SEQUENCE,
)
