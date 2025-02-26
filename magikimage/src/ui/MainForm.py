import npyscreen
import src.ui.OptionsArea as OptionsArea

class MainForm(npyscreen.FormBaseNew):
    def create(self):
        # Set Events
        self.add_event_hander("event_option_select", self.event_option_select)
        
        y, x = self.useable_space()
        
        # Set Sections
        self.optionBox = self.add(OptionsArea.OptionsArea, name="Options", value=0, relx=1, max_width=x // 5, rely=2,
                                   max_height=-5)
        
        
        # Create Sections
        self.optionBox.create()
    
    def event_option_select(self, event):
        self.parentApp.switchForm("OPTIONS")