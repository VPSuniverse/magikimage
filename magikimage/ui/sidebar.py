from textual.widgets import Button, Static
from textual.containers import VerticalScroll, VerticalGroup
from textual.app import ComposeResult

class Sidebar(VerticalGroup):
    def compose(self) -> ComposeResult:
        self.buttons = [
            Button("Información", id="info_button"),
            Button("Instalar Aplicaciones", id="install_button"),
            Button("Actualizar Sistema", id="update_button"),
            Button("Chequeos de Seguridad", id="security_button"),
            Button("Salir", id="exit_button"),
        ]
        
        yield VerticalScroll(
            *self.buttons
        )
        
    def on_mount(self) -> None:
        self.styles.width = 30
        self.styles.justify = "center"
        self.styles.padding = 1
        self.styles.dock = "left"
        
        for button in self.buttons:
            button.styles.width = 28
            button.styles.height = 3
            button.styles.margin = 1
            button.styles.text_align = "center"
            button.styles.text_style = "bold"


    def on_button_pressed(self, button: Button) -> None:
        output = self.query_one("#output", Static)
        footer = self.query_one(".footer", Static)

        if button.id == "info_button":
            output.update("Información del sistema operativo...")
            footer.update("Detalles sobre el sistema operativo.")
        elif button.id == "install_button":
            output.update("Aplicaciones disponibles para instalar...")
            footer.update("Detalles sobre las aplicaciones disponibles.")
        elif button.id == "update_button":
            output.update("Actualizando el sistema...")
            footer.update("Detalles sobre el proceso de actualización.")
        elif button.id == "security_button":
            output.update("Realizando chequeos de seguridad...")
            footer.update("Detalles sobre los chequeos de seguridad.") 