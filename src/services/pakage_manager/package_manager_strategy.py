from abc import ABC, abstractmethod

class PackageManagerStrategy(ABC):
    @abstractmethod
    def list_upgradable_packages(self):
        """Devuelve una lista de paquetes que se pueden actualizar."""
        pass

    @abstractmethod
    def update_all_packages(self):
        """Actualiza todos los paquetes."""
        pass 