import gettext
import os

class I18n:
    def __init__(self, lang='en'):
        self.lang = lang
        # Inicializa self.translations con NullTranslations para asegurar que siempre exista.
        self.translations = gettext.NullTranslations() 
        self.translations = self.load_translations()

    def load_translations(self):
        locales_dir = os.path.join(os.path.dirname(__file__), '../locales')
        mo_path = os.path.join(locales_dir, f"{self.lang}.mo")
        
        loaded_translations = None
        try:
            with open(mo_path, 'rb') as f:
                loaded_translations = gettext.GNUTranslations(f)
        except FileNotFoundError:
            # Si no se encuentra el archivo del idioma específico, intenta recurrir al inglés si no es ya inglés.
            if self.lang != 'en':
                en_mo_path = os.path.join(locales_dir, "en.mo")
                try:
                    with open(en_mo_path, 'rb') as f:
                        loaded_translations = gettext.GNUTranslations(f)
                except (FileNotFoundError, Exception): # Captura también corrupción de en.mo
                    # Si en.mo tampoco se encuentra o está corrupto, loaded_translations permanecerá None.
                    pass 
            # Si self.lang es 'en' y en.mo no se encuentra, loaded_translations permanecerá None.
        except Exception: # Captura otros errores al cargar el mo_path original, como corrupción
            # Si el archivo .mo original está corrupto, loaded_translations permanecerá None.
            # Podrías intentar cargar 'en' aquí también como fallback si el original corrupto no era 'en'
            if self.lang != 'en':
                en_mo_path = os.path.join(locales_dir, "en.mo")
                try:
                    with open(en_mo_path, 'rb') as f:
                        loaded_translations = gettext.GNUTranslations(f)
                except (FileNotFoundError, Exception): # Captura también corrupción de en.mo
                    pass

        # Si no se cargó con éxito ningún archivo .mo, devuelve NullTranslations.
        if loaded_translations is None:
            return gettext.NullTranslations()
        return loaded_translations
    
    def change_translations(self, lang):
        self.lang = lang
        self.translations = self.load_translations()

    def gettext(self, message):
        # self.translations siempre será un objeto Translations válido (GNUTranslations o NullTranslations).
        return self.translations.gettext(message) 

i18n = I18n()