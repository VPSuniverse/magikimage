import subprocess
from ..package_manager_strategy import PackageManagerStrategy

class YumStrategy(PackageManagerStrategy):
    def list_upgradable_packages(self):
        result = subprocess.run(['yum', 'check-update'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8').splitlines()

    def update_all_packages(self):
        subprocess.run(['yum', 'update', '-y'])