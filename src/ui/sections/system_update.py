import asyncio

from textual.widgets import Static, Label, Button, DataTable
from services.i18n import i18n
from textual.app import ComposeResult
from textual.containers import VerticalScroll
from services.packages.package_manager import PackageManager
from textual import on, work

class SystemUpdate(Static):
  package_manager = PackageManager()
  
  def compose(self) -> ComposeResult:
    yield DataTable()
    yield Button(i18n.gettext("Upgrade all packages"), id="update_button", variant="success", disabled=True)
    
  def on_mount(self) -> None:
    self.styles.width = "100%"
    self.styles.padding = 1
    self.styles.margin = 1
    self.styles.align_horizontal = "center"
    self.styles.align_vertical = "middle"
    for data_table in self.query(DataTable):
      data_table.loading = True
      self.load_data(data_table)
      data_table.styles.width = "100%"
    update_button = self.query_one("#update_button")
    update_button.styles.width = "100%"
    update_button.styles.margin = 1
    update_button.styles.align_horizontal = "center"
    update_button.styles.align_vertical = "middle"
    
    
  @work
  async def load_data(self, data_table: DataTable) -> None:
    update_button = self.query_one("#update_button")
    data_table.add_columns(i18n.gettext("Upgradable packages"))
    list_upgradable = await self.package_manager.list_upgradable_packages()
    if not list_upgradable:
      data_table.add_row(i18n.gettext("No hay actualizaciones disponibles."))
      update_button.disabled = True
      return
    else:
      for package in list_upgradable:
        data_table.add_row(package)
      update_button.disabled = False
    data_table.loading = False

    
  @on(Button.Pressed, "#update_button")
  async def update_system(self) -> None:
    await self.package_manager.update_all_packages()
    self.refresh(recompose=True)
