#!/usr/bin/env python
import rospy
import actionlib

from collections import deque

from move_base_msgs.msg import MoveBaseAction, MoveBaseActionGoal, MoveBaseGoal
from geometry_msgs.msg import Pose


class MoveTargets(object):
    def __init__(self):
        self._client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
        self._client.wait_for_server()
        self._targets = deque()


    def add_target(self, target):
        self._targets.append(target)

    def move(self):
        if len(self._targets) == 0:
            return False
        target = self._targets.pop()
        goal = MoveBaseGoal()
        pose = Pose()
        pose.position.x = target[0]
        pose.position.y = target[1]
        pose.position.z = 0.0
        pose.orientation.x = 0.0
        pose.orientation.y = 0.0
        pose.orientation.z = 0.0
        pose.orientation.w = 1.0
        goal.target_pose.pose = pose
        goal.target_pose.header.frame_id = 'robot_map'
        self._client.send_goal(goal)
        self._client.wait_for_result()
        res = self._client.get_state()
        return True


if __name__ == "__main__":
    rospy.init_node('move_targets')
    move_targets = MoveTargets()
    while True:
        move_targets.add_target((0.045, -0.037))
        move_targets.add_target((-2.825, 3.758))
        while move_targets.move():
            pass
