import pytest
from pytest_mock import MockerFixture

from src.component.motor.stepper_motor_degree import StepperMotorDegree


@pytest.mark.parametrize(
  "input,expected",
  [
    (-float("inf"), True),
    (float("inf"), True),
  ],
)
def test_is_valid(input: float, expected: bool):
  assert StepperMotorDegree.is_valid(input) == expected


def test_constructor_call_is_valid(mocker: MockerFixture):
  mock = mocker.patch(
    "src.component.motor.stepper_motor_degree.StepperMotorDegree.is_valid"
  )
  StepperMotorDegree(0)
  assert mock.call_count == 1


def test_constructor_raise_error(mocker: MockerFixture):
  mock = mocker.patch(
    "src.component.motor.stepper_motor_degree.StepperMotorDegree.is_valid"
  )
  mock.return_value = False
  with pytest.raises(ValueError):
    StepperMotorDegree(0)


def test_constructor_success(mocker: MockerFixture):
  mock = mocker.patch(
    "src.component.motor.stepper_motor_degree.StepperMotorDegree.is_valid"
  )
  mock.return_value = True
  StepperMotorDegree("not numeric")  # pyright: ignore[reportArgumentType]


def test_get_value():
  assert StepperMotorDegree(1).get_value() == 1


@pytest.mark.parametrize(
  "input,expected",
  [
    ((StepperMotorDegree(0), StepperMotorDegree(0)), True),
    ((StepperMotorDegree(0), StepperMotorDegree(1)), False),
  ],
)
def test_equals(input: tuple[StepperMotorDegree, StepperMotorDegree], expected: bool):
  input_1, input_2 = input
  assert input_1.equals(input_2) == expected
