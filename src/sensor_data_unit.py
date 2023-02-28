from typing import List


class SensorDataUnit:
    def __init__(self, default: str, supported: List[str] = []) -> None:
        self.__default = default
        self.__supported = [self.__default, *supported]

    @property
    def default(self) -> str:
        return self.__default

    @property
    def supported(self) -> List[str]:
        return self.__supported
