import unittest

from src.sensors.sensor import Sensor
from src.sensors.sensor_factory import SensorFactory


class TestSensorFactory(unittest.TestCase):

    def setUp(self):
        self.sensor_name = "sensehat"

        self.temperature_data_type = "Temperature"
        self.humidity_data_type = "Humidity"

        self.data_types = {
            self.temperature_data_type: {
                "unit": "Celsius",
                "targetValue": 23
            },
            self.humidity_data_type: {
                "unit": "%rH",
                "targetValue": 50
            }
        }

    def exec(self) -> Sensor:
        return SensorFactory.create(self.sensor_name, self.data_types)

    def test_create_with_undefined_sensor_name(self):
        self.sensor_name = None

        with self.assertRaises(Exception) as cm:
            self.exec()

        self.assertTrue('Undefined sensor name' in str(cm.exception))

    def test_create_with_undefined_data_types(self):
        self.data_types = None

        with self.assertRaises(Exception) as cm:
            self.exec()

        self.assertTrue('Undefined data types' in str(cm.exception))

    def test_create_with_unsupported_data_type(self):
        self.data_types["Bogus"] = self.data_types[self.temperature_data_type]
        del self.data_types[self.temperature_data_type]

        with self.assertRaises(Exception) as cm:
            self.exec()

        self.assertTrue('Unsupported data type' in str(cm.exception))

    def test_create_with_unsupported_data_unit(self):
        self.data_types[self.temperature_data_type]["unit"] = "Bogus"

        with self.assertRaises(Exception) as cm:
            self.exec()

        self.assertTrue('Unsupported data unit' in str(cm.exception))

    def test_create_with_invalid_target_value(self):
        self.data_types[self.temperature_data_type]["targetValue"] = "23"

        with self.assertRaises(Exception) as cm:
            self.exec()

        self.assertTrue('Invalid targetValue' in str(cm.exception))

    def test_create_with_valid_alternate_data_unit(self):
        self.data_types[self.temperature_data_type]["unit"] = "Farenheit"

        sensor = self.exec()

        self.assertIsInstance(sensor, Sensor)

    def test_create_with_valid_config(self):
        sensor = self.exec()

        self.assertIsInstance(sensor, Sensor)


if __name__ == '__main__':
    unittest.main()
