from .state.bow_detecting_state import BowDetectingState
from .state.end_state import EndState
from .state.human_detectable_state import HumanDetectableState
from .state.human_detecting_state import HumanDetectingState
from .state.initial_state import InitialState
from .state.re_spin_state import ReSpinState
from .state.result_state import ResultState
from .state.spin_state import SpinState
from .state_label import StateLabel
from .type.state_interface import IState


class StateFactory:
  @staticmethod
  def create_initial_state() -> InitialState:
    return InitialState()

  @staticmethod
  def create_human_detectable_state() -> HumanDetectableState:
    return HumanDetectableState()

  @staticmethod
  def create_human_detecting_state() -> HumanDetectingState:
    return HumanDetectingState()

  @staticmethod
  def create_bow_detecting_state() -> BowDetectingState:
    return BowDetectingState()

  @staticmethod
  def create_spin_state() -> SpinState:
    return SpinState()

  @staticmethod
  def create_re_spin_state() -> ReSpinState:
    return ReSpinState()

  @staticmethod
  def create_result_state() -> ResultState:
    return ResultState()

  @staticmethod
  def create_end_state() -> EndState:
    return EndState()

  @staticmethod
  def create_state(state_label: StateLabel) -> IState:
    if state_label.equals(StateLabel("INITIAL")):
      return StateFactory.create_initial_state()

    if state_label.equals(StateLabel("HUMAN_DETECTABLE")):
      return StateFactory.create_human_detectable_state()

    if state_label.equals(StateLabel("HUMAN_DETECTING")):
      return StateFactory.create_bow_detecting_state()

    if state_label.equals(StateLabel("HUMAN_DETECTABLE")):
      return StateFactory.create_human_detectable_state()

    if state_label.equals(StateLabel("BOW_DETECTING")):
      return StateFactory.create_bow_detecting_state()

    if state_label.equals(StateLabel("SPIN")):
      return StateFactory.create_spin_state()

    if state_label.equals(StateLabel("RE_SPIN")):
      return StateFactory.create_re_spin_state()

    if state_label.equals(StateLabel("RESULT")):
      return StateFactory.create_result_state()

    if state_label.equals(StateLabel("END")):
      return StateFactory.create_end_state()

    raise RuntimeError(f"NO_STATE_LABEL_MATCHED: {state_label}")
