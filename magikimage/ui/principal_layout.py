from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from ui.sidebar import Sidebar
from ui.main_content import MainContent
from ui.footer import FooterContent

class PrincipalLayout(HorizontalGroup):
  
  def compose(self) -> ComposeResult:
    yield Sidebar()
    yield MainContent()
    yield FooterContent()