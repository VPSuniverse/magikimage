import subprocess

class PackageManager:
    def detect_package_manager(self):
        """Detecta el gestor de paquetes del sistema operativo."""
        # Comprobar si apt está disponible
        if self._is_command_available("apt"):
            return "apt"
        # Comprobar si yum está disponible
        elif self._is_command_available("yum"):
            return "yum"
        # Comprobar si dnf está disponible
        elif self._is_command_available("dnf"):
            return "dnf"
        # Comprobar si pacman está disponible
        elif self._is_command_available("pacman"):
            return "pacman"
        else:
            return "No se pudo detectar un gestor de paquetes compatible."

    def _is_command_available(self, command):
        """Verifica si un comando está disponible en el sistema."""
        try:
            subprocess.run([command, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except FileNotFoundError:
            return False 