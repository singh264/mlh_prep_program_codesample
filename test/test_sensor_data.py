import unittest

from src.sensors.sensor_data import SensorData
from src.sensors.sensor_data_unit import SensorDataUnit


class TestSensorData(unittest.TestCase):

    def setUp(self):
        self.value = 22.2

        self.default_unit = 'default'
        self.supported_units = ['supported1', 'supported2']
        self.unit = SensorDataUnit(self.default_unit, self.supported_units)

    def exec(self) -> SensorData:
        return SensorData(self.value, self.unit)

    def test_data_returns_valid_value(self):
        data = self.exec()

        self.assertEqual(data.value, self.value)

    def test_data_returns_unit(self):
        data = self.exec()

        self.assertIsInstance(data.unit, SensorDataUnit)

    def test_data_returns_valid_default_unit(self):
        data = self.exec()

        self.assertEqual(data.unit.default, self.default_unit)

    def test_data_returns_valid_supported_unit(self):
        data = self.exec()

        self.assertEqual(data.unit.supported, [self.default_unit, *self.supported_units])


if __name__ == '__main__':
    unittest.main()
