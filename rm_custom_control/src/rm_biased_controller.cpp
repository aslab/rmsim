/*
#include <control_msgs/JointControllerState.h>
#include <control_msgs/JointControllerState.h>
#include <control_toolbox/pid.h>
#include <controller_interface/controller.h>
#include <hardware_interface/joint_command_interface.h>
#include <memory>
#include <realtime_tools/realtime_buffer.h>
#include <realtime_tools/realtime_publisher.h>
#include <ros/node_handle.h>
#include <std_msgs/Float64.h>
#include <urdf/model.h>
*/
#include <effort_controllers/joint_position_controller.h>
#include <angles/angles.h>
#include <pluginlib/class_list_macros.hpp>
#include <stdlib.h>
#include <math.h>
// Include ros dependencies
#include <ros/ros.h>
#include <std_srvs/Empty.h>
/*
// Gazebo
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo_plugins/gazebo_ros_utils.h>
*/

namespace rm_biased_controller_ns {
	
	class RMJointPositionController: public controller_interface::Controller<hardware_interface::EffortJointInterface>
	{

		private:
		  int loop_count_;
		  control_toolbox::Pid pid_controller_;       /**< Internal PID controller. */

		  std::unique_ptr<
			realtime_tools::RealtimePublisher<
			  control_msgs::JointControllerState> > controller_state_publisher_ ;

		  ros::Subscriber sub_command_;

		  //char* fault_flag;

		public:
			/*	
		    //Para el servicio del fallo
			bool SetBias(std_srvs::Empty::Request& req, std_srvs::Empty::Response& res){
				ROS_INFO_NAMED("setting_bias","Setting bias to joint");
				fault_flag = true;
				return true;
			}
			
			void start(int argc, char **argv)
			{
			
				// Make sure the ROS node for Gazebo has already been initialized
				if (!ros::isInitialized()){
					  ROS_FATAL_STREAM("A ROS node for Gazebo has not been initialized, unable to load plugin. "
						<< "Load the Gazebo system plugin 'libgazebo_ros_api_plugin.so' in the gazebo_ros package)");
					  return;
				}			
			
  				ros::init(argc, argv, "set_joint_bias_server");
		  		ros::NodeHandle nh_;
			    ros::ServiceServer set_joint_bias = nh_.advertiseService("joint_bias", &RMJointPositionController::SetBias, this);
				
				ROS_WARN("Plugin joint_bias iniciado");
				//set_joint_bias = nh_.advertiseService("joint_bias", &RMJointPositionController::SetBias, this);	
 				ros::spin();

			}
			*/
			  /**
			   * \brief Store position and velocity command in struct to allow easier realtime buffer usage
			   */
			  struct Commands
			  {
				double position_; // Last commanded position
				double velocity_; // Last commanded velocity
				bool has_velocity_; // false if no velocity command has been specified
			  };

			  RMJointPositionController()
				: loop_count_(0)
				{}
			  ~RMJointPositionController()
			  {
				 sub_command_.shutdown();
			  }


			//bool RMJointPositionController::init(hardware_interface::EffortJointInterface *robot, ros::NodeHandle &n)
			bool init(hardware_interface::EffortJointInterface *robot, ros::NodeHandle &n)
			{
				 // Get joint name from parameter server
				 std::string joint_name;
				 if (!n.getParam("joint", joint_name))
				 {
				   ROS_ERROR("No joint given (namespace: %s)", n.getNamespace().c_str());
				   return false;
				 }

				 // Load PID Controller using gains set on parameter server
				 if (!pid_controller_.init(ros::NodeHandle(n, "pid")))
				   return false;

				 // Start realtime state publisher
				 controller_state_publisher_.reset(
				   new realtime_tools::RealtimePublisher<control_msgs::JointControllerState>(n, "state", 1));

				 // Start command subscriber
				 sub_command_ = n.subscribe<std_msgs::Float64>("command", 1, &RMJointPositionController::setCommandCB, this);

				 // Get joint handle from hardware interface
				 joint_ = robot->getHandle(joint_name);

				 // Get URDF info about joint
				 urdf::Model urdf;
				 if (!urdf.initParamWithNodeHandle("robot_description", n))
				 {
				   ROS_ERROR("Failed to parse urdf file");
				   return false;
				 }
				 joint_urdf_ = urdf.getJoint(joint_name);
				 if (!joint_urdf_)
				 {
				   ROS_ERROR("Could not find joint '%s' in urdf", joint_name.c_str());
				   return false;
				 }

				 return true;
			}

