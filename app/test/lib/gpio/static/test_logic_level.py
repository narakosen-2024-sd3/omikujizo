# pyright: reportArgumentType=false


import pytest
from pytest_mock import MockerFixture

from src.lib.gpio.static.logic_level import LogicLevel


@pytest.mark.parametrize(
  "input,expected",
  [
    ("HIGH", True),
    ("LOW", True),
    ("high", False),
    ("low", False),
  ],
)
def test_is_valid(input: str, expected: bool):
  assert LogicLevel.is_valid(input) == expected


def test_constructor_call_is_valid(mocker: MockerFixture):
  mock = mocker.patch("src.lib.gpio.static.logic_level.LogicLevel.is_valid")
  LogicLevel("HIGH")
  assert mock.call_count == 1


def test_constructor_raise_error(mocker: MockerFixture):
  mock = mocker.patch("src.lib.gpio.static.logic_level.LogicLevel.is_valid")
  mock.return_value = False
  with pytest.raises(ValueError):
    LogicLevel("HIGH")


def test_constructor_success(mocker: MockerFixture):
  mock = mocker.patch("src.lib.gpio.static.logic_level.LogicLevel.is_valid")
  mock.return_value = True
  LogicLevel("invalid value")


@pytest.mark.parametrize(
  "input,expected",
  [("HIGH", True), ("LOW", False)],
)
def test_is_high(input: str, expected: bool):
  assert LogicLevel(input).is_high() == expected


@pytest.mark.parametrize(
  "input,expected",
  [("HIGH", False), ("LOW", True)],
)
def test_is_low(input: str, expected: bool):
  assert LogicLevel(input).is_low() == expected


@pytest.mark.parametrize(
  "input,expected",
  [
    ((LogicLevel("HIGH"), LogicLevel("HIGH")), True),
    ((LogicLevel("HIGH"), LogicLevel("LOW")), False),
  ],
)
def test_equals(input: tuple[LogicLevel, LogicLevel], expected: bool):
  input_1, input_2 = input
  assert input_1.equals(input_2) == expected
