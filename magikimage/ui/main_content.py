from textual.widgets import Static
from textual.containers import VerticalGroup
class MainContent(VerticalGroup):
    def compose(self):
        yield Static("Seleccione una opción del panel.", id="output", classes="main") 