# Temperature and humidity measurement devices example code

import dht
import tm1637
from machine import Pin
from utime import sleep

# DHT11 센서 초기화
d = dht.DHT11(machine.Pin(16))

# TM1637 모듈 초기화
display = tm1637.TM1637(clk=Pin(13), dio=Pin(10))

# "%" 문자의 7세그먼트 패턴
pattern = [0b11100011, 0b01011100]

while True:
    
    # set value t, h
    t = d.temperature()
    h = d.humidity()*100
    
    # clear all
    #display.show("    ")
    #sleep(0.1)
        
    # 온도와 습도를 tm1637 모듈에 출력
    d.measure()
    display.temperature(t)
    sleep(2)    

    display.number(h)
    display.write(pattern,2)
    sleep(2)

