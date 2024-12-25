from ..type.door_interface import DoorInterface


class DoorDummy(DoorInterface):
  def open(self) -> None:
    print("Door.open()")

  def close(self) -> None:
    print("Door.close()")
