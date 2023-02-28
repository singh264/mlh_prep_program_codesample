from src.sensors.sensor import Sensor
from src.sensors.sensehat.sensehat_singleton import SenseHatSingleton


class SenseHatSensor(Sensor):
    def __init__(self) -> None:
        super().__init__()
        self._sense = SenseHatSingleton.get_instance()
