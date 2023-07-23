from abc import ABC, abstractmethod, abstractproperty

# Classe ABSTRATA
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass
