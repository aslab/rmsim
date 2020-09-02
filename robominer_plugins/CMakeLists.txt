cmake_minimum_required(VERSION 2.8.3)
project(robominer_plugins)

## Add support for C++11, supported in ROS Kinetic and newer
add_definitions(-std=c++11)

# Load catkin and all dependencies required for this package
find_package(catkin REQUIRED COMPONENTS 
  roscpp 
  gazebo_ros 
  std_msgs
  message_generation
)


add_service_files(
  FILES
  robominer_srv.srv
)

generate_messages(
    DEPENDENCIES
    std_msgs
)

# Depend on system install of Gazebo
find_package(gazebo REQUIRED
             COMPONENTS
             message_generation
             std_msgs)

link_directories(${GAZEBO_LIBRARY_DIRS})
include_directories(${Boost_INCLUDE_DIR} ${catkin_INCLUDE_DIRS} ${GAZEBO_INCLUDE_DIRS})

# For robominer_fault_injection_plugin plugin
add_library(robominer_fault_injection_plugin src/robominer_fault_injection.cpp)
target_link_libraries(robominer_fault_injection_plugin ${catkin_LIBRARIES} ${GAZEBO_LIBRARIES})

# For camera_publisher_plugin plugin
add_library(camera_publisher_plugin src/camera_publisher.cpp)
target_link_libraries(camera_publisher_plugin ${catkin_LIBRARIES} ${GAZEBO_LIBRARIES})

catkin_package(
  DEPENDS 
    roscpp 
    gazebo_ros 
	message_runtime 
	std_msgs
)