# RMsim test

The objective is to evaluate how different robot morphologies are capable of developing selective mining. To create a first approximation a block wall shall be created. This wall may be composed of different block types (maybe in size and color) to represent different ore types. The hexapod robot must navigate to the wall, select the most profitable mineral, and take it to the processing station. The mineral extraction has to take into account security. Therefore, the maximum forces of the robot must be limited. On the other hand, the selection of points of extraction must ensure the wall and robot integrity.

There are four milestones to past the test:
 - Best mineral selection
 - Best extraction point
 - Robot integrity
 - Mine wall integrity

## Requirements for the simulation

This objectives impose several requirements for the system.

  - Mineral selection: Identify and locate material
 
To extract the optimal material available in the mine, it needs to be identified and located in the system.

Selection among materials could be done as a preliminary approximation with color differentiation as well as pose identification with artificial vision techniques.
  
  - Extraction point: Locate material, structure of the mine and mine integrity

Once the mineral is located in the mine wall, the extraction strategy must be developed to obtain the most quantity of mineral without collapse.

  - Robot integrity during mineral extraction and transportation: Position, force and torque of joints
  
To ensure the robot integrity, control and monitorization of joints must be implemented. This could be done by actuating and reporting joint position and force and torque sensed. In case of exceeding its mechanical capabilities the operation should be reconfigured.
