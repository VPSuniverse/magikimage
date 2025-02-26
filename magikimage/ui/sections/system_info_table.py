from textual.widgets import DataTable
from textual.app import ComposeResult

class SystemInfoTable(DataTable):
    def compose(self) -> ComposeResult:
        yield self 
    
    def on_mount(self) -> None:
        self.focus()
        self.add_columns("Propiedad", "Valor")
        
        # Aquí puedes agregar la información del sistema operativo
        self.add_row("Sistema Operativo", "Linux")  # Cambia esto por la información real
        self.add_row("Versión", "5.4.0-42-generic")  # Cambia esto por la información real
        self.add_row("Arquitectura", "x86_64")  # Cambia esto por la información real
        self.add_row("Hostname", "mi-computadora")  # Cambia esto por la información real