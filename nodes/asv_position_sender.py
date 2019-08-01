#!/usr/bin/env python
import socket
import rospy

from sensor_msgs.msg import NavSatFix
from marine_msgs.msg import NavEulerStamped

position = None
heading = None
last_send_time = None

out_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

def send_data():
    global last_send_time
    if position is not None and heading is not None:
        now = rospy.get_rostime()
        if last_send_time is None or now - last_send_time > rospy.Duration(0.25):
            out_string = str(position.latitude) + ' ' + str(position.longitude) + ' ' + str(heading.orientation.heading) +'\n'
            #print out_string
            out_socket.sendto(out_string, ('10.1.90.40',13281))            
            #out_socket.sendto(out_string, ('10.1.90.40',13281))            
            last_send_time = now

def position_callback(data):
    global position
    position = data
    send_data();

def heading_callback(data):
    global heading
    heading = data

def asv_position_sender():
    rospy.init_node('asv_position_sender', anonymous=False)
    rospy.Subscriber('/udp/posmv/position', NavSatFix, position_callback)
    rospy.Subscriber('/udp/posmv/orientation', NavEulerStamped, heading_callback)
    rospy.spin()
    
if __name__ == '__main__':
    asv_position_sender()

