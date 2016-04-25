# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import commands
from time import sleep

SC_USER="<PUT YOUR SCALENICS_ID>"
DEVICE_TOKEN="<PUT YOUR DEVICE_TOKEN>"
DEVICE_ID="<PUT YOUR DEVICE_ID>"
MQTT_BROKER="api.scalenics.io"

def on_connect(client, userdata, rc):
  print("Connected with result code " + str(rc))

def on_disconnect(client, userdata, rc):
  if rc != 0:
     print("Unexpected disconnection.")

def on_publish(client, userdata, mid):
  print("publish: {0}".format(mid))

def on_message(client, userdata, msg):
  print(msg.topic+" "+str(msg.payload))
  if msg.payload == "led3:on":
    print "led3 is on!"
    out = commands.getoutput("/bin/echo 1 > /sys/class/leds/led3/brightness")

  if msg.payload == "led3:off":
    print "led3 is off!"
    out = commands.getoutput("/bin/echo 0 > /sys/class/leds/led3/brightness")

def main():
  client = mqtt.Client()
  client.on_connect = on_connect
  client.on_disconnect = on_disconnect
  #client.on_publish = on_publish
  client.on_message = on_message
  client.username_pw_set(SC_USER, DEVICE_TOKEN)
  client.connect(MQTT_BROKER, 1883, 10)

  client.subscribe(DEVICE_TOKEN+"/"+DEVICE_ID+"/subscribe")
  client.loop_forever()


if __name__ == '__main__':
        main()

