# MLH Prep Program Code Sample

## Context

My code sample is the python module that I recently wrote for my personal project called SoundholeCare.

The goal of SoundholeCare is to help people monitor the environment near their musical instruments.

I have deployed this service on my Raspberry Pi to monitor the environment near my acoustic guitar!

## About the Code Sample

The python module encapsulates the logic to retrieve environment data from a sensor.

Currently, only the Sense HAT temperature and humidity sensors are supported.

In the future, DHT22 temperature and humidity sensors will be supported.

## Lessons learned from the Code Sample

When creating the python module I wanted to make it as reusable and extensible as possible.

I applied several design patterns to achieve this:

- The Chain of Responsibility pattern for the sensor creation logic to create custom sensors easily.
- The Template Method pattern for the sensor data retrieval logic to support new sensors easily.
- The Singleton pattern to create the Sense HAT sensor and share it among many classes.

Finally, I practiced writing clean unit tests for the python module.
