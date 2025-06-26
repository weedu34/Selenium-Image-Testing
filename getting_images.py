from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()

try:
    driver.get("http://demostore.supersqa.com/")
    
    all_images = driver.find_elements(By.TAG_NAME, "img")
    print("Length of images:", len(all_images))
    # Organize images by type
    product_images = []
    logo_images = []
    other_images = []
    
    for img in all_images:
        src = img.get_attribute("src")
        alt_text = img.get_attribute("alt") or ""
        
        if src:
            filename = os.path.basename(src)
            
            # Categorize images based on alt text or filename
            if "product" in alt_text.lower() or "item" in alt_text.lower():
                product_images.append({"filename": filename, "alt": alt_text, "src": src})
            elif "logo" in alt_text.lower() or "brand" in alt_text.lower():
                logo_images.append({"filename": filename, "alt": alt_text, "src": src})
            else:
                other_images.append({"filename": filename, "alt": alt_text, "src": src})
    
    # Print categorized results
    print("PRODUCT IMAGES:")
    for img in product_images:
        print(f"  - {img['filename']} (Alt: {img['alt']})")
    
    print("\nLOGO IMAGES:")
    for img in logo_images:
        print(f"  - {img['filename']} (Alt: {img['alt']})")
    
    print("\nOTHER IMAGES:")
    for img in other_images:
        print(f"  - {img['filename']} (Alt: {img['alt']})")

finally:
    driver.quit()