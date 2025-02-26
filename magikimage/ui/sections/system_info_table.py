from textual.widgets import DataTable
from textual.app import ComposeResult

class SystemInfoTable(DataTable):
    def compose(self) -> ComposeResult:
        yield self 
    
    def on_mount(self) -> None:
        self.focus()
        self.add_columns("Propiedad", "Valor")
        
        self.add_row("Sistema Operativo", "Linux")
        self.add_row("Versión", "5.4.0-42-generic")
        self.add_row("Arquitectura", "x86_64")
        self.add_row("Hostname", "mi-computadora")