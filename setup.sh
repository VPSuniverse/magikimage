#!/bin/bash

msgfmt src/locales/en.po -o src/locales/en.mo
msgfmt src/locales/es.po -o src/locales/es.mo

# Crear un entorno virtual
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate

# Instalar las dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python3 src/main.py