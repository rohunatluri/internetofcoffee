import pyupm_i2clcd as l
from time import sleep

lcd = l.Jhd1313m1(0, 0x3E, 0x62)
lcd.setColor(255, 0, 0)
print "initialized lcd"
lcd.setCursor(0,0)
lcd.write("Hello World")
print "wrote"
sleep(5)