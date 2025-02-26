from textual.widgets import Static
from textual.containers import VerticalGroup

class FooterContent(VerticalGroup):
    def compose(self):
        yield Static("Descripción de la opción seleccionada.", classes="footer") 