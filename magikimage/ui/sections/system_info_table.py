from textual.widgets import DataTable, Static
from textual.app import ComposeResult

class SystemInfoTable(Static):
    def compose(self) -> ComposeResult:
        yield DataTable() 
    
    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.focus()
        table.add_columns("Propiedad", "Valor")
        
        table.add_row("Sistema Operativo", "Linux")
        table.add_row("Versión", "5.4.0-42-generic")
        table.add_row("Arquitectura", "x86_64")
        table.add_row("Hostname", "mi-computadora")
        
        table.styles.padding = 1
        table.styles.margin = 1
        