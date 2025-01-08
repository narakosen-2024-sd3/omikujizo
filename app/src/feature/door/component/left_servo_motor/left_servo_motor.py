from src.component.motor.servo.servo_motor import ServoMotor

from .left_servo_motor_degree import LeftServoMotorDegree
from .left_servo_motor_rpm import LeftServoMotorRpm


class LeftServoMotor(ServoMotor[LeftServoMotorDegree, LeftServoMotorRpm]):
  pass
