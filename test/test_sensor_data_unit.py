import unittest

from src.sensors.sensor_data_unit import SensorDataUnit


class TestSensorDataUnit(unittest.TestCase):

    def setUp(self):
        self.default_unit = 'default'
        self.supported_units = ['supported1', 'supported2']

    def exec(self) -> SensorDataUnit:
        return SensorDataUnit(self.default_unit, self.supported_units)

    def test_unit_returns_valid_default_unit(self):
        unit = self.exec()

        self.assertEqual(unit.default, self.default_unit)

    def test_unit_returns_valid_supported_unit(self):
        unit = self.exec()

        self.assertEqual(unit.supported, [self.default_unit, *self.supported_units])


if __name__ == '__main__':
    unittest.main()
