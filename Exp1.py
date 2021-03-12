import paho.mqtt.client as m
c = m.Client()
c.connect("broker.hivemq.com",1883)
def abc(c,u,f,rc) :
    print(rc)
    c.subscribe("iot/123")
def abc1(c,u,msg) :
    print(msg.payload.decode())
c.on_connect=abc
c.on_message=abc1
c.loop_forever()
