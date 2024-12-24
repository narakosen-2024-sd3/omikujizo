# pyright: reportArgumentType=false


import pytest
from pytest_mock import MockerFixture

from src.component.motor.stepper_motor_revolution import StepperMotorRevolution


@pytest.mark.parametrize(
  "input,expected",
  [
    (2047, False),
    (2048, True),
    (2049, False),
    (4095, False),
    (4096, True),
    (4097, False),
  ],
)
def test_is_valid(input: int, expected: bool):
  assert StepperMotorRevolution.is_valid(input) == expected


def test_constructor_call_is_valid(mocker: MockerFixture):
  mock = mocker.patch(
    "src.component.motor.stepper_motor_revolution.StepperMotorRevolution.is_valid"
  )
  StepperMotorRevolution(2048)
  assert mock.call_count == 1


def test_constructor_raise_error(mocker: MockerFixture):
  mock = mocker.patch(
    "src.component.motor.stepper_motor_revolution.StepperMotorRevolution.is_valid"
  )
  mock.return_value = False
  with pytest.raises(ValueError):
    StepperMotorRevolution(2048)


def test_constructor_success(mocker: MockerFixture):
  mock = mocker.patch(
    "src.component.motor.stepper_motor_revolution.StepperMotorRevolution.is_valid"
  )
  mock.return_value = True
  StepperMotorRevolution(0)


def test_get_value():
  assert StepperMotorRevolution(2048).get_value() == 2048


@pytest.mark.parametrize(
  "input,expected",
  [
    ((StepperMotorRevolution(2048), StepperMotorRevolution(2048)), True),
    ((StepperMotorRevolution(2048), StepperMotorRevolution(4096)), False),
  ],
)
def test_equals(
  input: tuple[StepperMotorRevolution, StepperMotorRevolution], expected: bool
):
  input_1, input_2 = input
  assert input_1.equals(input_2) == expected
