from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from ui.layout.principal_layout import PrincipalLayout
from textual.containers import Container
from services.i18n import i18n # Importar i18n

class MainApp(App):
    # title ya no se define estáticamente aquí si queremos que sea dinámico desde el inicio
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def on_mount(self) -> None:
        """Se llama cuando la aplicación se monta."""
        self.update_translatable_elements() # Establece el título inicial y otros elementos

    def update_translatable_elements(self) -> None:
        """Actualiza elementos traducibles de la aplicación como el título."""
        self.title = i18n.gettext("Magik Image") # "Magik Image" como msgid

    def compose(self) -> ComposeResult:
        yield Header() # El Header usará self.title reactivamente
        yield Container(
            PrincipalLayout(),
        )
        yield Footer()
        
    def action_toggle_dark(self) -> None:
        """Una acción para alternar el modo oscuro."""
        self.dark = not self.dark # Corregido para usar self.dark
    
    # Eliminado el on_mount original que establecía un título estático.
    # El título ahora se maneja a través de update_translatable_elements.

if __name__ == "__main__":
    app = MainApp()
    app.run()