import RPi.GPIO as g
import paho.mqtt.client as m
g.setmode(g.BOARD)
g.setup(3,g.IN)
import time
c = m.Client()
c.connect("broker.hivemg.com",1883)
while true :
    out=g.input(3)
    c.publish("iot/123",out)
    time.sleep(0.5)
