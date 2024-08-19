
# Raspberry Pi Pico W Plant Care System

## Introduction

This project aims to develop a smart plant care system using the Raspberry Pi Pico W. The system monitors environmental conditions such as temperature, humidity, and soil moisture levels. It utilizes Wi-Fi communication and the MQTT protocol to send real-time data to Adafruit IO, which can be monitored on an iOS device.

## Project Overview

- **Estimated Time to Complete:** 8-10 hours

### Objectives

- Monitor temperature and humidity using the DHT11 sensor.
- Measure soil moisture using a soil moisture sensor.
- Send sensor data to Adafruit IO via MQTT.
- Access and monitor data on an iOS device.
- Receive notifications of unhealthy values and recommended measures.

## Why This Project?

This project was chosen to explore the integration of IoT technology with plant care. It provides a practical application of environmental monitoring and data visualization.

### Purpose

The system helps maintain optimal conditions for plant health by providing real-time monitoring and notifications, ensuring timely interventions to prevent plant stress.

### Insights

The data will offer insights into the environmental conditions affecting plant health, helping to optimize watering schedules and environmental adjustments.

## Materials

### List of Components

- **Raspberry Pi Pico W**
- **DHT11 Temperature and Humidity Sensor**
- **STEMMA Soil Moisture Sensor**
- **Breadboard**
- **Jumper Wires**

### Specifications and Purchase Information

- **Raspberry Pi Pico W**
  - **Specifications:** RP2040 microcontroller chip, 2.4GHz Wi-Fi
  - **Purchased from:** Electrokit


- **DHT11 Temperature and Humidity Sensor**
  - **Specifications:** Temperature range 0-50°C, Humidity range 20-90%
  - **Purchased from:** Electrokit

