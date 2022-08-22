#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import csv
import time
import sys

time_rn = time.time()
i = 0
x = []

csv_name = '/home/shreya/catkin_ws/src/DNT_IMU_9DOF/data/imu/imu_raw_'+str(time_rn)+'.csv'

with open(csv_name, 'a') as f:
     writer = csv.writer(f)
     writer.writerow(["Time","Acel X","Acel Y","Acel z","Gyro X","Gyro Y","Gyro Z"])
f.close()


def callback(data):  
     s=str(data.data)
     l=[]
     global i, x, csv_name
     l.append(time.time())
     l.append(s[s.rfind("A")+1:s.rfind("B")])
     l.append(s[s.rfind("B")+1:s.rfind("C")])
     l.append(s[s.rfind("C")+1:s.rfind("D")])
     l.append(s[s.rfind("D")+1:s.rfind("E")])   
     l.append(s[s.rfind("E")+1:s.rfind("F")])   
     l.append(s[s.rfind("F")+1:s.rfind("G")]) 
     print(i,l)
     x.append(l)
     i=i+1
     with open(csv_name, 'a') as f_object:
          writer = csv.writer(f_object)
          writer.writerow(l)
     f_object.close

def listener():
     global csv_name
     print(csv_name)
     rospy.init_node('Filtered_IMU', anonymous=True)

     rospy.Subscriber("imu_raw", String, callback)

     # spin() simply keeps python from exiting until this node is stopped
     rospy.spin()

if __name__ == '__main__':
     listener()