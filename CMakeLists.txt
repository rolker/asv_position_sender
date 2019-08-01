cmake_minimum_required(VERSION 2.8.3)
project(asv_position_sender)

find_package(catkin REQUIRED COMPONENTS
  sensor_msgs
  rospy
)

catkin_python_setup()

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES radar_obstacle_detection
#  CATKIN_DEPENDS marine_msgs rospy
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

