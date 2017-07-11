#!/usr/bin/python

from RPi import GPIO
from time import sleep

pulse = 2
check_pin = 21
check_relay = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(check_pin,GPIO.IN)
GPIO.setup(pulse,GPIO.OUT, initial=0)
GPIO.setup(check_relay,GPIO.OUT, initial=0)

def connect():

        current_state = GPIO.input(check_pin)

        if current_state == True:
                GPIO.output(check_relay,0)
        else:
                GPIO.output(check_relay,1)

        sleep(0.5)

        if current_state != GPIO.input(check_pin):
                print "Already connected..."
                GPIO.output(check_relay,1)
        else:
                print "Connecting..."
                while current_state == GPIO.input(check_pin):
                        for x in range(4):
                                GPIO.output(pulse,1)
                                sleep(0.05)
                                GPIO.output(pulse,0)
                                sleep(0.05)
                        sleep(0.2)
                        if current_state == True:
                                GPIO.output(check_relay,0)
                        else:
                                GPIO.output(check_relay,1)
                print "Relay board active!"
                GPIO.output(check_relay,1)

def disconnect():

        current_state = GPIO.input(check_pin)

        if current_state == True:
                GPIO.output(check_relay,0)
        else:
                GPIO.output(check_relay,1)

        sleep(0.5)

        if current_state == GPIO.input(check_pin):
                print "Already disconnected..."
        else:
                print "Disconnecting..."
                while current_state == True:
                        GPIO.output(check_relay,0)
                        current_state = GPIO.input(check_pin)
                        for x in range(4):
                                GPIO.output(pulse,1)
                                sleep(0.05)
                                GPIO.output(pulse,0)
                                sleep(0.05)
                        sleep(0.2)
                        GPIO.output(check_relay,1)
                print "Relay board deactivated!"

try:

        while True:
                input = raw_input("connect/disconnect (d/c): ")

                if input == "c":
                        connect()

                if input == "d":
                        disconnect()

                sleep(0.2)

except KeyboardInterrupt:
    print "  Quit"
    GPIO.cleanup()