import subprocess
from ..package_manager_strategy import PackageManagerStrategy

class DnfStrategy(PackageManagerStrategy):
    def list_upgradable_packages(self):
        result = subprocess.run(['dnf', 'check-update'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8').splitlines()

    def update_all_packages(self):
        subprocess.run(['dnf', 'upgrade', '-y'])