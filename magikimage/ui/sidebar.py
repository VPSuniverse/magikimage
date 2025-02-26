from textual import on
from textual.widgets import Button
from textual.containers import VerticalScroll, VerticalGroup
from textual.app import ComposeResult
from ui.main_content import MainContent

class Sidebar(VerticalGroup):
    def compose(self) -> ComposeResult:
        self.buttons = [
            Button("Información", id="info_button"),
            Button("Instalar Aplicaciones", id="install_button"),
            Button("Actualizar Sistema", id="update_button"),
            Button("Chequeos de Seguridad", id="security_button"),
            Button("Salir", id="exit_button", variant="error"),
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
            
    @on(Button.Pressed, "#info_button")
    def show_system_info(self) -> None:
        main_content = self.app.query_one("MainContent")
        main_content.show_system_info()
    
    @on(Button.Pressed, "#install_button")
    def show_install_applications(self) -> None:
        main_content = self.app.query_one("MainContent")
        main_content.show_install_applications()
    
    @on(Button.Pressed, "#update_button")
    def show_update_system(self) -> None:
        main_content = self.app.query_one("MainContent")
        main_content.show_update_system()
    
    @on(Button.Pressed, "#security_button")
    def show_security_checks(self) -> None:
        main_content = self.app.query_one("MainContent")
        main_content.show_security_checks()
    
    @on(Button.Pressed, "#exit_button")
    def exit_app(self) -> None:
        self.app.exit()
