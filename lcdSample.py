import pyupm_i2clcd as lcd
import time
# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

myLcd.setCursor(0,0)
# RGB Blue
#myLcd.setColor(53, 39, 249)

# RGB Red
myLcd.setColor(255, 0, 0)
for i in range(2000):
    myLcd.setCursor(0, 0)
    myLcd.write('%d' %i)
    time.sleep(1)