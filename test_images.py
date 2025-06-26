import csv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



# Read images from CSV
def load_images():
    with open('images.csv', 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://demostore.supersqa.com/")
    yield driver
    driver.quit()

# Generate test cases automatically from CSV
class TestImagesFromCSV:
    
    @pytest.mark.parametrize("image_data", load_images(), ids=lambda x: x['filename'])
    def test_image_exists(self, driver, image_data):
        """Test that image exists on page"""
        filename = image_data['filename']
        image = driver.find_element(By.XPATH, f"//img[contains(@src, '{filename}')]")
        assert image.is_displayed(), f"{filename} should be visible"
    
    @pytest.mark.parametrize("image_data", load_images(), ids=lambda x: x['filename'])
    def test_image_has_src(self, driver, image_data):
        """Test that image has source URL"""
        filename = image_data['filename']
        image = driver.find_element(By.XPATH, f"//img[contains(@src, '{filename}')]")
        assert image.get_attribute('src'), f"{filename} should have src attribute"
    
    @pytest.mark.parametrize("image_data", load_images(), ids=lambda x: x['filename'])
    def test_image_size(self, driver, image_data):
        """Test that image has proper dimensions"""
        filename = image_data['filename']
        image = driver.find_element(By.XPATH, f"//img[contains(@src, '{filename}')]")
        size = image.size
        assert size['width'] > 0, f"{filename} width should be > 0"
        assert size['height'] > 0, f"{filename} height should be > 0"