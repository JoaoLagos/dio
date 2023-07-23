from abc import ABC, abstractmethod

# Classe ABSTRATA
class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta):
        pass
