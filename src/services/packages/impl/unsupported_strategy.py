import subprocess
from ..package_manager_strategy import PackageManagerStrategy
from typing import List

class UnsupportedStrategy(PackageManagerStrategy):
    async def list_upgradable_packages(self) -> List[str]:
        return []

    async def update_all_packages(self) -> None:
        pass

    def is_supported(self) -> bool:
        return False

    async def install_package(self, package_name: str) -> bool:
        print(f"Cannot install {package_name}: Package manager not supported.")
        return False