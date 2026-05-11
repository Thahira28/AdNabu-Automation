from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def test_add_to_cart():

    # Open browser
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.maximize_window()

    # Open website
    driver.get("https://www.saucedemo.com")

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    # Add product to cart
    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()

    time.sleep(2)

    # Open cart
    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    time.sleep(2)

    # Verify product added
    cart_item = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    )

    assert cart_item.is_displayed()

    print("Product added successfully")

    time.sleep(3)

    driver.quit()