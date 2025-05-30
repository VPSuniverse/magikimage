from abc import ABC, abstractmethod
from typing import List

class PackageManagerStrategy(ABC):
    @abstractmethod
    async def list_upgradable_packages(self) -> List[str]:
        """Devuelve una lista de paquetes que se pueden actualizar."""
        pass

    @abstractmethod
    async def update_all_packages(self) -> None:
        """Actualiza todos los paquetes."""
        pass

    @abstractmethod
    def is_supported(self) -> bool:
        """Check if the package manager is supported on this system."""
        return True

    @abstractmethod
    async def install_package(self, package_name: str) -> bool:
        """Installs a given package. Returns True on success, False otherwise."""
        pass