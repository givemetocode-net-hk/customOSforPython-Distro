import paho.mqtt.client as paho
from paho import mqtt
import ssl


def remove_duplicate_messages(message):
    if ":" in message:
        return message.split(":", 1)[1]
    return message

username = input("your name: ") #fix
def on_message(client, userdata, msg):
    message = msg.payload.decode()
    if not message.startswith(username + ":"):
        if ":" in message:
            message = remove_duplicate_messages(message)
        print(f"\r{message}\n{username}: ", end="", flush=True)


def on_connect(client, userdata, flags, rc, properties=None):
    #print("CONNACK received with code %s." % rc)
    print("connected, press enter to chat.")

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5, callback_api_version=paho.CallbackAPIVersion.VERSION2)
client.on_message = on_message
client.on_connect = on_connect

# Set TLS and authentication
client.tls_set(tls_version=ssl.PROTOCOL_TLS)
client.username_pw_set("customos-client", "Customos-client1")
client.connect("ffdd7ccbe01d48c5a6e3fd8463b79604.s1.eu.hivemq.cloud", 8883)
client.subscribe("customos/worldchat", qos=1)


client.loop_start()

while True:
    message = input(f"{username}: ")    
    if ":" in message:
        message = remove_duplicate_messages(message)
    if message.lower() == "quit":
        break    
    client.publish("customos/worldchat", f"{username}:{message}", qos=1)    
client.loop_stop()
