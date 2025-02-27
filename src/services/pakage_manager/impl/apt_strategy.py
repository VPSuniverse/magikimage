import subprocess
from ..package_manager_strategy import PackageManagerStrategy

class AptStrategy(PackageManagerStrategy):
    def list_upgradable_packages(self):
        result = subprocess.run(['apt', 'list', '--upgradable'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8').splitlines()

    def update_all_packages(self):
        subprocess.run(['apt', 'update'])
        subprocess.run(['apt', 'upgrade', '-y'])