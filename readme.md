
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Hi there! Welcome to AWS Cloud9!

To get started, create some files, play with the terminal,
or visit https://docs.aws.amazon.com/console/cloud9/ for our documentation.

Happy coding!

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
    
    
    
Documentation:

As part of this course we decided to develop a system that assists to controll in real time the number of visitors in a certain business.
Our system should be based on sensor that should recognize movement from/to a certain place and count the current number of persons at the place in real time.
Due to restrictions, we based our project first on pressing a button to present "movement" of poeples.
Once pressing the button, a record of entrancing sent to the cloud DB and the counter is grown in 1.
This way it is possible to control in real time, several places capacity and it could be a very helpful tool for city halls and other organizations.

Description of the code:

1.Defiding a specific method for call to action (pressing the button)
2.connecting to DB
3.Put the data in the DB