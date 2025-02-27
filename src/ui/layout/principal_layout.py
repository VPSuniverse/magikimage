from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from ui.sidebar import Sidebar
from ui.main_content import MainContent
from ui.info_content import InfoContent

class PrincipalLayout(HorizontalGroup):
  
  def compose(self) -> ComposeResult:
    yield Sidebar()
    yield MainContent()
    yield InfoContent()