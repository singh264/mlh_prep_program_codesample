from src.sensors.sensehat.sensehat_sensor import SenseHatSensor
from src.sensors.sensor_data import SensorData
from src.sensors.sensor_data_unit import SensorDataUnit


class SenseHatTemperatureSensor(SenseHatSensor):
    def __init__(self) -> None:
        super().__init__()

    @property
    def _data_type(self) -> str:
        return "Temperature"

    def _get_data(self) -> SensorData:
        value = self._sense.get_temperature()
        unit = SensorDataUnit('Celsius', supported=['Farenheit'])

        return SensorData(value, unit)
