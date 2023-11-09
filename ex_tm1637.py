# reference: https://github.com/mcauser/micropython-tm1637

import tm1637
from machine import Pin
from utime import sleep

# Set up the TM1637 driver
display = tm1637.TM1637(clk=Pin(13), dio=Pin(10))

# "%" 문자의 7세그먼트 패턴
pattern = [0b11100011, 0b01011100]

# Clear all
display.show("    ")
sleep(1)

display.write(pattern,2)
sleep(1)

# Word
display.show("AbCd")
sleep(1)
 
#Clear all
display.show("    ")
sleep(1)
 
#Numbers
display.number(1234)
sleep(1)
 
#Time with colon
display.numbers(10,40)
sleep(1)
 
#Lower Brightness
display.brightness(0)
sleep(1)
 
#Scrolling text
display.scroll("SCrOLL", delay=500)
sleep(1)
 
#Temperature
display.temperature(37)
sleep(1)
 
#Clear all
display.show("    ")
