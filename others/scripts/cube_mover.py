import sys
import copy
import rospy
import moveit_commander
from math import pi
from moveit_commander.conversions import pose_to_list
from moveit_commander.exception import MoveItCommanderException
import time

moveit_commander.roscpp_initialize(sys.argv)
#rospy.init_node('abb_mover',anonymous=False)
robot = moveit_commander.RobotCommander()





def go_to_joint_state(joint_g):

    group_name = "rot1"
    group = moveit_commander.MoveGroupCommander(group_name)

    joint_goal = group.get_current_joint_values()
    #print(joint_goal)
    
    joint_goal[0] = joint_g[0] #(-7pi/8 to 7pi/8)
    joint_goal[1] = joint_g[1] #(pi/4 to -pi/2)
    joint_goal[2] = joint_g[2] #(-pi/2 to (pi/2 - pi/8))(upwards vs downwards)
    joint_goal[3] = joint_g[3] #(-pi/2 to pi/2)
    joint_goal[4] = joint_g[4] #(-5pi/8 to 5pi/8)(upwards vs downwards)
    joint_goal[5] = joint_g[5]  #(-2pi tp 2pi)
    
    #joint_goal = joint_g

    # The go command can be called with joint values, poses, or without any
    # parameters if you have already set the pose or joint target for the group
    print("Moving to: ", joint_goal)
    group.go(joint_goal, wait=True)
  
    # Calling ``stop()`` ensures that there is no residual movement
    group.stop()

    ## END_SUB_TUTORIAL

    # For testing:
    # Note that since this section of code will not be included in the tutorials
    # we use the class variable rather than the copied state variable
    current_joints = group.get_current_joint_values()

  

def mover(joints):
    
  joint_ang = joints  
  try:
    go_to_joint_state(joint_ang)
  except MoveItCommanderException:
    print("Move-it exception raised")
    pass
  except rospy.ROSInterruptException:
    print("ROS interupt called")
    return
  except KeyboardInterrupt:
    return
