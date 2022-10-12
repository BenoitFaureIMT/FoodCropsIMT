class Indicator:
    def __init__(self,id: str,frequency: int,frequencyDesc: str,geogLocation: str):
        self.id = id
        self.__frequency = frequency
        self.__frequencyDesc = frequencyDesc
        self.__geogLocation = geogLocation
