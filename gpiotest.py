import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print(GPIO.input(17))

GPIO.add_event_detect(17, GPIO.RISING)
def my_callback():
  print('PUSHED')
GPIO.add_event_callback(17, my_callback)
