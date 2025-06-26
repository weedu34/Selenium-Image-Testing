# Selenium-Image-Testing


A comprehensive web automation project using Python and Selenium to test and validate product images on e-commerce websites. This project demonstrates automated image testing, accessibility validation, and user interaction testing.

## 🚀 Project Overview

This project automates the testing of product images on the demo e-commerce site `http://demostore.supersqa.com/`. It includes functionality to:

- Discover and categorize all images on a webpage
- Test specific product images for visibility, dimensions, and accessibility
- Validate image properties (alt text, src attributes, etc.)
- Test user interactions (hover effects, click navigation)
- Generate comprehensive test reports using pytest

## 📋 Features

### Image Discovery & Categorization
- **Automatic Image Detection**: Finds all images on a webpage
- **Smart Categorization**: Organizes images into product, logo, and other categories
- **Property Extraction**: Extracts filename, alt text, source URL, and dimensions

### Image Testing
- **Visibility Testing**: Verifies images are properly displayed
- **Accessibility Testing**: Checks for missing alt text and proper attributes
- **Dimension Validation**: Ensures images meet expected size requirements
- **Interaction Testing**: Tests hover effects and click functionality

### Test Framework Integration
- **Pytest Integration**: Professional test framework with fixtures and reporting
- **Parametrized Testing**: Efficiently test multiple images with single test functions
- **Cross-browser Support**: Easily configurable for different browsers

## 🛠️ Prerequisites

Before running this project, ensure you have the following installed:

### Required Software
- **Python 3.7+**
- **Google Chrome Browser**
- **ChromeDriver** (automatically managed with webdriver-manager)

### Python Packages
```bash
pip install selenium pytest webdriver-manager
```

## 📁 Project Structure

```
selenium-image-testing/
│
├── conftest.py              # Pytest fixtures and configuration
├── test_selenium.py         # Main test file with image testing classes
├── image_discovery.py       # Standalone script for image discovery
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🔧 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <https://github.com/weedu34/Selenium-Image-Testing.git>
   cd selenium-image-testing
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv selenium_image_testing_venv
   source selenium_image_testing_venv/bin/activate  # On Windows: venv\Scripts\activate.bat
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Chrome installation**
   - Ensure Google Chrome is installed on your system
   - ChromeDriver will be automatically downloaded and managed

## 🚀 Usage

### Running Image Discovery Script

The standalone image discovery script categorizes all images on the demo store:

```bash
python image_discovery.py
```

**Expected Output:**
```
Length of images: 16
PRODUCT IMAGES:
  - (No product images found with current criteria)

LOGO IMAGES:
  - (No logo images found with current criteria)

OTHER IMAGES:
  - album-1-324x324.jpg (Alt: )
  - beanie-2-324x324.jpg (Alt: )
  - hoodie-2-324x324.jpg (Alt: )
  # ... more images
```

### Running Pytest Tests

#### Run All Tests
```bash
pytest test_selenium.py -v -s
```

#### Run Specific Test Classes
```bash
# Run only the TestProductImages class
pytest test_selenium.py::TestProductImages -v -s

# Run a specific test method
pytest test_selenium.py::TestProductImages::test_hoodie_image -v -s
```

#### Run Parametrized Tests
```bash
# Run the parametrized test for multiple images
pytest test_selenium.py::TestProductImages::test_multiple_images_parametrized -v -s
```

#### Run Accessibility Tests
```bash
# Test for missing alt text (this will likely fail and show issues)
pytest test_selenium.py::test_all_images_accessibility -v -s
```

#### Run Navigation Tests
```bash
# Test image click functionality
pytest test_selenium.py::test_image_click_navigation -v -s
```

## 📊 Test Examples

### Individual Image Testing
Tests specific product images for various properties:
- **Visibility**: Confirms image is displayed on page
- **Source Validation**: Ensures image has valid src attribute
- **Dimension Check**: Validates image width and height
- **Hover Interaction**: Tests mouse hover effects

### Accessibility Testing
Identifies images missing alt text for screen reader compatibility:
```python
def test_all_images_accessibility(driver):
    # Checks all product images for proper alt text
    # Reports which images need accessibility improvements
```

### Navigation Testing
Verifies that clicking product images navigates to product detail pages:
```python
def test_image_click_navigation(driver):
    # Clicks on product images
    # Validates navigation to product pages
```

## 🧪 Test Configuration

### Browser Configuration
The project uses Chrome by default with these options:
- **Maximized Window**: `--start-maximized`
- **Configurable Options**: Easy to add headless mode or other browser options

### Fixture Setup
```python
@pytest.fixture
def driver():
    """Creates WebDriver instance with automatic cleanup"""
    # Setup Chrome driver
    # Navigate to demo store
    # Yield driver to tests
    # Automatic cleanup after tests
```

## 📈 Test Reports

### Verbose Output
Run tests with `-v -s` flags to see detailed output:
```bash
pytest test_selenium.py -v -s
```

### HTML Reports (Optional)
Install pytest-html for detailed HTML reports:
```bash
pip install pytest-html
pytest test_selenium.py --html=report.html --self-contained-html
```

## 🎯 Targeted Images

The project currently tests these specific product images:
- **hoodie-2-324x324.jpg** - Hoodie product image
- **tshirt-2-324x324.jpg** - T-shirt product image  
- **sunglasses-2-324x324.jpg** - Sunglasses product image
- **beanie-2-324x324.jpg** - Beanie product image
- **cap-2-324x324.jpg** - Cap product image
- **polo-2-324x324.jpg** - Polo shirt product image

## 🔍 Common Issues & Solutions

### ChromeDriver Issues
If you encounter ChromeDriver issues:
```bash
# Install webdriver-manager for automatic management
pip install webdriver-manager
```

### Element Not Found
If tests fail with element not found:
- Check that the demo site is accessible
- Verify image filenames match exactly
- Ensure page has fully loaded before testing

### Missing Alt Text Failures
The accessibility test intentionally fails to highlight missing alt text:
- This is expected behavior for the demo site
- Use this to identify accessibility improvements needed

## 🛡️ Best Practices

### Test Organization
- **Class-based tests** for related functionality
- **Parametrized tests** for testing multiple similar items
- **Fixtures** for setup and teardown

### Error Handling
- Comprehensive try-catch blocks
- Meaningful error messages
- Automatic browser cleanup

### Accessibility
- Alt text validation
- Screen reader compatibility checks
- WCAG compliance testing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues or have questions:
1. Check the [Issues](../../issues) section
2. Create a new issue with detailed description
3. Include error messages and system information

## 🔗 Useful Resources

- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)
- [Demo Store Site](http://demostore.supersqa.com/)

---

**Happy Testing! 🧪✨**