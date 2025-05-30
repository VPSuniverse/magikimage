from textual.app import ComposeResult, App
from textual.widgets import Static, Button, Log, Checkbox, Label
from textual.containers import VerticalScroll, Horizontal, Vertical
from services.applications.application_repository import ApplicationRepository, Application
from services.packages.package_manager import PackageManager
from services.i18n import i18n
from textual import work, on

class InstallAppsSection(Static):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.app_repo = ApplicationRepository()
        # Pasar self.app a PackageManager si las estrategias necesitan acceso a la app (para logs, etc.)
        self.package_manager = PackageManager(app_instance=self.app) 
        self.selected_apps_to_install = set()

    def compose(self) -> ComposeResult:
        yield Label(i18n.gettext("Available Applications to Install:"))
        with VerticalScroll(id="app_list_scroll_id", classes="app_list_scroll_class"):
            applications = self.app_repo.get_all_applications()
            if not applications:
                yield Label(i18n.gettext("No applications defined in configuration."))
            else:
                for app_item in applications: # Renombrado para evitar conflicto con self.app
                    yield Horizontal(
                        Checkbox(app_item.name, id=f"cb_{app_item.id}"), 
                        Label(f" ({app_item.description})", classes="app_description_label")
                    )
        
        yield Button(
            i18n.gettext("Install Selected Applications"), 
            id="install_selected_apps_button", 
            variant="primary"
        )
        yield Log(id="install_log", auto_scroll=True, highlight=True, classes="install_log_class")

    def on_mount(self) -> None:
        self.styles.padding = 1
        log_widget = self.query_one("#install_log", Log)
        log_widget.write_line(i18n.gettext("Select applications and click install."))
        
        install_button = self.query_one("#install_selected_apps_button", Button)
        if not self.package_manager.strategy.is_supported():
            install_button.disabled = True
            log_widget.write_line(f"[b red]{i18n.gettext('Package manager not supported. Installation disabled.')}[/b red]")
        else:
            install_button.disabled = True # Deshabilitado hasta que se seleccione algo

    @on(Checkbox.Changed)
    def handle_checkbox_change(self, event: Checkbox.Changed) -> None:
        app_id_from_checkbox = event.checkbox.id.replace("cb_", "", 1)
        if event.value:
            self.selected_apps_to_install.add(app_id_from_checkbox)
        else:
            self.selected_apps_to_install.discard(app_id_from_checkbox)
        
        install_button = self.query_one("#install_selected_apps_button", Button)
        if self.package_manager.strategy.is_supported():
            install_button.disabled = not bool(self.selected_apps_to_install)

    @on(Button.Pressed, "#install_selected_apps_button")
    async def on_install_button_pressed(self) -> None:
        log_widget = self.query_one("#install_log", Log)
        if not self.selected_apps_to_install:
            log_widget.write_line(i18n.gettext("No applications selected for installation."))
            return

        install_button = self.query_one("#install_selected_apps_button", Button)
        install_button.disabled = True
        
        log_widget.write_line(f"[b blue]{i18n.gettext('Starting installation process...')}[/b blue]")

        apps_to_process = list(self.selected_apps_to_install) # Copia para iterar
        for app_id_to_install in apps_to_process:
            app_to_install_obj = self.app_repo.find_application_by_id(app_id_to_install)
            if app_to_install_obj:
                log_widget.write_line(f"{i18n.gettext('Preparing to install')} {app_to_install_obj.name}...")
                self.run_install_worker(app_to_install_obj) 
            else:
                log_widget.write_line(f"[yellow]{i18n.gettext('Application with ID')} '{app_id_to_install}' {i18n.gettext('not found.')}[/yellow]")
        
        # El botón se re-habilitará a través de los workers o cambios en checkboxes

    @work(exclusive=False, thread=True)
    async def run_install_worker(self, application_obj: Application) -> None:
        log_widget = self.query_one("#install_log", Log)
        log_widget.write_line(f"{i18n.gettext('Worker started for:')} {application_obj.name}")
        
        success = await self.package_manager.install_application(application_obj)
        
        if success:
            log_widget.write_line(f"[b green]{application_obj.name} {i18n.gettext('installation command executed successfully.')}[/b green]")
            try:
                checkbox = self.query_one(f"#cb_{application_obj.id}", Checkbox)
                checkbox.value = False # Desmarcar después de la instalación exitosa
                self.selected_apps_to_install.discard(application_obj.id) # Asegurar que se quita
            except Exception as e:
                log_widget.write_line(f"[dim]Could not deselect checkbox for {application_obj.name}: {e}[/dim]")
        else:
            log_widget.write_line(f"[b red]{application_obj.name} {i18n.gettext('installation command failed or reported an error.')}[/b red]")

        # Re-evaluar estado del botón de instalación principal después de que un worker termine
        # Esto es un poco simplista si hay muchos workers concurrentes,
        # pero para este caso debería funcionar para reactivar el botón si quedan selecciones.
        install_button = self.query_one("#install_selected_apps_button", Button)
        if self.package_manager.strategy.is_supported():
            install_button.disabled = not bool(self.selected_apps_to_install)
        else:
            install_button.disabled = True