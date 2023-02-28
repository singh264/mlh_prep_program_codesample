from typing import Dict, Any

from src.sensors.sensor import Sensor
from src.sensors.sensehat.sensehat_factory import SenseHatFactory


class SensorFactory:
    @classmethod
    def _validate_data_types(cls, sensor: Sensor, data_types: Dict[str, Dict[str, Any]]) -> None:
        for data_type, props in data_types.items():
            if data_type not in sensor.data.keys():
                raise Exception(f"Unsupported data type: '{data_type}'.")

            data_unit = props['unit']
            if data_unit not in sensor.data[data_type].unit.supported:
                raise Exception(f"Unsupported data unit for '{data_type}': '{data_unit}'.")

            if "targetValue" in props and type(props["targetValue"]) != int:
                raise Exception(f"Invalid targetValue of '{data_type}.")

    @classmethod
    def create(cls, sensor_name: str, data_types: Dict[str, Dict[str, Any]]) -> Sensor:
        if not sensor_name:
            raise Exception(f"Undefined sensor name.")

        if not data_types:
            raise Exception(f"Undefined data types for {sensor_name} to collect.")

        sensor = None
        if sensor_name == "sensehat":
            sensor = SenseHatFactory.create()
        else:
            raise Exception(f"Unsupported sensor: {sensor_name}.")

        cls._validate_data_types(sensor, data_types)

        return sensor
