from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from ui.layout.principal_layout import PrincipalLayout
from textual.containers import Container

class MainApp(App):
    title = "Magik Image"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]


    def compose(self) -> ComposeResult:
        yield Header()

        yield Container(
            PrincipalLayout(),
        )
        
        yield Footer()
        
    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
    
    def on_mount(self) -> None:
        self.title = "Magik Image"

if __name__ == "__main__":
    app = MainApp()
    app.run()