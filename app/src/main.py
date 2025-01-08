from src.component.camera.usb_camera import UsbCamera
from src.component.light.led import Led
from src.component.motor.servo.servo_motor import ServoMotor
from src.component.motor.stepper.stepper_motor import StepperMotor
from src.config.config import config
from src.feature.door.door import Door
from src.feature.halo.halo import Halo
from src.feature.jewel.jewel import Jewel
from src.feature.omikuji.omikuji import Omikuji
from src.lib.gpio.gpio_number import GpioNumber
from src.lib.gpio.pwm.test.mock_pwm import MockPwmOutput as PwmOutput
from src.lib.gpio.static.test.mock_output import MockStaticOutput as StaticOutput
from src.lib.time.sleep import Sleep

camera = UsbCamera(0)

door = Door(
  left_servo_motor=ServoMotor(
    control_pin=PwmOutput(gpio_number=GpioNumber(value=config.left_door.PWM_PIN)),
    sleep=Sleep(),
  ),
  right_servo_motor=ServoMotor(
    control_pin=PwmOutput(gpio_number=GpioNumber(value=config.right_door.PWM_PIN)),
    sleep=Sleep(),
  ),
)

halo = Halo(
  tape_light=Led(
    anode_pin=StaticOutput(gpio_number=GpioNumber(value=config.halo.ANODE_PIN)),
  ),
  sleep=Sleep(),
)

jewel = Jewel(
  led=Led(
    anode_pin=StaticOutput(gpio_number=GpioNumber(value=config.jewel.ANODE_PIN)),
  ),
)

top_omikuji = Omikuji[config.top_omikuji.ROLL_TYPE](
  stepper_motor=StepperMotor(
    in1_pin=StaticOutput(gpio_number=GpioNumber(value=config.top_omikuji.IN1_PIN)),
    in2_pin=StaticOutput(gpio_number=GpioNumber(value=config.top_omikuji.IN2_PIN)),
    in3_pin=StaticOutput(gpio_number=GpioNumber(value=config.top_omikuji.IN3_PIN)),
    in4_pin=StaticOutput(gpio_number=GpioNumber(value=config.top_omikuji.IN4_PIN)),
    sleep=Sleep(),
  ),
  sequence=config.top_omikuji.SEQUENCE,
)

bottom_omikuji = Omikuji[config.bottom_omikuji.ROLL_TYPE](
  stepper_motor=StepperMotor(
    in1_pin=StaticOutput(gpio_number=GpioNumber(value=config.bottom_omikuji.IN1_PIN)),
    in2_pin=StaticOutput(gpio_number=GpioNumber(value=config.bottom_omikuji.IN2_PIN)),
    in3_pin=StaticOutput(gpio_number=GpioNumber(value=config.bottom_omikuji.IN3_PIN)),
    in4_pin=StaticOutput(gpio_number=GpioNumber(value=config.bottom_omikuji.IN4_PIN)),
    sleep=Sleep(),
  ),
  sequence=config.bottom_omikuji.SEQUENCE,
)
