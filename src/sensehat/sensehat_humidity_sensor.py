from src.sensors.sensehat.sensehat_sensor import SenseHatSensor
from src.sensors.sensor_data import SensorData
from src.sensors.sensor_data_unit import SensorDataUnit


class SenseHatHumiditySensor(SenseHatSensor):
    def __init__(self) -> None:
        super().__init__()

    @property
    def _data_type(self) -> str:
        return "Humidity"

    def _get_data(self) -> SensorData:
        value = self._sense.get_humidity()
        unit = SensorDataUnit('%rH')

        return SensorData(value, unit)
