from ..type.door_interface import IDoor


class DoorDummy(IDoor):
  def open(self) -> None:
    print("Door.open()")

  def close(self) -> None:
    print("Door.close()")
