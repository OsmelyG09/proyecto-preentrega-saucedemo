from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL objetivo
BASE_URL = "https://www.saucedemo.com/"

# Localizadores principales
LOCATORS = {
    "username_input": (By.ID, "user-name"),
    "password_input": (By.ID, "password"),
    "login_button": (By.ID, "login-button"),
    "products_title": (By.CLASS_NAME, "title"),
    "error_message": (By.XPATH, "//h3[@data-test='error']"),
    "add_to_cart_backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
    "cart_badge": (By.CLASS_NAME, "shopping_cart_badge"),
}

def login(driver, username, password, timeout=10):
    """
    Función auxiliar para realizar inicio de sesión en SauceDemo.
    """
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, timeout)
    
    # Espera explícita de campos e inserción de credenciales
    user_field = wait.until(EC.visibility_of_element_located(LOCATORS["username_input"]))
    pass_field = wait.until(EC.visibility_of_element_located(LOCATORS["password_input"]))
    login_btn = wait.until(EC.element_to_be_clickable(LOCATORS["login_button"]))
    
    user_field.clear()
    user_field.send_keys(username)
    pass_field.clear()
    pass_field.send_keys(password)
    login_btn.click()

def get_text_element(driver, locator, timeout=10):
    """
    Obtiene el texto de un elemento esperando su visibilidad previa.
    """
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.visibility_of_element_located(locator))
    return element.text