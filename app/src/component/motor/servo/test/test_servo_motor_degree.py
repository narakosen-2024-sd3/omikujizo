import math

import pytest
from pytest_mock import MockerFixture

from ..value.servo_motor_degree import ServoMotorDegree


@pytest.mark.parametrize(
  "input,expected",
  [
    (math.nextafter(-90, -91), False),
    (-90, True),
    (90, True),
    (math.nextafter(90, 91), False),
  ],
)
def test_is_valid(input: float, expected: bool):
  assert ServoMotorDegree.is_valid(input) == expected


def test_constructor_call_is_valid(mocker: MockerFixture):
  mock = mocker.patch(
    "src.component.motor.servo_motor_degree.ServoMotorDegree.is_valid"
  )
  ServoMotorDegree(0)
  assert mock.call_count == 1


def test_constructor_raise_error(mocker: MockerFixture):
  mock = mocker.patch(
    "src.component.motor.servo_motor_degree.ServoMotorDegree.is_valid"
  )
  mock.return_value = False
  with pytest.raises(ValueError):
    ServoMotorDegree(0)


def test_constructor_success(mocker: MockerFixture):
  mock = mocker.patch(
    "src.component.motor.servo_motor_degree.ServoMotorDegree.is_valid"
  )
  mock.return_value = True
  ServoMotorDegree(-99999)


def test_get_value():
  assert ServoMotorDegree(1).get_value() == 1


@pytest.mark.parametrize(
  "input,expected",
  [
    ((ServoMotorDegree(0), ServoMotorDegree(0)), True),
    ((ServoMotorDegree(0), ServoMotorDegree(1)), False),
  ],
)
def test_equals(input: tuple[ServoMotorDegree, ServoMotorDegree], expected: bool):
  input_1, input_2 = input
  assert input_1.equals(input_2) == expected
