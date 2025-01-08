import pytest

from lib.gpio.pwm.test.mock_pwm import DummyPwm
from src.lib.gpio.gpio_number import GpioNumber
from src.lib.gpio.pwm.duty_cycle import DutyCycle
from src.lib.gpio.pwm.frequency import Frequency
from src.lib.time.sleep import Sleep

from ..servo_motor import ServoMotor
from ..servo_motor_degree import ServoMotorDegree
from ..servo_motor_rpm import ServoMotorRpm


@pytest.mark.parametrize(
  "input_angle,input_speed,expected_frequency,expected_duty_cycle",
  [
    (ServoMotorDegree(-90), Rpm(0), Frequency(50), DutyCycle(0.025)),
    (ServoMotorDegree(90), Rpm(0), Frequency(50), DutyCycle(0.12)),
  ],
)
def test_move_to(
  input_angle: ServoMotorDegree,
  input_speed: ServoMotorRpm,
  expected_frequency: Frequency,
  expected_duty_cycle: DutyCycle,
):
  servo_driver = ServoMotor(DummyPwm(GpioNumber(2)), Sleep())
  servo_driver.move_to(input_angle, input_speed)
