from textual.widgets import DataTable, Static
from textual.app import ComposeResult
from services.os_information import OSInformation
from services.i18n import i18n

class SystemInfoTable(Static):
    os_information = OSInformation()
    def compose(self) -> ComposeResult:
        yield DataTable() 
    
    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.focus()
        table.add_columns(i18n.gettext("Propiedad"), i18n.gettext("Valor"))
        
        table.add_row(i18n.gettext("Sistema Operativo"), self.os_information.get_os())
        table.add_row(i18n.gettext("Versión"), self.os_information.get_version())
        table.add_row(i18n.gettext("Arquitectura"), self.os_information.get_architecture())
        table.add_row(i18n.gettext("Hostname"), self.os_information.get_hostname())
        table.add_row(i18n.gettext("Kernel"), self.os_information.get_kernel_version())
        table.add_row(i18n.gettext("Home"), self.os_information.get_home_directory())
        table.add_row(i18n.gettext("Usuario"), self.os_information.get_user())
        table.add_row(i18n.gettext("Shell"), self.os_information.get_shell())
        
        table.styles.padding = 1
        table.styles.margin = 1
        table.styles.height = "88vh"
        table.styles.width = "100%"