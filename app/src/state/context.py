from transitions import Machine, State, Transition
from transitions.core import StateIdentifier

states: list[State] = [
  State(
    name="Initial",
  ),
  State(
    name="HumanDetectable",
  ),
]

transitions: list[Transition] = [
  Transition(
    source="Initial",
    dest="HumanDetectable",
  ),
]


class Context:
  def __init__(
    self,
    states: list[State],
    transitions: list[Transition],
    initial: StateIdentifier | None = None,
  ) -> None:
    self.__machine = Machine(
      states=states,
      transitions=transitions,
      initial=initial,
      auto_transitions=False,
      ordered_transitions=False,
    )
