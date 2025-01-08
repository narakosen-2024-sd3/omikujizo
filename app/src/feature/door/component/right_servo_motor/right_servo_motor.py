from src.component.motor.servo.servo_motor import ServoMotor

from .right_servo_motor_degree import RightServoMotorDegree
from .right_servo_motor_rpm import RightServoMotorRpm


class RightServoMotor(ServoMotor[RightServoMotorDegree, RightServoMotorRpm]):
  pass
