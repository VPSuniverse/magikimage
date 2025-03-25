import gettext
import os

class I18n:
    def __init__(self, lang='en'):
        self.lang = lang
        self.translations = self.load_translations()

    def load_translations(self):
        locales_dir = os.path.join(os.path.dirname(__file__), '../locales')
        lang_translations = gettext.translation('messages', localedir=locales_dir, languages=[self.lang], fallback=True)
        return lang_translations
    
    def change_translations(self, lang):
        self.lang = lang
        self.translations = self.load_translations()

    def gettext(self, message):
        return self.translations.gettext(message) 

i18n = I18n()