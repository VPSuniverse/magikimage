import asyncio
from ..package_manager_strategy import PackageManagerStrategy
from typing import List

class AptStrategy(PackageManagerStrategy):
    async def list_upgradable_packages(self) -> List[str]:
        # Implementación para listar paquetes actualizables con apt
        try:
            process = await asyncio.create_subprocess_exec(
                "apt", "list", "--upgradable",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            if process.returncode == 0:
                lines = stdout.decode().splitlines()
                packages = []
                for line in lines:
                    if line and not line.startswith("Listing..."):
                        packages.append(line.split('/')[0])
                return packages
            return []
        except FileNotFoundError: # apt no encontrado
            return []
        except Exception: # Otros errores
            return []


    async def update_all_packages(self) -> None:
        # Implementación para actualizar todos los paquetes con apt
        try:
            process = await asyncio.create_subprocess_exec(
                "sudo", "apt-get", "update",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            await process.communicate() # Esperar a que 'apt-get update' termine

            process_upgrade = await asyncio.create_subprocess_exec(
                "sudo", "apt-get", "upgrade", "-y",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            # Aquí podrías procesar stdout/stderr si necesitas feedback detallado
            await process_upgrade.communicate()
        except Exception as e:
            print(f"Error during apt update/upgrade: {e}")


    def is_supported(self) -> bool:
        # Podrías añadir una comprobación más robusta si 'apt' está disponible
        return True # Asumimos que si se elige esta estrategia, es porque es soportada

    async def install_package(self, package_name: str) -> bool:
        command = ["sudo", "apt-get", "install", "-y"] + package_name.split()
        log_widget = self.app.query_one("#install_log") if hasattr(self.app, "query_one") else None # Intenta obtener el log
        
        if log_widget:
            log_widget.write_line(f"Executing: {' '.join(command)}")

        try:
            process = await asyncio.create_subprocess_exec(
                *command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()

            if stdout and log_widget:
                log_widget.write_line(f"[dim]stdout:\n{stdout.decode()}[/dim]")
            if stderr and log_widget:
                 # No imprimir stderr si el código de retorno es 0, ya que apt a veces usa stderr para info
                if process.returncode != 0:
                    log_widget.write_line(f"[dim red]stderr:\n{stderr.decode()}[/dim red]")


            if process.returncode == 0:
                if log_widget:
                    log_widget.write_line(f"[green]Successfully installed {package_name}.[/green]")
                return True
            else:
                if log_widget:
                    log_widget.write_line(f"[red]Error installing {package_name}. Return code: {process.returncode}[/red]")
                return False
        except FileNotFoundError:
            if log_widget:
                log_widget.write_line(f"[red]Error: 'sudo' or 'apt-get' command not found.[/red]")
            return False
        except Exception as e:
            if log_widget:
                log_widget.write_line(f"[red]Exception during installation of {package_name}: {e}[/red]")
            return False