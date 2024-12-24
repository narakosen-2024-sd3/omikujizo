# pyright: reportArgumentType=false


import pytest
from pytest_mock import MockerFixture

from src.lib.gpio.gpio_number import GpioNumber


@pytest.mark.parametrize(
  "input,expected",
  [
    (0, False),
    (1, False),
    (2, True),
    (27, True),
    (28, False),
  ],
)
def test_is_valid(input: int, expected: bool):
  assert GpioNumber.is_valid(input) == expected


def test_constructor_call_is_valid(mocker: MockerFixture):
  mock = mocker.patch("src.lib.gpio.gpio_number.GpioNumber.is_valid")
  GpioNumber(2)
  assert mock.call_count == 1


def test_constructor_raise_error(mocker: MockerFixture):
  mock = mocker.patch("src.lib.gpio.gpio_number.GpioNumber.is_valid")
  mock.return_value = False
  with pytest.raises(ValueError):
    GpioNumber(2)


def test_constructor_success(mocker: MockerFixture):
  mock = mocker.patch("src.lib.gpio.gpio_number.GpioNumber.is_valid")
  mock.return_value = True
  GpioNumber(0)


def test_get_value():
  assert GpioNumber(2).get_value() == 2


@pytest.mark.parametrize(
  "input,expected",
  [
    ((GpioNumber(2), GpioNumber(2)), True),
    ((GpioNumber(2), GpioNumber(3)), False),
  ],
)
def test_equals(input: tuple[GpioNumber, GpioNumber], expected: bool):
  input_1, input_2 = input
  assert input_1.equals(input_2) == expected
