import dht
import time
import datetime

# read data using pin 4
instance = dht.DHT11(pin=4, sample_interval=10, debug=0)

while True:
    result = instance.read()
    print("Last valid input: " + str(datetime.datetime.now()))
    print("Temperature: %d C" % result[0])
    print("Humidity: %d %%" % result[1])

    time.sleep(instance.sample_interval)



