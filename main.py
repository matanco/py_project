# Import Raspberry Pi GPIO library
import RPi.GPIO as GPIO
import boto3
import string
import random
 
def button_callback(channel):
    print("Button was pushed!")
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('passblind1')
    char_set = string.ascii_uppercase + string.digits
	
    table.put_item(
	   Item={
			'data' : ''.join(random.sample(char_set*6, 6)),
			'place' : 'barbi'
		}
	)
    

    
		
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up