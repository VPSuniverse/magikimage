from textual.widgets import Static, Label, Button
from services.i18n import i18n
from textual.app import ComposeResult
from textual.containers import VerticalScroll
from services.packages.package_manager import PackageManager
from textual import on

class SystemUpdate(Static):
  package_manager = PackageManager()
  
  def compose(self) -> ComposeResult:
    list_upgradable = self.package_manager.list_upgradable_packages()
    if not list_upgradable:
      yield Label("No hay actualizaciones disponibles.")
      return
    # List all upgradable packages
    label_list= [Label(package) for package in list_upgradable]

    self.package_manager.list_upgradable_packages()
    yield VerticalScroll(
      Label("  Upgradable packages:"),
      *label_list,
      Button(i18n.gettext("Upgrade all packages"), id="update_button", variant="success", disabled=False),
    )
    
  def on_mount(self) -> None:
    self.styles.width = 40
    self.styles.padding = 1
    self.styles.margin = 1
    
  @on(Button.Pressed, "#update_button")
  def update_system(self) -> None:
    self.package_manager.update_all_packages()
