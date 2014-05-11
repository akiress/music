import RPi.GPIO as GPIO
import os
import time

class ButtonMatrix():
    BUTTON_MATRIX = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    ROW = [22,27,18,17]
    COLUMN = [10,9,11,23]
    
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
    
    def buttonPressed(self):
        for i in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[i], GPIO.OUT)
            GPIO.output(self.COLUMN[i], GPIO.LOW)
        
        for i in range(len(self.ROW)):
            GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        row_value = None
        for i in range(len(self.ROW)):
            gpio_read_value = GPIO.input(self.ROW[i])
            if gpio_read_value == 0:
                row_value = i
                
        if row_value < 0 or row_value > 3:
            self.exit()
            return
        
        for i in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
        GPIO.setup(self.ROW[row_value], GPIO.OUT)
        GPIO.output(self.ROW[row_value], GPIO.HIGH)

        column_value = None
        for i in range(len(self.COLUMN)):
            gpio_read_value = GPIO.input(self.COLUMN[i])
            if gpio_read_value == 1:
                column_value=i
                
        if column_value < 0 or column_value > 3:
            self.exit()
            return

        self.exit()
        return self.BUTTON_MATRIX[row_value][column_value]
        
    def exit(self):
        for i in range(len(self.ROW)):
                GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
if __name__ == '__main__':
    Button = ButtonMatrix()
    while True:
        button_value = Button.buttonPressed()
        if button_value is not None:
            if button_value == 15 or button_value == 16 or button_value == 13:
                os.system("echo ' %d;' | pdsend 3000" % (button_value))
                time.sleep(0.05)
            else:
                os.system("echo ' %d;' | pdsend 3000" % (button_value))
                time.sleep(0.25)
        button_value = None
