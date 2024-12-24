import sys

import pytest
from pytest_mock import MockerFixture

from src.component.motor.rpm import Rpm

epsilon = sys.float_info.epsilon


@pytest.mark.parametrize(
  "input,expected",
  [
    (-1, False),
    (0, True),
    (60, True),
    (61, False),
  ],
)
def test_is_valid(input: int, expected: bool):
  assert Rpm.is_valid(input) == expected


def test_constructor_call_is_valid(mocker: MockerFixture):
  mock = mocker.patch("src.component.motor.rpm.Rpm.is_valid")
  Rpm(0)
  assert mock.call_count == 1


def test_constructor_raise_error(mocker: MockerFixture):
  mock = mocker.patch("src.component.motor.rpm.Rpm.is_valid")
  mock.return_value = False
  with pytest.raises(ValueError):
    Rpm(0)


def test_constructor_success(mocker: MockerFixture):
  mock = mocker.patch("src.component.motor.rpm.Rpm.is_valid")
  mock.return_value = True
  Rpm(-1)


def test_get_value():
  assert Rpm(1).get_value() == 1


@pytest.mark.parametrize(
  "input,expected",
  [
    ((Rpm(0), Rpm(0)), True),
    ((Rpm(0), Rpm(1)), False),
  ],
)
def test_equals(input: tuple[Rpm, Rpm], expected: bool):
  input_1, input_2 = input
  assert input_1.equals(input_2) == expected
