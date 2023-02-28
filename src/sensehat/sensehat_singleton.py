from sense_hat import SenseHat

class SenseHatSingleton:
    __sense_hat = None

    @staticmethod
    def get_instance() -> SenseHat:
        if not SenseHatSingleton.__sense_hat:
            SenseHatSingleton()

        return SenseHatSingleton.__sense_hat

    def __init__(self) -> None:
        if SenseHatSingleton.__sense_hat:
            raise Exception('SenseHat already initialized.')

        SenseHatSingleton.__sense_hat = SenseHat()
