#!/usr/bin/env python
import sys
import rospy

from moveit_commander import (
    roscpp_initialize,
    roscpp_shutdown,
)

from move_arm import MoveArm
from move_targets import MoveTargets

if __name__ == '__main__':
    roscpp_initialize(sys.argv)
    rospy.init_node('move_combined')
    move = MoveArm()
    move_targets = MoveTargets()
    try:
        while not rospy.is_shutdown():
            move.fold_arm()
            move_targets.add_target((-2.825, 3.758))
            move_targets.move()
            move.extend_arm()
            rospy.sleep(1.0)
            move.fold_arm()
            move_targets.add_target((0.045, -0.037))
            move_targets.move()
            move.extend_arm()
            rospy.sleep(1.0)
    except KeyboardInterrupt:
        pass
    roscpp_shutdown()