			//void RMJointPositionController::setGains(const double &p, const double &i, const double &d, const double &i_max, const double &i_min, const bool &antiwindup)
			void setGains(const double &p, const double &i, const double &d, const double &i_max, const double &i_min, const bool &antiwindup)
			{
				pid_controller_.setGains(p,i,d,i_max,i_min,antiwindup);
			}

			//void RMJointPositionController::getGains(double &p, double &i, double &d, double &i_max, double &i_min, bool &antiwindup)
			void getGains(double &p, double &i, double &d, double &i_max, double &i_min, bool &antiwindup)
			{
				pid_controller_.getGains(p,i,d,i_max,i_min,antiwindup);
			}

			//void RMJointPositionController::getGains(double &p, double &i, double &d, double &i_max, double &i_min)
			void getGains(double &p, double &i, double &d, double &i_max, double &i_min)
			{
				 bool dummy;
				 pid_controller_.getGains(p,i,d,i_max,i_min,dummy);
			}

			//void RMJointPositionController::printDebug()
			void printDebug()
			{
				 pid_controller_.printValues();
			}

			//std::string RMJointPositionController::getJointName()
			std::string getJointName()
			{
				 return joint_.getName();
			}

			//double RMJointPositionController::getPosition()
			double getPosition()
			{
			 return joint_.getPosition();
			}

			// Set the joint position command
			//void RMJointPositionController::setCommand(double pos_command)
			void setCommand(double pos_command)
			{
				 command_struct_.position_ = pos_command;
				 command_struct_.has_velocity_ = false; // Flag to ignore the velocity command since our setCommand method did not include it

				 // the writeFromNonRT can be used in RT, if you have the guarantee that
				 //  * no non-rt thread is calling the same function (we're not subscribing to ros callbacks)
				 //  * there is only one single rt thread
				 command_.writeFromNonRT(command_struct_);
			}

			// Set the joint position command with a velocity command as well
			//void RMJointPositionController::setCommand(double pos_command, double vel_command)
			void setCommand(double pos_command, double vel_command)
			{
				 command_struct_.position_ = pos_command;
				 command_struct_.velocity_ = vel_command;
				 command_struct_.has_velocity_ = true;

				 command_.writeFromNonRT(command_struct_);
			}

			//void RMJointPositionController::starting(const ros::Time& time)
			void starting(const ros::Time& time)
			{
				 double pos_command = joint_.getPosition();

				 // Make sure joint is within limits if applicable
				 enforceJointLimits(pos_command);
				 command_struct_.position_ = pos_command;				 
				 command_struct_.has_velocity_ = false;

				 command_.initRT(command_struct_);

				 pid_controller_.reset();
			}

