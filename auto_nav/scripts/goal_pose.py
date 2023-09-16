#!/usr/bin/env python3

import rospy
import actionlib # service reqd to send msgs to move_base
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# callback function
def active_cb(extra):
    rospy.loginfo("goal pose bwing processed")

def feedback_cb(feeedback):
    rospy.loginfo("current location: "+str(feeedback))

def done_cb(status, result):
    if status == 3:
        rospy.loginfo("goal reached")
    if status == 2 or status == 8:
        rospy.loginfo("goal cancelled")
    if status == 4:
        rospy.loginfo("goal aborted")

rospy.init_node("goal_pose")

navclient = actionlib.SimpleActionClient("move_base", MoveBaseAction) #client for a server #SimpleActionClient is inbuilt func of actionlib, service is move_base and message is MoveBaseAction
navclient.wait_for_server()

# example of nav goal
goal = MoveBaseGoal()
goal.target_pose.header.frame_id = "map"
goal.target_pose.header.stamp = rospy.Time.now()

goal.target_pose.pose.position.x = -2.16
goal.target_pose.pose.position.y = 0.764
goal.target_pose.pose.position.z = 0.0
goal.target_pose.pose.orientation.x = 0.0
goal.target_pose.pose.orientation.y = 0.0
goal.target_pose.pose.orientation.z = 0.662
goal.target_pose.pose.orientation.w = 0.750

navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
finsihed = navclient.wait_for_result()

if not finsihed:
    rospy.logerr("action server not available")
else:
    rospy.loginfo( navclient.get_result())