import cv2
import numpy as np
import os


class OpenCVController(object):

    def __init__(self):
        self.in_zone = False
        print('OpenCV controller initiated')

    def get_frame(self, camera):
        img = frame = camera.get_frame()


        # Get one image at once
        #img = cv2.imread("2.jpg")
        #cv2.imshow("frame", img)

        # Convert images from BGR to HSV

        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # cv2.imshow("converted",hsv_img)


        # Set range for blue color and
        # define mask

        blue_low = np.array([[100,150,0]])
        blue_upper = np.array([140,255,255])
        blue_mask = cv2.inRange(hsv_img, blue_low, blue_upper)
        # cv2.imshow("Blue Mask", blue_mask)

        # Set range for red color and
        # define mask

        red_low = np.array([0,120,70])
        red_upper = np.array([10,255,255])
        red_mask = cv2.inRange(hsv_img, red_low, red_upper)
        # cv2.imshow("Red Mask",red_mask)

        # Color detection
        kernal = np.ones((5, 5), "uint8")
        #for red color
        red_mask = cv2.dilate(red_mask, kernal)
        res_red = cv2.bitwise_and(img, img, mask=red_mask)
        # for blue color
        blue_mask = cv2.dilate(blue_mask, kernal)
        res_blue = cv2.bitwise_and(img, img, mask=blue_mask)

        # for red color

        #res_red = cv2.bitwise_and(img, img, mask=red_mask)

        # Display the color detected image

        combined = res_blue + res_red
        #contours, hierarchy = cv2.findContours(red_mask,
                                               #cv2.RETR_TREE,
                                               #cv2.CHAIN_APPROX_SIMPLE)
        contours, hierarchy = cv2.findContours(red_mask,
                                               cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)
        #cv2.imshow("combined", combined)
        #contours, hierarchy = cv2.findContours(red_mask,
                                               #cv2.RETR_TREE,
                                              # cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 2500):
             img_Mod1 = cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
             x1, y1, w1, h1= cv2.boundingRect(contour)




            #img_Mod1 = cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
            #x1, y1, w1, h1 = cv2.boundingRect(contours)


        cv2.imshow("img_mod1", img_Mod1)


        contours, hierarchy = cv2.findContours(blue_mask,
                                               cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
           area = cv2.contourArea(contour)
           if (area > 2500):
            img_Mod2 = cv2.drawContours(img, contours, -1, (0,255,0), 2)
            x, y, w, h = cv2.boundingRect(contour)


        cv2.imshow("img_mod2", img_Mod2)

        #img_Mod2 = cv2.drawContours(img, contours, -1, (255, 0, 0), 2)
        #cv2.imshow("img_mod2", img_Mod2)
        #x, y, w, h = cv2.boundingRect(contours)'''


        if (x1<(x+w) and x<(x1+w1)):
            print("Ovelapping")
            self.in_zone = True
        else:
            self.in_zone= False



        #cv2.imshow("img_mod2", img_Mod2)

        print('Monitoring')
        return frame

    def is_in_zone(self):

          return self.in_zone

