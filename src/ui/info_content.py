from textual import on
from textual.widgets import Static, Select
from textual.containers import VerticalScroll, VerticalGroup
from services.i18n import i18n

class InfoContent(VerticalGroup):
    
    def compose(self):
        self.select_language = Select(
                options=[
                    ("English", "en"),
                    ("Español", "es"),
                ],
                id="language_selector",
                value="en"
            )
        
        yield VerticalScroll(
            self.select_language,
            Static ("Descripcion de la aplicacion seleccionada."),
        )
    
    def on_mount(self):
        self.styles.width = 40
        self.styles.padding = 1
        # Verificar si hay un valor seleccionado
        if self.select_language.value != Select.BLANK:
            i18n.change_translations(self.select_language.value)
        else:
            # Establecer un valor predeterminado, por ejemplo, 'en'
            i18n.change_translations('en')
    
    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        i18n.change_translations(event.value)