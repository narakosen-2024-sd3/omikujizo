from copy import deepcopy
from typing import Any, Final

import numpy as np

type ImageArray = np.ndarray[Any, np.dtype[np.integer[Any] | np.floating[Any]]]


class Image:
  def __init__(self, value: ImageArray) -> None:
    self.__value: Final[ImageArray] = value

  def get_value(self) -> ImageArray:
    return deepcopy(self.__value)
