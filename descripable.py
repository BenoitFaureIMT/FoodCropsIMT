from abc import ABC, abstractmethod

class Descripable(ABC):
    @abstractmethod
    def describe(self):
        pass