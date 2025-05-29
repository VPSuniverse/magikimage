from textual import on
from textual.widgets import Static, Select
from textual.containers import VerticalScroll, VerticalGroup
from services.i18n import i18n
from textual.app import ComposeResult # Import ComposeResult

class InfoContent(VerticalGroup):
    
    def compose(self) -> ComposeResult:
        available_languages = [opt[1] for opt in [("English", "en"), ("Español", "es")]]
        # Asegura que el idioma inicial de i18n sea una de las opciones disponibles
        if i18n.lang not in available_languages:
            # Si el idioma actual de i18n no está en la selección, usa 'en' por defecto
            # y actualiza el estado de i18n.
            i18n.change_translations(available_languages[0])

        self.select_language = Select(
                options=[
                    ("English", "en"),
                    ("Español", "es"),
                ],
                id="language_selector",
                value=i18n.lang # Inicializa Select con el idioma actual de i18n
            )
        
        # Guarda el widget Static para que su contenido pueda ser actualizado si es necesario,
        # aunque app.refresh(recompose=True) debería recrearlo.
        self.description_text = Static(i18n.gettext("Descripcion de la aplicacion seleccionada."))
        
        yield VerticalScroll(
            self.select_language,
            self.description_text,
        )
    
    def on_mount(self) -> None:
        self.styles.width = 40
        self.styles.padding = 1
        # La lógica original en on_mount para configurar i18n basada en el valor de Select
        # ahora se maneja inicializando Select con i18n.lang y asegurando
        # que i18n.lang sea una opción válida en compose.
    
    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        if event.value is not None and str(event.value) != Select.BLANK: # Asegura que event.value sea string para la comparación
            new_lang = str(event.value)
            if new_lang != i18n.lang: # Solo si el idioma realmente cambió
                i18n.change_translations(new_lang)
                # Llama a un método en la app para actualizar elementos no recompuestos automáticamente si es necesario
                if hasattr(self.app, 'update_translatable_elements'):
                    self.app.update_translatable_elements()
                self.app.refresh(recompose=True) # Refresca toda la UI de la aplicación