#!/usr/bin/env python
import rospy
import sys
from PyQt5 import uic
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import rviz


class MyWindow(object):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('new.ui', self)
        # self.addWiz(myviz)
        # QWidget.__init__(self)
        '''
        self.frame = rviz.VisualizationFrame()
        self.frame.setSplashPath( "" )
        self.frame.initialize()
            reader = rviz.YamlConfigReader()
            config = rviz.Config()
            reader.readFile( config, "trust_new.rviz" )
            self.frame.load( config )
            self.frame.setMenuBar( None )
            self.frame.setStatusBar( None )
            self.frame.setHideButtonVisibility( False )
        ## any changes in an rviz instance.
            self.manager = self.frame.getManager()
        ## Since the config file is part of the source code for this
        ## example, we know that the first display in the list is the
        ## grid we want to control.  Here we just save a reference to
        ## it for later.
            self.grid_display = self.manager.getRootDisplayGroup().getDisplayAt( 0 )


        ## Here we create the layout and other widgets in the usual Qt way.

            self.map_layout.addWidget( self.frame )        		
            self.frame.show()
            '''

        self.image_data = None
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/image_raw", Image, self.image_callback)
        self.map_widget = MyViz()
        self.gridLayout.addWidget(self.map_widget)

        self.publisher = rospy.Publisher('/chatter', String, queue_size=1)
        self.pause_button.clicked.connect(self.button_click_listener)
        # self.show()
        rospy.loginfo("Object initialised..")
        self.timer = QTimer()
        self.timer.setInterval(100)  # ms
        self.timer.timeout.connect(self.update_gui)
        self.timer.start()
        rospy.loginfo("Here")

    def button_click_listener(self):
        rospy.loginfo("Button pressed..")
        msg = String()
        msg.data = "Hello"
        self.publisher.publish(msg)

    def image_callback(self, data):
        self.image_data = data

    def update_gui(self):
        try:
            # rospy.loginfo("calling update_gui..")
            cv_image = self.bridge.imgmsg_to_cv2(self.image_data, "bgr8")
            # cv2.imshow("Image window", cv_image)
            height, width, channel = cv_image.shape
            bytesPerLine = 3 * width
            qImg = QImage(cv_image.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.video_stream.setPixmap(QPixmap(qImg))

        except CvBridgeError as e:
            print(e)

    '''
    def addWiz(self, myviz):
            self.map_layout.addWidget(myviz)
            myviz.show()
            #myviz.setLayout(self.map_layout)
            rospy.loginfo("wiz added!	")
        '''
    '''
    def do_stuff(self):
            try:
                rospy.loginfo("calling do_stuff..")
                  cv_image = self.bridge.imgmsg_to_cv2(self.image_data, "bgr8")
                  cv2.imshow("Image window", cv_image)	
                  height, width, channel = cv_image.shape
            bytesPerLine = 3 * width
            qImg = QtGui.QImage(cv_image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        #pixmap = self.label.pixmap
            self.label.setPixmap(QtGui.QPixmap(qImg))
            #app.exec_()
            except CvBridgeError as e:
                  print(e)


    def run(self):
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.do_stuff()
            r.sleep()
        sys.exit(0)
    '''


class MyViz(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.frame = rviz.VisualizationFrame()
        self.frame.setSplashPath("")
        self.frame.initialize()
        reader = rviz.YamlConfigReader()
        config = rviz.Config()
        reader.readFile(config, "trust_new.rviz")
        self.frame.load(config)
        self.setWindowTitle(config.mapGetChild("Title").getValue())
        self.frame.setMenuBar(None)
        self.frame.setStatusBar(None)
        self.frame.setHideButtonVisibility(False)
        self.manager = self.frame.getManager()
        self.grid_display = self.manager.getRootDisplayGroup().getDisplayAt(0)
        layout = QVBoxLayout()
        layout.addWidget(self.frame)
        self.setLayout(layout)


if __name__ == '__main__':
    rospy.init_node('talker')
    rospy.loginfo("Node initialised")
    app = QApplication(sys.argv)
    # map_viz = MyViz()
    myWindow = MyWindow()
    # myWindow.addWiz(map_viz)
    # map_viz.resize( 500, 500 )
    # map_viz.show()
    myWindow.show()
    app.exec_()
# myWindow.run()
# rospy.loginfo("run called")
# app.exec_()
# print "Hello"
# while not rospy.is_shutdown():
# print "excuting"
# rospy.spin()