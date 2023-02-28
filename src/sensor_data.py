from __future__ import annotations
from typing import Dict, List, Any

from src.sensors.sensor_data_unit import SensorDataUnit


class SensorData:
    def __init__(self, value: float, unit: SensorDataUnit) -> None:
        self.__value = value
        self.__unit = unit

    @property
    def value(self) -> Dict[str, float]:
        return self.__value

    @ property
    def unit(self) -> Dict[str, SensorDataUnit]:
        return self.__unit
