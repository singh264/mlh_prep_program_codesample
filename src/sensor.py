from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List, Any

from src.sensors.sensor_data import SensorData


class Sensor(ABC):
    def __init__(self):
        self.__next = None
        self.__data = {}

    def _set_next(self, sensor: Sensor) -> None:
        self.__next = sensor

    next = property(fset=_set_next)

    @property
    def data(self) -> Dict[str, SensorData]:
        if self.__next:
            self.__data = self.__next.data

        self.__data.update({self._data_type: self._get_data()})

        return self.__data

    @property
    @abstractmethod
    def _data_type(self) -> str:
        pass

    @abstractmethod
    def _get_data(self) -> SensorData:
        pass
