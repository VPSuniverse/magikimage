from textual.widgets import Static
from textual.containers import VerticalGroup

class InfoContent(VerticalGroup):
    def compose(self):
        yield Static("Descripción de la opción seleccionada.", classes="footer") 
    
    def on_mount(self):
        self.styles.width = 40
        self.styles.padding = 1