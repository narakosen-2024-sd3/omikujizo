import pytest

from src.lib.gpio.pwm.test.pwm_dummy import PwmDummy
from src.lib.gpio.pwm.value.duty_cycle import DutyCycle
from src.lib.gpio.pwm.value.frequency import Frequency
from src.lib.gpio.value.gpio_number import GpioNumber
from src.lib.time.sleep import Sleep

from ...rpm import Rpm
from ..servo_motor_driver import ServoMotorDriver
from ..value.servo_motor_degree import ServoMotorDegree


@pytest.mark.parametrize(
  "input_angle,input_speed,expected_frequency,expected_duty_cycle",
  [
    (ServoMotorDegree(-90), Rpm(0), Frequency(50), DutyCycle(0.025)),
    (ServoMotorDegree(90), Rpm(0), Frequency(50), DutyCycle(0.12)),
  ],
)
def test_move_to(
  input_angle: ServoMotorDegree,
  input_speed: Rpm,
  expected_frequency: Frequency,
  expected_duty_cycle: DutyCycle,
):
  servo_driver = ServoMotorDriver(PwmDummy(GpioNumber(2)), Sleep())
  servo_driver.move_to(input_angle, input_speed)
