# cmake_minimum_required(VERSION 3.0.2)
cmake_minimum_required(VERSION 2.8.3)
project(smarp_msgs)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  rospy
  std_msgs
)

## Generate messages in the 'msg' folder
# add_message_files(
#   FILES
#   Message1.msg
#   Message2.msg
# )

add_message_files(
  # DIRECTORY msg 
  FILES
  camInfo.msg
  recogObj.msg
  objInfo.msg
  objectStatus.msg
  lidarStatus.msg
)

## System dependencies are found with CMake's conventions
## Generate services in the 'srv' folder
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES smarp_msgs
  CATKIN_DEPENDS message_runtime rospy std_msgs
#  CATKIN_DEPENDS message_generation rospy std_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(
## include
#  ${catkin_INCLUDE_DIRS}
# )


