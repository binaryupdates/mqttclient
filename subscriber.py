# Import package
import paho.mqtt.client as mqtt

# Define Variables
MQTT_HOST = "192.168.1.25"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 5
MQTT_TOPIC = "hello/world"
MQTT_MSG = "Hello MQTT"

# Define on_connect event Handler
def on_connect(mosq, obj, flags, rc):
	#Subscribe to a the Topic
	mqttc.subscribe(MQTT_TOPIC, 0)

# Define on_subscribe event Handler
def on_subscribe(mosq, obj, mid, granted_qos):
    print ("Subscribed to MQTT Topic")

# Define on_message event Handler
def on_message(mosq, obj, msg):
	print (msg.payload.decode())

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register Event Handlers
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL )

# Continue the network loop
mqttc.loop_forever()
