# Selenium-Image-Testing


# Automated Selenium Image Testing Pipeline

A comprehensive, data-driven web automation project using Python and Selenium to discover, test, and validate images on e-commerce websites. This project features an automated pipeline that discovers images, saves them to CSV, and runs comprehensive tests with detailed reporting.

## 🚀 Project Overview

This project automates the complete image testing workflow for web applications:

1. **🔍 Discovery Phase**: Automatically finds all images on a webpage and saves metadata to CSV
2. **🧪 Testing Phase**: Reads from CSV and runs comprehensive automated tests
3. **📊 Reporting Phase**: Generates detailed test reports and tracks results over time

**Target Site**: `http://demostore.supersqa.com/`

## ⭐ Key Features

### Automated Discovery
- **Smart Image Detection**: Finds and categorizes all images automatically
- **Metadata Extraction**: Captures filename, URL, alt text, dimensions, position
- **CSV Storage**: Saves all data in structured CSV format for easy analysis


### Comprehensive Testing
- **Data-Driven Tests**: Reads test cases from CSV files
- **Multi-Level Testing**: Visibility, accessibility, interaction, HTTP loading
- **Result Tracking**: Updates CSV with test results and timestamps
- **Pytest Integration**: Professional test framework with detailed reporting

### Advanced Reporting
- **Test Statistics**: Pass/fail rates by category
- **Accessibility Audits**: Missing alt text identification
- **Historical Tracking**: Track test results over time
- **Export Capabilities**: CSV and HTML report generation

## 🛠️ Prerequisites

### Required Software
- **Python 3.7+**
- **Google Chrome Browser**
- **ChromeDriver** (automatically managed)

### Python Dependencies
```bash
pip install selenium pytest
```

## 📁 Project Structure

```
automated-selenium-testing/
│
├── find_images.py
│  
├── test_images.py
├── run_automation.py
├── requirements.txt 
└──  README.md
    
```

## 🚀 Quick Start

### Option 1: Automated Pipeline (Recommended)

Run the complete automated pipeline:

```bash
# Install dependencies
pip install -r requirements.txt

# Run complete pipeline (discovery + testing + reporting)
python run_automation.py

```

### Option 2: Step-by-Step Execution

```bash
# Step 1: Discover images and save to CSV
python find_images.py


```

### Option 3: Pytest Integration

```bash
# Run pytest tests using CSV data
pytest test_images.py -v -s

# Run specific test categories
pytest test_images.py::TestAutomatedImages::test_product_images_from_csv -v

# Generate HTML reports
pytest test_images.py --html=report.html --self-contained-html
```

## 📊 CSV Data Structure

The automated pipeline generates a comprehensive CSV file with the following structure:

```csv
id,filename,full_url,alt_text,title,width,height,x_position,y_position,is_displayed,category,discovered_date,test_status,test_results,last_tested
1,hoodie-2-324x324.jpg,http://demostore.supersqa.com/wp-content/uploads/2018/06/hoodie-2-324x324.jpg,,,,324,324,0,0,True,product,2025-01-15 10:30:00,passed,"{""found"": true, ""displayed"": true}",2025-01-15 10:35:00
```

### CSV Fields Explained:
- **Basic Info**: `id`, `filename`, `full_url`, `alt_text`, `title`
- **Dimensions**: `width`, `height`, `x_position`, `y_position`
- **Status**: `is_displayed`, `category`
- **Tracking**: `discovered_date`, `test_status`, `test_results`, `last_tested`

## 🎯 Testing Categories

### Image Categories
- **🛍️ Product**: Product images, items for sale
- **🏢 Logo**: Company logos, branding elements  
- **🔧 UI Element**: Icons, buttons, interface components
- **📷 Other**: Miscellaneous images

### Test Types
- **👁️ Visibility**: Is the image displayed and visible?
- **🏷️ Accessibility**: Does the image have proper alt text?
- **📏 Dimensions**: Are the image dimensions correct?
- **🖱️ Interactions**: Hover effects, click functionality
- **🌐 Loading**: Does the image URL return HTTP 200?

## 💡 Advanced Usage

### Custom URL Testing
```bash
python run_pipeline.py --url "https://your-site.com" --csv "your_images.csv"
```

