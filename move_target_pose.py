#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import geometry_msgs.msg
import utils
from primitive_action import *
from math import pi
from tf.transformations import *




if __name__ == "__main__":
    # Initialize moveit_commander and node
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('d2_move_target_pose', anonymous=False)

    # Get instance from moveit_commander
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()

    # Get group_commander from MoveGroupCommander
    group_name = "panda_arm"
    move_group = moveit_commander.MoveGroupCommander(group_name)


    # Move using target_pose
    pose_goal = geometry_msgs.msg.Pose()

    #Start pose
    pose_goal.position.x = 0.30646574567259716
    pose_goal.position.y = -2.366951358129629e-16
    pose_goal.position.z = 0.5895587217732924




    # #test
    # pose_goal.position.x = 0.3580361640436944
    # pose_goal.position.y = 0.05308103595170339
    # pose_goal.position.z = 0.40148404633838114


    # pose_goal.position.x = 0.0
    # pose_goal.position.y = 0.0
    # pose_goal.position.z = 0.8

    # quat = quaternion_from_euler(-pi/2, 0, 0.0)

    # pose_goal.orientation.x = quat[0]
    # pose_goal.orientation.y = quat[1]
    # pose_goal.orientation.z = quat[2]
    # pose_goal.orientation.w = quat[3]

    #Start pose
    pose_goal.orientation.x = 0.9238761773316531
    pose_goal.orientation.y = -0.3826366288404408
    pose_goal.orientation.z = -0.0023558893585879656
    pose_goal.orientation.w = 0.000975843858378463

    # #test
    # pose_goal.orientation.x = 0.923883641126151
    # pose_goal.orientation.y = -0.3826366288404408
    # pose_goal.orientation.z = -0.004816755330753461
    # pose_goal.orientation.w = 0.002242052004701504

    #1
    # pre_dist_pose = [0, 0, -0.1, 0, 0, 0, 1]
    # pre_pose = utils.concatenate_to_pose(pose_goal, pre_dist_pose)


    move_group.set_pose_target(pose_goal)

    #PrimitiveAction.linear_motion([0, 0, -0.1], True, "eef")

    plan = move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()



    #2
    # plan = move_group.plan(pose_goal)

    # cur_state = move_group.get_current_state()
    # plan = move_group.retime_trajectory(cur_state, plan, 2.0, 1.0)
    # move_group.execute(plan, wait=True)
    # move_group.stop()
    # move_group.clear_pose_targets()
    quit()