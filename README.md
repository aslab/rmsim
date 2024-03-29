# RMsim

The **ROBOMINERS Robot Simulator (RMsim)** is a simulator of autonomous modular robots to be used in the exploration of metacontrol strategies for the improvement of adaptivity and autonomy.

The purpose of the RMsim is the development of a customizable simulation testbed on Gazebo to be used in:

* The design and test of the robot mechanical structure.
* The test of the high-level reconfiguration metacontrollers.

RMsim shall be able to manage different **robot models** set in different **worlds** using different **controlllers**. The controllers themselves are not part of RMsim, but RMThe simulator shall provide a ROS2 API to interact with the virtual robot.

---
## About the robots

The initial target robot is the modular robot ROMERIN developed at the UPM ETSIDI. A second objective is the RM2 ROBOMINERS robot.

### ROMERIN robot

ROMERIN characteristics are the following:

* It has four modules: ODIN, THOR, LOKI and FRIGG.
* 7 controlled degrees of freedom  3-1-3
* All three orientations are reversible and low torque
* Battery and integrated control electronics
* BT-WIFI-CA external communication and a PWM channel
* Internal communication: I2C, 485
* 80cm leg span

M. Hernando, A. Brunete, and E. Gambao. ROMERIN: A modular climber robot for infrastructure inspection. In *Preprints of the 8th IFAC Symposium on Mechatronic Systems (MECHATRONICS 2019)*, pages 1049–1054, Vienna, Austria, Sept. 4-6 2019.

![ROMERIN leg module 3D rendition](https://github.com/aslab/rmsim/blob/master/images/ROMERIN-leg-3D.png)

### RM2 robot

THe RM2 robot is a laboratory robot used to study mining robot modularity inside the ROBOMINERS project.

---
## A Basic Scenario

### Context

Robot modularity. Robot self-assembly. Self-awareness. Self-knowledge. The ASys project. The ROBOMINERS Project.

### Sequence of events

The ROBOMINERS robot is performing the mining operations it was designed to do. The robot loses capability in a leg -e.g. due to an actuator malfunction: The robot is able to perceive this situation and reorganises itself (e.g. changing the gait controller or replacing the leg). The metacontroller drives this process. 

All this happens in the simulation. The metacontroller engineer tests the operation of the metacontroller against the simulation. The simulator is able to perform the simulation (change of physical structure of the robot).


## Implementation

* A ROS2 package.
* A Gazebo model of the robot. 
* A user manual.

***
## About the ROBOMINERS project

[**ROBOMINERS**](http://robominers.eu) is a project funded under the European Union's Research and Innovation programme Horizon 2020 (grant agreement n°820971) within strategic objective to facilitate EU access to mineral raw materials. ROBOMINERS' innovative approach combines the creation of a new mining ecosystem with novel ideas from other sectors, in particular with the inclusion of disruptive concepts from robotics. This is where we focus our work: mining robots that adapt to harsh conditions. 

[Link to ROBOMINERS](http://robominers.eu)

## About Gazebo

Robot simulation is an essential tool in the exploration of robot control strategies. A good simulator makes it possible to evaluate robot designs, test control algorithms, or train ML system using close to reality scenarios. [**Gazebo**](http://gazebosim.org/) is a robot simulator that offers the ability to accurately simulate robots situated in realistic environments. It has a robust physics engine, high-quality graphics, and convenient programmatic and graphical interfaces.

[Link to Gazebosim](http://gazebosim.org/)

## About ROS 2

We use [ROS 2](https://index.ros.org/doc/ros2/) in ROBOMINERS and hence in this work. The Robot Operating System (ROS) is a set of open source software libraries and tools for building robot applications. It provides integration middleware, device drivers and state-of-the-art robot algorithms, and all packaged with powerful developer tools. ROS started in 2007. ROS2 is under current heavy development. The goal of the ROS 2 project is to solve existing limitations of ROS and adapt to changes in the robot and software world, leveraging what is great about ROS.

[Link to ROS 2 docummentation](https://index.ros.org/doc/ros2/)

***

This README.md follows [GitHub Markdown Syntax](https://guides.github.com/features/mastering-markdown/).

Follow [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).

Follow [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)

