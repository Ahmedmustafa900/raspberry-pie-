import RPi.GPIO as GPIO # For testing in Raspberry Pi
import time
import numpy as np

class SensorController:

  def __init__(self):
    self.PIN_TRIGGER = 18 # do not change
    self.PIN_ECHO = 24 # do not change
    self.distance = None
    print('Sensor controller initiated')

  def track_rod(self):
    print ("----------Distance Measurement----------")

    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_TRIGGER,GPIO.OUT) #we ping this pin to start the sensor
        GPIO.setup(self.PIN_ECHO,GPIO.IN) #expecting data from ECHO pin

        GPIO.output(self.PIN_TRIGGER, GPIO.LOW) #to allow sensor to settle

        print ("Waiting For Sensor To Settle")
        time.sleep(2)
        dist = []
        for i in range (50):
            #print("loop is working")

            GPIO.output(self.PIN_TRIGGER, GPIO.HIGH) #triggers the distance sensor

            time.sleep(0.00001) #giving distance sensor required pulse to trigger it
            GPIO.output(self.PIN_TRIGGER, GPIO.LOW)
            pulse_start_time = time.time()
            pulse_end_time = time.time()

            while GPIO.input(self.PIN_ECHO) == 0:
                pulse_start_time = time.time()
            while GPIO.input(self.PIN_ECHO) == 1:
                pulse_end_time = time.time()

            pulse_duration = pulse_end_time - pulse_start_time
            dist_inst=pulse_duration*17150
            #pulse_duration = pulse_start_time
            print("distance received ", (pulse_duration*17150))
            dist.append(dist_inst)
            print("array value ", dist[i])
            print("iteration number:", (i+1))

        last10values = dist[-10:]
        print("last10values ", last10values)
        if (np.std(last10values) <= 0.05):
            self.distance = np.mean(last10values)
            print ("Mean:", self.distance)
        else:
            self.distance = np.median(dist)
            print ("Median:", self.distance)

    finally:
        GPIO.cleanup()

    print('Monitoring')


  def get_distance(self):
    return self.distance
