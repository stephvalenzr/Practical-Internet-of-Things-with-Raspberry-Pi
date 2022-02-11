import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/GarbageBin/#")
    
mess = 0
def on_message(client1, userdata, message):

    print("Notice: "  ,str(message.payload.decode("utf-8")))
    
    #print("Message received:  " + msg.topic + " " + msg.payload.decode("utf-8"))
    
client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.36", 1883, 60)

client.loop_forever()
    
