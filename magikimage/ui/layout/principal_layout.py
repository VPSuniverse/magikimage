from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from ui.sidebar import Sidebar
from ui.main_content import MainContent
from ui.footer import FooterContent

class PrincipalLayout(HorizontalGroup):
  
  def compose(self) -> ComposeResult:
    main_content = MainContent()
    yield Sidebar(main_content)
    yield main_content
    yield FooterContent()