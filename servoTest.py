from firebase import firebase
from time import sleep
import pyupm_servo as s
import pyupm_i2clcd as l
from random import randint
from listCompiler import makeList

from math import ceil

# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
# myLCD = l.Jhd1313m1(0, 0x3E, 0x62)

cQuote = "Coffee is very good for you it is even better than water"

'''
def displayLCD(myLCD, cQuote):
        myLCD.setColor(randint(0, 255), randint(0, 255), randint(0, 255))
    for i in range(0,int(ceil(len(cQuote)/16)-1)):
            myLCD.setCursor(0,0)
            myLCD.write(cQuote[i*16:i*16+15])
            myLCD.setCursor(1,0)
        myLCD.write(cQuote[(i+1)*16:(i+1)*16+15])
        sleep(1)
'''



factlist = makeList(open("factlist.txt", "r"))
print factlist
firebase = firebase.FirebaseApplication('https://shining-heat-4946.firebaseio.com', authentication=None)
result = firebase.get('/Coffee Status', None)
servo = s.ES08A(5)
lcd = l.Jhd1313m1(0, 0x3E, 0x62)
lcd.setCursor(0, 0)
lcd.write("Initializing...")
sleep(1)


def turnOn():
        servo.setAngle(100)
        sleep(2)
        scrollRand()
    #displayLCD(myLCD, cQuote)
def scrollRand():
        fact = str(factlist[randint(0, 15)])
    print fact
    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.write(fact[0:len(fact)][0:16])
        sleep(3)
    for i in range(len(fact)):
        lcd.setCursor(0, 0)
        lcd.write(fact[i:len(fact)][0:16])
            sleep(.2)
    sleep(2)
    lcd.setCursor(0, 0)
    lcd.clear()


changed = False
while True:
    print "entered while loop"
    if firebase.get('/Coffee Status', None) == 1 and changed == False:
        print "coffee requested"
        turnOn();
        changed = True
    elif firebase.get('/Coffee Status', None) == 0:
        print "no coffee"
        changed = False
        servo.setAngle(60)
    else:
        print "coffee request still active"
    sleep(2)


