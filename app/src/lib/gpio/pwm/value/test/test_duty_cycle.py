import sys

import pytest
from pytest_mock import MockerFixture

from ..duty_cycle import DutyCycle

epsilon = sys.float_info.epsilon


@pytest.mark.parametrize(
  "input,expected",
  [
    (0 - epsilon, False),
    (0, True),
    (1, True),
    (1 + epsilon, False),
  ],
)
def test_is_valid(input: float, expected: bool):
  assert DutyCycle.is_valid(input) == expected


def test_constructor_call_is_valid(mocker: MockerFixture):
  mock = mocker.patch("src.lib.gpio.pwm.duty_cycle.DutyCycle.is_valid")
  DutyCycle(0)
  assert mock.call_count == 1


def test_constructor_raise_error(mocker: MockerFixture):
  mock = mocker.patch("src.lib.gpio.pwm.duty_cycle.DutyCycle.is_valid")
  mock.return_value = False
  with pytest.raises(ValueError):
    DutyCycle(0)


def test_constructor_success(mocker: MockerFixture):
  mock = mocker.patch("src.lib.gpio.pwm.duty_cycle.DutyCycle.is_valid")
  mock.return_value = True
  DutyCycle(-1)


def test_get_value():
  assert DutyCycle(1).get_value() == 1


@pytest.mark.parametrize(
  "input,expected",
  [
    ((DutyCycle(0), DutyCycle(0)), True),
    ((DutyCycle(0), DutyCycle(1)), False),
  ],
)
def test_equals(input: tuple[DutyCycle, DutyCycle], expected: bool):
  input_1, input_2 = input
  assert input_1.equals(input_2) == expected
