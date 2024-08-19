import network
import time
import dht
import machine
from umqtt.simple import MQTTClient # type: ignore
from machine import Pin, I2C
from stemma_soil_sensor import StemmaSoilSensor
import secrets

# Initialize DHT11 sensor
dht_sensor = dht.DHT11(machine.Pin(15))

# Initialize I2C bus and Seesaw sensor
SDA_PIN = 12 # update this
SCL_PIN = 13 # update this

i2c = machine.I2C(sda=machine.Pin(SDA_PIN), scl=machine.Pin(SCL_PIN), freq=400000)
seesaw = StemmaSoilSensor(i2c)

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
    
    while not wlan.isconnected():
        print('Connecting to Wi-Fi...')
        time.sleep(1)
    
    print('Connected to Wi-Fi')
    print('Network config:', wlan.ifconfig())

def connect_adafruit_io():
    client = MQTTClient(secrets.ADAFRUIT_IO_USERNAME, secrets.ADAFRUIT_IO_URL, user=secrets.ADAFRUIT_IO_USERNAME, password=secrets.ADAFRUIT_IO_KEY, ssl=False)
    client.connect()
    print('Connected to Adafruit IO')
    return client

def main():
    connect_wifi()
    client = connect_adafruit_io()

    print("Scanning I2C bus for devices...")
    devices = i2c_bus.scan()
    if devices:
        print('I2C devices found:', [hex(device) for device in devices])
    else:
        print('No I2C devices found')
    
    while True:
        # Read temperature and humidity from DHT11
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()

        # Read soil moisture and temperature from I2C sensor
        moisture = seesaw.get_moisture()

        # Publish data to Adafruit IO
        client.publish(secrets.ADAFRUIT_IO_FEED_TEMPERATURE, str(temp))   
        client.publish(secrets.ADAFRUIT_IO_FEED_HUMIDITY, str(hum))     
        client.publish(secrets.ADAFRUIT_IO_FEED_SOIL, str(moisture))
        
        # Print readings to the console
        print(f'Temperature: {temp}°C, Humidity: {hum}%')
        if moisture is not None:
            print(f'Soil Moisture: {moisture}')

        
        time.sleep(60)  # Adjust the delay as needed

if __name__ == '__main__':
    main()
