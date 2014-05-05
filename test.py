#!/usr/bin/python

import RPi.GPIO as GPIO
import time     

GPIO.setmode(GPIO.BCM)

# CONSTANTS 
KEYPAD     = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

COLUMN = [17,18,27,22]
ROW = [2,3,4,23]

rowVal = -1
colVal = -1


def setInterrupts(self):
    #set the first row as output low
    #only first one needed as it will ground to all columns
    for r in range(len(ROW)):
        GPIO.setup(ROW[r], GPIO.OUT)
        GPIO.output(ROW[r], GPIO.LOW)

    #set columns as inputs and attach interrupt handlers on rising edge
    for c in range(len(COLUMN)):
        GPIO.setup(COLUMN[c], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(COLUMN[c], GPIO.FALLING, bouncetime=400, callback=__colRise)


def cleanup(self):
    GPIO.cleanup()
    print("Cleanup done!")


def main():
    for c in range(len(COLUMN)):
        if channel == COLUMN[c]:
            colVal = c
    print("ColVal: " + str(colVal))

    try:
        for r in range(len(ROW)):
            GPIO.setup(ROW[r], GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.setup(channel, GPIO.OUT)
        GPIO.output(channel, GPIO.LOW)

        for r in range(len(ROW)):
            print(ROW)
            print(ROW[r])
            print("r: " + str(r))
            tmpRead = GPIO.input(ROW[r])
            print("tmpRead: " + str(tmpRead))
            if tmpRead == 0:
                rowVal = r

        print("RowVal: " + str(rowVal))

        if rowVal >= 0 and rowVal <= 3:
            print("Key: " + str(KEYPAD[rowVal][colVal]))
        else:
            print("Invalid Row!")
    except ValueError:
        print("Invalid Col!")

    #re-enable interrupts
    setInterrupts()

if __name__ == '__main__':
    try:
        while True:
            main()
            time.sleep(1)

    except KeyboardInterrupt:
        cleanup()