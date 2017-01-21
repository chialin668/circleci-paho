#!/usr/bin/env python
import paho.mqtt.client as paho
import os, socket, ssl

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc) )
    client.subscribe("#" , 1 )

def on_message(client, userdata, msg):
    print("topic: "+msg.topic)
    print("payload: "+str(msg.payload))

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

awshost = "a1arqmop0meczp.iot.us-west-2.amazonaws.com"
awsport = 8883
caPath = "./ssl/root-CA.crt"
certPath = "./ssl/cert.pem"
keyPath = "./ssl/privkey.pem"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
mqttc.connect(awshost, awsport, keepalive=60)
mqttc.loop_forever()