- **STEMMA Soil Moisture Sensor**
  - **Specifications:** I2C interface, 3.3V operating voltage
  - **Purchased from:** [Adafruit](https://www.adafruit.com)

- **Breadboard and Jumper Wires**
  - **Purchased from:** Electrokit



 **Total Cost:** 625 SEK

## Computer Setup

### Chosen IDE

**Thonny**: An easy-to-use IDE for MicroPython programming.

### Setup Steps

1. **Flash MicroPython on Raspberry Pi Pico W**:
   - Download the MicroPython UF2 file from the official website.
   - Connect Pico W to the computer while holding the BOOTSEL button.
   - Drag and drop the UF2 file onto the Pico W drive.

2. **Install Thonny**:
   - Download and install Thonny from [thonny.org](https://thonny.org).
   - Select the MicroPython (Raspberry Pi Pico) interpreter in Thonny.

3. **Install Required Libraries**:
   - Use Thonny to install libraries for DHT11 and STEMMA Soil Moisture Sensor (e.g., `adafruit_dht` and `adafruit_seesaw`).

## Putting Everything Together

### Circuit Diagram

![418AED6E-A6EF-4E1D-BB75-BCB75B7A1C8C](https://hackmd.io/_uploads/SJUlR1j8A.jpg)


### Electrical Connections

- **DHT11 Sensor**:
  - VCC to 3.3V on Pico W
  - GND to GND on Pico W
  - Data to GPIO 15 on Pico W
- **Soil Moisture Sensor**:
  - VCC to 3.3V on Pico W
  - GND to GND on Pico W
  - SDA to GP12 on Pico W
  - SCL to GP13 on Pico W

## Hardware Setup Images

## Raspberry Pi Pico W Pinout Diagram

![Raspberry_pi_pico_w_pinout](https://hackmd.io/_uploads/r1y_O5WD0.png)


### Close-Up of DHT11 Sensor Connections:

![D64C1FB2-456F-4D7E-B354-C279F4FE1978](https://hackmd.io/_uploads/ryGBBcbvC.jpg)

As presented the DHT11 sensor is connnected with power to the + line, by the red jumpercable, which is supplied with power from the Raspberry Pi Pico W. It has connecetion to ground the same way by the black jumperwire. The green jumpercable supplies the data to the Pico W to GP15 pin.


## Close-Up of Soil Moisture Sensor Connections:


![FCDFE6CF-E733-4253-8AC4-F2FF31C49A2D](https://hackmd.io/_uploads/rybDUqbDA.jpg)


The soil moisture sensor is supplied with power and is connected to ground in the same way the DHT11 sensor is. The data is being sent from sensor to Pico W a little bit different, it is an I2C sensor so its connected with 2 jumperwires as the picture presents one green and one white. Theese are separate and needs to be rightfully declared to get the data. White cable connects the SDA output and is connected to the pico through GP12, which as you can see in the Raspberry Pi Pico W pinout diagram is created to suit the SDA output. The green jumpercable is connected to the sensors SCL output and is connected to the corresponding SCL pin on the Pico W, which is GP13.


## Electrical Calculations

To ensure that the current and voltage requirements of all sensors do not exceed the capabilities of the Raspberry Pi Pico W, we need to consider the power consumption of each component.

### Power Consumption

### Raspberry Pi Pico W

Operating Voltage: 3.3V
Current Consumption: ~100 mA (depending on the workload and peripherals connected)

### DHT11 Temperature and Humidity Sensor

Operating Voltage: 3.3V
Current Consumption: ~2.5 mA (average during measurements)

### STEMMA Soil Moisture Sensor

Operating Voltage: 3.3V
Current Consumption: ~10 mA (during measurements)
Total Power Consumption
Total Current Consumption:

Raspberry Pi Pico W: 100 mA
DHT11 Sensor: 2.5 mA
STEMMA Soil Moisture Sensor: 10 mA
Total: 100 mA + 2.5 mA + 10 mA = 112.5 mA

Voltage Supply: 3.3V

The total current consumption of 112.5 mA is well within the capabilities of the Raspberry Pi Pico W, which can handle up to 500 mA on its 3.3V rail. This ensures that our sensors can operate reliably without overloading the microcontroller.

## Platform

### Platform Choice

**Adafruit IO**: Chosen for its ease of use, free tier availability, and robust MQTT support. It allows for real-time data visualization and mobile access via the Adafruit IO app.

### Platform Functionality

- **Local or Cloud**: Cloud-based
- **Subscription**: Free tier used
- **Scalability**: Can be expanded with more sensors and integrated with other IoT platforms.

## The Code

![63EE546E-4BAD-4B94-BE28-495D2A226CE6](https://hackmd.io/_uploads/SJGs2JjUA.jpg)
![C98FFFA6-3057-4A01-9651-8C0AE8CB0F57](https://hackmd.io/_uploads/Byfjn1iL0.jpg)



# Explanation

#### Sensor Initialization: 

Initializes the DHT11 and STEMMA soil moisture sensors.
#### Data Reading: 
Reads temperature, humidity, and soil moisture levels in a loop.

#### Data Publishing: 
Sends data to Adafruit IO using MQTT (actual implementation requires Adafruit_IO library and MQTT setup).
Transmitting the Data / Connectivity
Data Transmission
Frequency: Every 60 seconds
Wireless Protocol: Wi-Fi
Transport Protocol: MQTT

#### Design Choices
Wi-Fi: Chosen for its ease of integration and range.
MQTT: Lightweight protocol suitable for IoT applications, ensuring efficient data transmission.

Presenting the Data through a Dashboard Setup on Adafruit IO

Create Feeds: Temperature, Humidity, Soil Moisture on Adafruit IO.

# Customize Dashboard: Use widgets to visualize the data.


![5BA005ED-889F-47BE-9552-A80E1D7A16A9](https://hackmd.io/_uploads/S1NtJgsUC.jpg)

# Data Storage
Frequency: Data is sent and saved every 60 seconds.
Database Choice: Adafruit IO's internal storage, suitable for small-scale projects. The free tier of adafruit allows storing data for 30 days.

# Final Thoughts
The project successfully demonstrates the integration of IoT technology for plant care. Future improvements could include adding more sensors such as light sensors, and ph sensor for the soil, implementing automatic watering, and integrating with other IoT platforms for enhanced functionality.

# Final Results

![5A0EA166-48AA-4857-A3FA-EDAD4D53C0B9](https://hackmd.io/_uploads/SJ7FJljLR.jpg)

Above are the feeds created for this project

![BC1AA4D7-D356-4D46-9898-38D1C5384A38](https://hackmd.io/_uploads/rJGylxi80.jpg)

Here are the no-code solution to trigger actions based on values of data that is transmitted to the feeds.

![2C537AF2-4F60-4761-B7B0-1FDF67950FA3_1_105_c](https://hackmd.io/_uploads/SJ43QTMDA.jpg)

Here is the mobile monitoring system suitable for iOS devices (itsaSnap by Adafruit)

![DFD9D3DA-4BA7-4C86-8B5F-CAC7CA4339B3_1_105_c](https://hackmd.io/_uploads/BJmaXaGvR.jpg)
![80C3B1C9-8150-4A6A-8E35-802F990546C9](https://hackmd.io/_uploads/HJ5TX6MDA.jpg)
![BDAE2AFB-BBA7-4D8B-939F-D2D3A3300EF2_1_105_c](https://hackmd.io/_uploads/SydCQaGPC.jpg)
![0A8E3CA8-1A52-47E4-8AF4-38C6080AFB0E](https://hackmd.io/_uploads/SkJkEpfD0.jpg)

Here are a visual representation of the notifications sent by Adafruit by email. Values of data is manipulated by me to actually trigger the notification, so disregard them.


With the triggers and actions specified like above emails will be sent out when values are not suiting the plant, theese can be customized to ones own preferences.


# References
Adafruit IO documentation
MicroPython documentation
Tutorials on using DHT11 and STEMMA sensors with Raspberry Pi Pico W