### Category-Specific Testing
```bash
# Test only product images
python run_automation.py--categories product

# Test multiple categories
python run_automation.py --categories product logo ui_element
```

### Limited Testing
```bash
# Test maximum 5 images
python run_automation.py --max-images 5

# Report only (skip discovery and testing)
python run_automation.py --report-only
```



## 📈 Sample Output

### Discovery Phase
```
🔍 Discovering images on: http://demostore.supersqa.com/
📊 Found 16 images
✅ Saved 16 images to discovered_images.csv

📊 Image Summary by Category:
  Product: 12 images
  Logo: 1 images
  Other: 3 images
```

### Testing Phase
```
🧪 Testing 12 images...

[1/12] Testing: hoodie-2-324x324.jpg
  ✅ PASSED - hoodie-2-324x324.jpg
     Displayed: True
     Has Alt Text: False
     Size: 324x324

[2/12] Testing: tshirt-2-324x324.jpg
  ✅ PASSED - tshirt-2-324x324.jpg
     Displayed: True
     Has Alt Text: False
     Size: 324x324
```

### Report Phase
```
📊 COMPREHENSIVE IMAGE TEST REPORT
==================================================
Total Images: 16
Tested: 12
Passed: 11
Failed: 1
Pending: 4

📋 BY CATEGORY:
  Product: 11/12 tested, 12 total
  Logo: 1/1 tested, 1 total
  Other: 0/3 tested, 3 total

⚠️ ACCESSIBILITY ISSUES:
  12 product images missing alt text:
    - hoodie-2-324x324.jpg
    - tshirt-2-324x324.jpg
    - sunglasses-2-324x324.jpg
    - beanie-2-324x324.jpg
    - cap-2-324x324.jpg
```

## 🔧 Customization

### Adding New Test Types

Extend the `test_single_image` method in `AutomatedImageTester`:

```python
def test_single_image(self, driver, image_info):
    # Add your custom tests here
    results["custom_test"] = your_custom_test_logic()
    return status, results
```

### Custom Image Categorization

Modify the `categorize_image` function in `image_discovery.py`:

```python
def categorize_image(filename, alt_text):
    # Add your categorization logic
    if "your_pattern" in filename.lower():
        return "your_category"
    # ... existing logic
```

### Custom Report Formats

Extend `generate_test_report` to add new report sections:

```python
def generate_custom_report(csv_file):
    # Your custom reporting logic
    pass
```

## 🚨 Troubleshooting

### Common Issues

**CSV File Not Found**
```bash
# Solution: Run discovery first
python image_discovery.py
```

**ChromeDriver Issues**
```bash
# Solution: Install webdriver-manager
pip install webdriver-manager
```

**Element Not Found Errors**
- Ensure the target website is accessible
- Check that image filenames match exactly
- Verify page loading is complete

**Memory Issues with Large Sites**
```bash
# Solution: Limit testing scope
python run_pipeline.py --max-images 20 --categories product
```

### Debug Mode

Enable verbose logging:
```bash
# Detailed pytest output
pytest test_automated_images.py -v -s --tb=long

# Chrome browser visible (remove headless)
# Edit image_discovery.py and comment out: chrome_options.add_argument("--headless")
```

## 📊 Performance Tips

- **Use `--headless` mode** for faster discovery
- **Limit test scope** with `--max-images` for development
- **Test specific categories** instead of all images
- **Use pytest markers** to separate slow tests

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Add your changes with tests
4. Update CSV structure documentation if needed
5. Commit changes (`git commit -m 'Add amazing feature'`)
6. Push to branch (`git push origin feature/amazing-feature`)
7. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support & Resources

- **Issues**: [GitHub Issues](../../issues)
- **Documentation**: [Project Wiki](../../wiki)
- **Examples**: See `examples/` directory
- **API Reference**: See inline code documentation

### Useful Resources
- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)
- [CSV Module Documentation](https://docs.python.org/3/library/csv.html)
- [Demo Store Site](http://demostore.supersqa.com/)

---

**🤖 Automated Testing Made Simple! ✨**

*Transform your image testing from manual to fully automated with data-driven insights.*