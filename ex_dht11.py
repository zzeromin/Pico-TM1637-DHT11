import dht
from machine import Pin
from utime import sleep

# DHT11 센서 초기화
d = dht.DHT11( machine.Pin(16) )

while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    
    # 콘솔창에 온습도 데이터 출력
    print("Temp: {}°C, Hum: {}%".format(temp, hum))
    sleep(2)

