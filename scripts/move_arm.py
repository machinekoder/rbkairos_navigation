#!/usr/bin/env python
import sys
import rospy
from moveit_commander import (
    RobotCommander,
    roscpp_initialize,
    roscpp_shutdown,
    MoveGroupCommander,
)

class MoveArm(object):
    def __init__(self):
        self._robot = RobotCommander('/robot_description')
        self._manipulator = MoveGroupCommander('arm')
    
    def fold_arm(self):
        self._manipulator.set_named_target('start')
        self._manipulator.go()
    
    def extend_arm(self):
        self._manipulator.set_named_target('all_forward')
        self._manipulator.go()

    def stop(self):
        pass

if __name__ == '__main__':
    roscpp_initialize(sys.argv)
    rospy.init_node('move_robot')
    move = MoveArm()
    move.fold_arm()
    roscpp_shutdown()