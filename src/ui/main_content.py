import asyncio

from textual.widgets import Static
from textual.containers import VerticalGroup
from textual.reactive import reactive
from ui.sections.system_info_table import SystemInfoTable
from ui.sections.system_update import SystemUpdate

class MainContent(VerticalGroup):
    content = reactive(SystemInfoTable())
    
    def __init__(self):
        super().__init__()
        
    def show_system_info(self):
        self.content = SystemInfoTable()
        self.refresh(recompose=True)
        
    def show_install_applications(self):
        self.content = Static("Instalar aplicaciones")
        self.refresh(recompose=True)
        
    def show_update_system(self):
        self.content = SystemUpdate()
        self.refresh(recompose=True)
        
    def show_security_checks(self):
        self.content = Static("Chequeos de seguridad")
        self.refresh(recompose=True)


    def compose(self):
        yield self.content
        