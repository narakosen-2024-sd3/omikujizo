import sys

import pytest
from pytest_mock import MockerFixture

from src.lib.gpio.pwm.frequency import Frequency

epsilon = sys.float_info.epsilon


@pytest.mark.parametrize(
  "input,expected",
  [
    (0 - epsilon, False),
    (0, True),
    (float("inf"), True),
  ],
)
def test_is_valid(input: float, expected: bool):
  assert Frequency.is_valid(input) == expected


def test_constructor_call_is_valid(mocker: MockerFixture):
  mock = mocker.patch("src.lib.gpio.pwm.frequency.Frequency.is_valid")
  Frequency(0)
  assert mock.call_count == 1


def test_constructor_raise_error(mocker: MockerFixture):
  mock = mocker.patch("src.lib.gpio.pwm.frequency.Frequency.is_valid")
  mock.return_value = False
  with pytest.raises(ValueError):
    Frequency(0)


def test_constructor_success(mocker: MockerFixture):
  mock = mocker.patch("src.lib.gpio.pwm.frequency.Frequency.is_valid")
  mock.return_value = True
  Frequency(-1)


def test_get_value():
  assert Frequency(50).get_value() == 50


@pytest.mark.parametrize(
  "input,expected",
  [
    ((Frequency(0), Frequency(0)), True),
    ((Frequency(0), Frequency(1)), False),
  ],
)
def test_equals(input: tuple[Frequency, Frequency], expected: bool):
  input_1, input_2 = input
  assert input_1.equals(input_2) == expected
