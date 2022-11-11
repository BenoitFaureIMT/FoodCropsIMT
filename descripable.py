from abc import ABC, abstractmethod

class Descripable(ABC):
    # classe descripable permmettant d'afficher les données dans la console
    @abstractmethod
    def describe(self):
        pass