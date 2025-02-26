import npyscreen
from src.ui.MainForm import MainForm

class MagikImage(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="Magik Image")