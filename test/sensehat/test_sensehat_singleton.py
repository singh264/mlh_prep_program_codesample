import unittest
from sense_hat import SenseHat

from src.sensors.sensehat.sensehat_singleton import SenseHatSingleton


class TestSensehatSingleton(unittest.TestCase):

    def exec(self) -> SenseHatSingleton:
        return SenseHatSingleton.get_instance()

    def test_get_instance_returns_sensehat(self):
        sensehat = self.exec()

        self.assertIsInstance(sensehat, SenseHat)

    def test_get_instance_returns_singleton(self):
        sensehat1 = self.exec()
        sensehat2 = self.exec()

        self.assertTrue(sensehat1 is sensehat2)


if __name__ == '__main__':
    unittest.main()
