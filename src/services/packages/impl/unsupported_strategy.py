import subprocess
from ..package_manager_strategy import PackageManagerStrategy

class UnsupportedStrategy(PackageManagerStrategy):
    def list_upgradable_packages(self):
        return []

    def update_all_packages(self):
        pass