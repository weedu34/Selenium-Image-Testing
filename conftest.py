import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    """Create a WebDriver instance for testing"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://demostore.supersqa.com/")  # Navigate once per test
    
    yield driver
    driver.quit()