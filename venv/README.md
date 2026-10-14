# Pre-Entrega de Proyecto: Automatización SauceDemo

Este repositorio contiene la suite de pruebas automatizadas para la aplicación [SauceDemo](https://www.saucedemo.com/) implementada como parte de la pre-entrega del curso.

## 🎯 Proposito del Proyecto
* Automatización de flujos críticos de navegación y validación funcional en el sitio de pruebas. [www.saucedemo.com](https://www.saucedemo.com)

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.10+
* **Testing Framework:** Pytest
* **Automatización:** Selenium WebDriver
* **Control de Versiones:** Git / GitHub

## 📁 Estructura del Proyecto
* `utils.py`: Módulo de funciones de soporte, constantes y localizadores web.
* `test_saucedemo.py`: Casos de prueba automatizados (Login exitoso, Login fallido, Agregar al carrito).
* `requirements.txt`: Lista de librerías y dependencias necesarias.

proyecto-preentrega-saucedemo/
│
├── tests/
│   └── test_saucedemo.py       # Casos de prueba automatizados (Login, Catálogo, Carrito)
│
├── utils/
│   └── utils.py                # Localizadores web y funciones auxiliares (login, esperas)
│
├── reports/                    # Carpeta para reportes HTML de Pytest
│
├── .gitignore                  # Exclusión de venv, __pycache__, etc.
├── requirements.txt            # Dependencias del proyecto (Selenium, Pytest, etc.)
└── README.md                   # Documentación completa del proyecto

## 🚀 Instrucciones de Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd proyecto-preentrega-saucedemo

2. **Instrucciones de instalación:**
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. **Comando de ejecución y generación de reportes:**
   pytest tests/test_saucedemo.py -v --html=reports/reporte.html