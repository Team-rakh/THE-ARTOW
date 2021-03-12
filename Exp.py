import paho.mqtt.client as m
c = m.Client()
c.connect("broker.hivemq.com",1883)
while True :
    c.publish("iot/abit","Hello Dayanidhi Sir")
    