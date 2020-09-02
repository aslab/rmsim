#include <string.h>
#include <std_msgs/String.h>
#include <sensor_msgs/JointState.h>

// Gazebo
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo_plugins/gazebo_ros_utils.h>
#include <gazebo/sensors/sensors.hh>
#include <gazebo/common/common.hh>
#include <gazebo/transport/TransportTypes.hh>
#include <gazebo/msgs/MessageTypes.hh>
#include <gazebo/common/Time.hh>


// Boost
#include <boost/thread.hpp>
#include <boost/bind.hpp>

// Include ros dependencies
#include <ros/ros.h>
#include <std_srvs/Empty.h>

// Project dependencies
#include <robominer_plugins/robominer_srv.h>

namespace gazebo
{
class RobominerFaultInjection : public ModelPlugin
{

    private:
	
	    physics::ModelPtr model;
		physics::JointPtr joint;
		ros::NodeHandle nh_;
		ros::ServiceServer drop_leg_service;
		ros::ServiceServer lock_joint_service;
		
	public:
    RobominerFaultInjection() : nh_("") {
	}
	
	    void Load(physics::ModelPtr _parent, sdf::ElementPtr _sdf){	   
		
			// Make sure the ROS node for Gazebo has already been initialized
			if (!ros::isInitialized()){
				  ROS_FATAL_STREAM("A ROS node for Gazebo has not been initialized, unable to load plugin. "
					<< "Load the Gazebo system plugin 'libgazebo_ros_api_plugin.so' in the gazebo_ros package)");
				  return;
			}
			
			ROS_WARN("Plugin robominer_fault_injection iniciado");

			this->model = _parent;
			this->drop_leg_service = this->nh_.advertiseService("drop_leg", &RobominerFaultInjection::DetachJoint, this);	  
			this->lock_joint_service = this->nh_.advertiseService("lock_joint", &RobominerFaultInjection::LockJoint, this);	  
		}	
		
		//bool DetachJoint(std_srvs::Empty::Request& req, std_srvs::Empty::Response& res){		
		bool DetachJoint(robominer_plugins::robominer_srv::Request& req, robominer_plugins::robominer_srv::Response& res){
			ROS_INFO_NAMED("model_detaching","Detaching leg");
			// Get the joint and detach it
			this->model->GetJoint(req.joint_id)->Detach();
			return true;
		}
		bool LockJoint(robominer_plugins::robominer_srv::Request& req, robominer_plugins::robominer_srv::Response& res){
			ROS_INFO_NAMED("joint_locking","Locking joint");
			// Get the current joint position
			joint = this->model->GetJoint(req.joint_id);
			joint->SetUpperLimit(0, joint->Position(0));
			joint->SetLowerLimit(0, joint->Position(0));
			return true;
		}
			
};	
	
  // Register this plugin with the simulator
  GZ_REGISTER_MODEL_PLUGIN(RobominerFaultInjection)  
}
		