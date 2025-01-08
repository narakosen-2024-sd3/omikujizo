from typing import Protocol

from ..servo_motor_degree import ServoMotorDegree
from ..servo_motor_rpm import ServoMotorRpm


class IServoMotor[ANGLE_TYPE: ServoMotorDegree, SPEED_TYPE: ServoMotorRpm](Protocol):
  async def move_to(self, angle: ANGLE_TYPE, speed: SPEED_TYPE) -> None:
    raise NotImplementedError()
