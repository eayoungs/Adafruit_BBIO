
import Adafruit_BBIO as GPIO
import Adafruit_PWM as PWM


GPIO.setup("P8_10", GPIO.OUT)
GPIO.output("P8_10", GPIO.HIGH)
GPIO.cleanup()
