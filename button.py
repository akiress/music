import RPi.GPIO as GPIO

class ButtonMatrix():
    BUTTON_MATRIX = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    ROW = [22,27,18,17]
    COLUMN = [2,3,4,23]
    
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
    
    def buttonPressed(self):
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.OUT)
            GPIO.output(self.COLUMN[j], GPIO.LOW)
        
        for i in range(len(self.ROW)):
            GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        rowVal = -1
        for i in range(len(self.ROW)):
            tmpRead = GPIO.input(self.ROW[i])
            if tmpRead == 0:
                rowVal = i
                
        if rowVal < 0 or rowVal > 3:
            self.exit()
            return
        
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
        GPIO.setup(self.ROW[rowVal], GPIO.OUT)
        GPIO.output(self.ROW[rowVal], GPIO.HIGH)

        colVal = -1
        for j in range(len(self.COLUMN)):
            tmpRead = GPIO.input(self.COLUMN[j])
            if tmpRead == 1:
                colVal=j
                
        if colVal < 0 or colVal > 3:
            self.exit()
            return

        self.exit()
        return self.BUTTON_MATRIX[rowVal][colVal]
        
    def exit(self):
        for i in range(len(self.ROW)):
                GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
if __name__ == '__main__':
    key = ButtonMatrix()
    temp = None
    while True:
        button = key.buttonPressed()
        if button is not None:
            if button == temp:
                pass
            else:
                print(button)
                temp = button
        button = None