			//void RMJointPositionController::update(const ros::Time& time, const ros::Duration& period)
			void update(const ros::Time& time, const ros::Duration& period)
			{
				 command_struct_ = *(command_.readFromRT());
				 double command_position = command_struct_.position_ - M_PI/4; // 0.7853981634;
				 double command_velocity = command_struct_.velocity_;
				 bool has_velocity_ =  command_struct_.has_velocity_;

				 double error, vel_error;
				 double commanded_effort;

				 double current_position = joint_.getPosition();

				 // Make sure joint is within limits if applicable
				 enforceJointLimits(command_position);

				 // Compute position error
				 if (joint_urdf_->type == urdf::Joint::REVOLUTE)
				 {
				  angles::shortest_angular_distance_with_limits(
					 current_position,
					 command_position,
					 joint_urdf_->limits->lower,
					 joint_urdf_->limits->upper,
					 error);
				 }
				 else if (joint_urdf_->type == urdf::Joint::CONTINUOUS)
				 {
				   error = angles::shortest_angular_distance(current_position, command_position);
				 }
				 else //prismatic
				 {
				   error = command_position - current_position;
				 }

				 // Decide which of the two PID computeCommand() methods to call
				 if (has_velocity_)
				 {
				   // Compute velocity error if a non-zero velocity command was given
				   vel_error = command_velocity - joint_.getVelocity();

				   // Set the PID error and compute the PID command with nonuniform
				   // time step size. This also allows the user to pass in a precomputed derivative error.
				   commanded_effort = pid_controller_.computeCommand(error, vel_error, period);
				 }
				 else
				 {
				   // Set the PID error and compute the PID command with nonuniform
				   // time step size.
				   commanded_effort = pid_controller_.computeCommand(error, period);
				 }

				 joint_.setCommand(commanded_effort);

				 // publish state
				 if (loop_count_ % 10 == 0)
				 {
				   if(controller_state_publisher_ && controller_state_publisher_->trylock())
				   {
					 controller_state_publisher_->msg_.header.stamp = time;
					 controller_state_publisher_->msg_.set_point = command_position;
					 controller_state_publisher_->msg_.process_value = current_position;
					 controller_state_publisher_->msg_.process_value_dot = joint_.getVelocity();
					 controller_state_publisher_->msg_.error = error;
					 controller_state_publisher_->msg_.time_step = period.toSec();
					 controller_state_publisher_->msg_.command = commanded_effort;

					 double dummy;
					 bool antiwindup;
					 getGains(controller_state_publisher_->msg_.p,
					   controller_state_publisher_->msg_.i,
					   controller_state_publisher_->msg_.d,
					   controller_state_publisher_->msg_.i_clamp,
					   dummy,
					   antiwindup);
					 controller_state_publisher_->msg_.antiwindup = static_cast<char>(antiwindup);
					 controller_state_publisher_->unlockAndPublish();
				   }
				 }
				 loop_count_++;
			}

			//void RMJointPositionController::setCommandCB(const std_msgs::Float64ConstPtr& msg)
			void setCommandCB(const std_msgs::Float64ConstPtr& msg)
			{
				setCommand(msg->data);
			}

			// Note: we may want to remove this function once issue https://github.com/ros/angles/issues/2 is resolved
			//void RMJointPositionController::enforceJointLimits(double &command)
			void enforceJointLimits(double &command)
			{
				 // Check that this joint has applicable limits
				 if (joint_urdf_->type == urdf::Joint::REVOLUTE || joint_urdf_->type == urdf::Joint::PRISMATIC)
				 {
				   if( command > joint_urdf_->limits->upper ) // above upper limnit
				   {
					 command = joint_urdf_->limits->upper;
				   }
				   else if( command < joint_urdf_->limits->lower ) // below lower limit
				   {
					 command = joint_urdf_->limits->lower;
				   }
			 }
			}	

			  hardware_interface::JointHandle joint_;
			  urdf::JointConstSharedPtr joint_urdf_;
			  realtime_tools::RealtimeBuffer<Commands> command_;
			  Commands command_struct_; // pre-allocated memory that is re-used to set the realtime buffer

		};

} // namespace

PLUGINLIB_EXPORT_CLASS( rm_biased_controller_ns::RMJointPositionController, controller_interface::ControllerBase)
/*
// Register this plugin with the simulator
GZ_REGISTER_MODEL_PLUGIN(RMJointPositionController)  
*/
	