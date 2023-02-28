from __future__ import annotations

from src.sensors.sensor import Sensor
from src.sensors.sensehat.sensehat_temperature_sensor import SenseHatTemperatureSensor
from src.sensors.sensehat.sensehat_humidity_sensor import SenseHatHumiditySensor


class SenseHatFactory():
    @staticmethod
    def create() -> Sensor:
        humidity_sensor = SenseHatHumiditySensor()
        temperature_sensor = SenseHatTemperatureSensor()

        humidity_sensor.next = temperature_sensor

        return humidity_sensor
