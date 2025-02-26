from textual.widgets import Static
from textual.containers import VerticalGroup
from textual.reactive import reactive
from ui.sections.system_info_table import SystemInfoTable

class MainContent(VerticalGroup):
    content = reactive("INFO")
    
    def __init__(self):
        super().__init__()

    def show_system_info(self):
        self.content = "INFO"
        self.refresh(recompose=True)
        
    def show_install_applications(self):
        self.content = "INSTALL"
        self.refresh(recompose=True)
        
    def show_update_system(self):
        self.content = "UPDATE"
        self.refresh(recompose=True)
        
    def show_security_checks(self):
        self.content = "SECURITY"
        self.refresh(recompose=True)

    def compose(self):
        match self.content:
            case "INFO":
                yield Static("Información del sistema")
            case "INSTALL":
                yield Static("Instalar aplicaciones")
            case "UPDATE":
                yield Static("Actualizar sistema")
            case "SECURITY":
                yield Static("Chequeos de seguridad")
