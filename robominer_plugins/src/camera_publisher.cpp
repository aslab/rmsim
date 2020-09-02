#include <gazebo/gui/GuiIface.hh>
#include <gazebo/rendering/rendering.hh>
#include <gazebo/gazebo.hh>
#include "gazebo/transport/transport.hh"
#include "gazebo/plugins/CameraPlugin.hh"
#include "gazebo/common/Plugin.hh"
#include "gazebo/sensors/CameraSensor.hh"
#include "gazebo/rendering/Camera.hh"
#include <string>
#include <iostream>
#include <sstream>

// Include ros dependencies
#include <ros/ros.h>

typedef const boost::shared_ptr<gazebo::msgs::Image const> ConstImagePtr;

#define COUT_PREFIX "\033[1;33m" << "[CameraPublisher] " << "\033[0m"
using namespace gazebo;
using namespace std;

class CameraDump: public CameraPlugin
{
//記得打virtual啊 否則不會invoke這函數
public:virtual ~CameraDump()
{
	cout<<COUT_PREFIX<<"in destructor"<<endl;
}
public:void Load(sensors::SensorPtr _parent, sdf::ElementPtr _sdf)
{

	// Make sure the ROS node for Gazebo has already been initialized
	if (!ros::isInitialized()){
		  ROS_FATAL_STREAM("A ROS node for Gazebo has not been initialized, unable to load plugin. "
			<< "Load the Gazebo system plugin 'libgazebo_ros_api_plugin.so' in the gazebo_ros package)");
		  return;
	}

	ROS_WARN("Plugin camera_publisher iniciado");
			
	node = transport::NodePtr(new transport::Node());
	node->Init("default");
	publisher = node->Advertise<gazebo::msgs::Image>("~/fake_streaming");
	CameraPlugin::Load(_parent, _sdf);
	this->parentSensor->SetActive(true);
}

public: void OnNewFrame(const unsigned char *_image,  unsigned int _width, unsigned int _height, unsigned int _depth, const std::string &_format)
  {

	// Create an image message

	msgs::Image fakeMsg;
	_image_ptr=_image;
	fakeMsg.set_width(_width);
	fakeMsg.set_height(_height);
	fakeMsg.set_pixel_format((common::Image::PixelFormat)3);//RGB_INT8,
	fakeMsg.set_data(_image_ptr, _width*_height*3);
	fakeMsg.set_step(0);//不太懂這參數是啥,亂設根本沒差
	publisher->Publish(fakeMsg);



}



const unsigned char *_image_ptr;
gazebo::transport::NodePtr node;
gazebo::transport::PublisherPtr publisher;

};

GZ_REGISTER_SENSOR_PLUGIN(CameraDump)

