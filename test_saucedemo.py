import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils import login, get_text_element, LOCATORS

@pytest.fixture
def driver():
    """
    Fixture que configura e inicializa el navegador para cada prueba.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)  # Espera implícita global de respaldo
    
    yield driver
    
    driver.quit()  # Cierre limpio del navegador al finalizar cada test

def test_login_exitoso(driver):
    """
    Verifica que un usuario estándar pueda iniciar sesión correctamente.
    """
    login(driver, "standard_user", "secret_sauce")
    
    # Validación: verificar presencia del título 'Products'
    title = get_text_element(driver, LOCATORS["products_title"])
    assert title.upper() == "PRODUCTS"

def test_login_fallido(driver):
    """
    Verifica que se muestre el mensaje de error adecuado ante credenciales inválidas.
    """
    login(driver, "usuario_invalido", "clave_incorrecta")
    
    # Validación: captura del mensaje de error
    error_msg = get_text_element(driver, LOCATORS["error_message"])
    assert "Username and password do not match" in error_msg

def test_agregar_producto_al_carrito(driver):
    """
    Verifica que el contador del carrito se incremente al añadir un producto.
    """
    login(driver, "standard_user", "secret_sauce")
    
    # Agregar mochila al carrito
    driver.find_element(*LOCATORS["add_to_cart_backpack"]).click()
    
    # Validación: verificar badge del carrito con cantidad '1'
    badge_count = get_text_element(driver, LOCATORS["cart_badge"])
    assert badge_count == "1"