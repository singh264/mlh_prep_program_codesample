import unittest

from src.sensors.sensor import Sensor
from src.sensors.sensehat.sensehat_factory import SenseHatFactory


class TestSensehatFactory(unittest.TestCase):

    def setUp(self):
        self.temperature_data_type = 'Temperature'
        self.humidity_data_type = 'Humidity'

    def exec(self) -> Sensor:
        return SenseHatFactory.create()

    def test_create_returns_sensor(self):
        sensor = self.exec()

        self.assertIsInstance(sensor, Sensor)

    def test_sensehat_sensor_supports_humidity(self):
        sensor = self.exec()

        self.assertTrue(self.humidity_data_type in sensor.data)

    def test_sensehat_sensor_returns_valid_humidity(self):
        sensor = self.exec()

        self.assertIsInstance(sensor.data[self.humidity_data_type].value, float)

    def test_sensehat_sensor_supports_temperature(self):
        sensor = self.exec()

        self.assertTrue(self.temperature_data_type in sensor.data)

    def test_sensehat_sensor_returns_valid_temperature(self):
        sensor = self.exec()

        self.assertIsInstance(sensor.data[self.temperature_data_type].value, float)


if __name__ == '__main__':
    unittest.main()
