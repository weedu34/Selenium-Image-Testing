from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import time

class TestProductImages:
    """Test class for product image testing"""
    
    def test_hoodie_image(self, driver):
        """Test hoodie product image"""
        self._test_single_image(driver, "hoodie-2-324x324.jpg", "Hoodie")
    
    def test_tshirt_image(self, driver):
        """Test t-shirt product image"""
        self._test_single_image(driver, "tshirt-2-324x324.jpg", "T-Shirt")
    
    def test_sunglasses_image(self, driver):
        """Test sunglasses product image"""
        self._test_single_image(driver, "sunglasses-2-324x324.jpg", "Sunglasses")
    
    def test_beanie_image(self, driver):
        """Test beanie product image"""
        self._test_single_image(driver, "beanie-2-324x324.jpg", "Beanie")
    
    def _test_single_image(self, driver, image_name, product_type):
        """Helper method to test a specific product image"""
        # Find image by filename
        image = driver.find_element(By.XPATH, f"//img[contains(@src, '{image_name}')]")
        
        # Assertions for pytest
        assert image.is_displayed(), f"{product_type} image should be visible"
        assert image.get_attribute('src'), f"{product_type} image should have src attribute"
        
        # Print test info
        print(f"\n🛍️ Testing {product_type}:")
        print("-" * 25)
        print(f"✅ Image found: {image_name}")
        print(f"📍 Source: {image.get_attribute('src')}")
        print(f"🏷️ Alt text: '{image.get_attribute('alt') or 'MISSING ALT TEXT'}'")
        
        # Size validation
        size = image.size
        expected_size = 324
        print(f"📏 Size: {size['width']}x{size['height']} (Expected: {expected_size}x{expected_size})")
        
        # Assert size is reasonable
        assert size['width'] > 0, f"{product_type} image width should be greater than 0"
        assert size['height'] > 0, f"{product_type} image height should be greater than 0"
        
        # Hover test
        actions = ActionChains(driver)
        actions.move_to_element(image).perform()
        time.sleep(1)
        print("🖱️ Hover test: ✅")

    @pytest.mark.parametrize("image_name,product_type", [
        ("hoodie-2-324x324.jpg", "Hoodie"),
        ("tshirt-2-324x324.jpg", "T-Shirt"),
        ("sunglasses-2-324x324.jpg", "Sunglasses"),
        ("beanie-2-324x324.jpg", "Beanie"),
        ("cap-2-324x324.jpg", "Cap"),
        ("polo-2-324x324.jpg", "Polo")
    ])
    def test_multiple_images_parametrized(self, driver, image_name, product_type):
        """Test multiple images using pytest parametrize"""
        self._test_single_image(driver, image_name, product_type)

# Standalone test functions (alternative to class-based)
def test_all_images_accessibility(driver):
    """Test that all product images have proper accessibility"""
    product_images = [
        "hoodie-2-324x324.jpg", "tshirt-2-324x324.jpg", 
        "sunglasses-2-324x324.jpg", "beanie-2-324x324.jpg"
    ]
    
    missing_alt_images = []
    
    for img_name in product_images:
        try:
            image = driver.find_element(By.XPATH, f"//img[contains(@src, '{img_name}')]")
            alt_text = image.get_attribute('alt')
            
            if not alt_text or alt_text.strip() == "":
                missing_alt_images.append(img_name)
                
        except Exception as e:
            pytest.fail(f"Could not find image {img_name}: {e}")
    
    # This will likely fail and show you which images need alt text
    assert len(missing_alt_images) == 0, f"Images missing alt text: {missing_alt_images}"

def test_image_click_navigation(driver):
    """Test that clicking an image navigates to product page"""
    original_url = driver.current_url
    
    # Click on hoodie image
    hoodie_image = driver.find_element(By.XPATH, "//img[contains(@src, 'hoodie-2-324x324.jpg')]")
    hoodie_image.click()
    time.sleep(2)
    
    # Verify navigation occurred
    assert driver.current_url != original_url, "Clicking image should navigate to product page"
    print(f"✅ Navigation successful: {driver.current_url}")