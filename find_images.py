from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import os

def find_and_save_images():
    driver = webdriver.Chrome()
    driver.get("http://demostore.supersqa.com/")
    
    # Find all images
    images = driver.find_elements(By.TAG_NAME, "img")
    
    # Prepare CSV data
    image_data = []
    for i, img in enumerate(images, 1):
        src = img.get_attribute("src")
        if src:
            filename = os.path.basename(src)
            image_data.append({
                'id': i,
                'filename': filename,
                'url': src,
                'alt_text': img.get_attribute("alt") or "Missing text"
            })
    
    # Save to CSV
    with open('images.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'filename', 'url', 'alt_text'])
        writer.writeheader()
        writer.writerows(image_data)
    
    driver.quit()
    print(f"✅ Found {len(image_data)} images and saved to images.csv")

if __name__ == "__main__":
    find_and_save_images()