import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # Start browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Provide driver to test
    yield driver

    # Teardown
    driver.quit()