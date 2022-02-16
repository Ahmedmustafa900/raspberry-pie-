# Please note that this is a fake camera, it will just 
# yield the images 1.jpg, 2.jpg, 3.jg and 4.jpg. It is
# just for testing purposes. You should actually use the
# picamera module and implement the get_frame properly  

from time import time
import os, sys
import glob
import cv2

class Camera(object):
    def __init__(self):
        directory = os.path.join(os.path.dirname(__file__), 'test_frames')
        self.images = [cv2.imread(file) for file in glob.glob('E:/RASP/wise2020groupg/task3_opencv_control/test_frames/*.jpg')]
        #self.test_frames_name = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
        #self.frames = [open(os.path.join(directory, f), 'rb').read() for f in self.test_frames_name]

    def get_frame(self):
        random_index = int(time()) % 4
        #return self.images[1]

        #print('Frame', self.test_frames_name[random_index])
        #return self.frames[random_index]
        return self.images[random_index]