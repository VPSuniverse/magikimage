from .package_manager_validator import PackageManagerValidator
from .package_manager_strategy import PackageManagerStrategy
from .impl.apt_strategy import AptStrategy
from .impl.yum_strategy import YumStrategy
from .impl.dnf_strategy import DnfStrategy
from .impl.pacman_strategy import PacmanStrategy
from .impl.unsupported_strategy import UnsupportedStrategy

class PackageManager:
    def __init__(self):
        self.package_manager_validator = PackageManagerValidator()
        self.strategy: PackageManagerStrategy = self.get_strategy()

    def get_strategy(self) -> PackageManagerStrategy:
        manager = self.package_manager_validator.detect_package_manager()
        if manager == "apt":
            return AptStrategy()
        elif manager == "yum":
            return YumStrategy()
        elif manager == "dnf":
            return DnfStrategy()
        elif manager == "pacman":
            return PacmanStrategy()
        else:
            return UnsupportedStrategy()

    async def list_upgradable_packages(self) -> list:
        package_list = self.strategy.list_upgradable_packages()
        return package_list

    async def update_all_packages(self):
        self.strategy.update_all_packages()