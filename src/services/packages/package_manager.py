from .package_manager_validator import PackageManagerValidator
from .package_manager_strategy import PackageManagerStrategy
from .impl.apt_strategy import AptStrategy
from .impl.yum_strategy import YumStrategy # Asegúrate que estos archivos existen y están implementados
from .impl.dnf_strategy import DnfStrategy # Asegúrate que estos archivos existen y están implementados
from .impl.pacman_strategy import PacmanStrategy # Asegúrate que estos archivos existen y están implementados
from .impl.unsupported_strategy import UnsupportedStrategy
from ..applications.application_repository import Application # Import Application
from typing import Optional # Import Optional

class PackageManager:
    def __init__(self, app_instance=None): # app_instance para pasar la app Textual a las estrategias
        self.package_manager_validator = PackageManagerValidator()
        self.app_instance = app_instance # Guardar la instancia de la app
        self.strategy: PackageManagerStrategy = self._get_strategy()


    def _get_strategy(self) -> PackageManagerStrategy:
        manager_type = self.package_manager_validator.detect_package_manager()
        # Pasar self.app_instance a las estrategias si lo necesitan para logging
        if manager_type == "apt":
            strategy = AptStrategy()
        elif manager_type == "yum":
            strategy = YumStrategy()
        elif manager_type == "dnf":
            strategy = DnfStrategy()
        elif manager_type == "pacman":
            strategy = PacmanStrategy()
        else:
            strategy = UnsupportedStrategy()
        
        if hasattr(strategy, 'app') and self.app_instance: # Si la estrategia tiene un atributo 'app'
            strategy.app = self.app_instance
        return strategy

    def get_current_manager_type(self) -> Optional[str]:
        # Retorna el tipo de gestor detectado, o None si no es soportado/encontrado
        detected_manager = self.package_manager_validator.detect_package_manager()
        if detected_manager in ["apt", "yum", "dnf", "pacman"]:
            return detected_manager
        return None # O podrías retornar "unsupported" si UnsupportedStrategy se considera un tipo

    async def list_upgradable_packages(self) -> list:
        return await self.strategy.list_upgradable_packages()

    async def update_all_packages(self):
        await self.strategy.update_all_packages()

    async def install_application(self, application: Application) -> bool:
        manager_type = self.get_current_manager_type()
        if not manager_type or not self.strategy.is_supported():
            print(f"Cannot install {application.name}: No supported package manager detected or strategy is unsupported.")
            # Podrías escribir en un log de la UI si tienes acceso
            return False

        package_name = application.get_package_name_for_manager(manager_type)
        if not package_name:
            print(f"Cannot install {application.name}: No package defined for manager '{manager_type}'.")
            return False
        
        print(f"Attempting to install '{package_name}' for application '{application.name}' using '{manager_type}'...")
        return await self.strategy.install_package(package_name)