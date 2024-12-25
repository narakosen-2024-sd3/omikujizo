from typing import Final, Literal, TypeAlias, get_args

LogicLevelType: TypeAlias = Literal["HIGH", "LOW"]


class LogicLevel:
  """LogicLevel

  論理電圧値を表すクラス

  """

  __AVAILABLE_VALUES: Final[list[LogicLevelType]] = list(get_args(LogicLevelType))
  """論理電圧値一覧
  
  論理電圧値の列挙．文字列「 HIGH 」「 LOW 」（すべて大文字）を格納した配列．
  
  """

  @staticmethod
  def is_valid(value: LogicLevelType) -> bool:
    """入力値検証

    value 引数の値が，論理電圧値として正しいか判定する．
    正しい場合は True を返し，正しくない場合は False を返す．

    Args:
      value: 論理電圧値

    Returns:
      bool: 論理電圧値として正しいかどうか

    Examples:
      >>> LogicLevel.is_valid("HIGH")
      True

      >>> LogicLevel.is_valid("high")
      False

    """
    return value in LogicLevel.__AVAILABLE_VALUES

  def __init__(self, value: LogicLevelType) -> None:
    """コンストラクタ

    value 引数の値が，論理電圧値として正しいなら value 属性を value 引数で初期化する．
    正しくないなら，初期化せず例外をスローする．

    Args:
      value: 論理電圧値

    Raises:
      ValueError: value 引数が論理電圧値として正しくない場合に発生

    Examples:
      >>> level = LogicLevel("HIGH")
      >>> level = LogicLevel("high")
      ValueError: Logic level is invalid: high

    """
    if not LogicLevel.is_valid(value):
      raise ValueError("Logic level is invalid: {}".format(value))

    self.__value: Final[LogicLevelType] = value

  def is_high(self) -> bool:
    """アクティブハイ判定

    value 属性の値が「 HIGH 」なら True を返し，それ以外の場合は False を返す．

    Returns:
      bool: 論理電圧値が HIGH かどうか

    Examples:
      >>> LogicLevel("HIGH").is_high()
      True

      >>> LogicLevel("LOW").is_high()
      False

    """
    return self.__value == "HIGH"

  def is_low(self) -> bool:
    """アクティブロー判定

    value 属性の値が「 LOW 」なら True を返し，それ以外の場合は False を返す．

    Returns:
      bool: 論理電圧値が LOW かどうか

    Examples:
      >>> LogicLevel("LOW").is_low()
      True

      >>> LogicLevel("HIGH").is_low()
      False

    """
    return self.__value == "LOW"

  def equals(self, other: "LogicLevel") -> bool:
    """同値判定

    other 引数が，自身と同じ論理電圧値かどうか判定する．
    同じならば True を返し，異なる場合は False を返す．

    Args:
      other: LogicLevel インスタンス

    Returns:
      bool: 自分と同じ論理電圧値かどうか

    Examples:
      >>> LogicLevel("HIGH").equals(LogicLevel("HIGH"))
      True

      >>> LogicLevel("HIGH").equals(LogicLevel("LOW"))
      False

    """
    return self.__value == other.__value
