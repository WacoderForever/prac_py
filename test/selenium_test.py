#!/usr/bin/env python3
"""
Simple Selenium test script
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import sys

def test_chrome():
    """Test Chrome browser automation"""
    try:
        print("Testing Chrome browser...")
        
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        # Initialize driver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Test basic functionality
        driver.get("https://www.google.com")
        print(f"Successfully opened Google. Title: {driver.title}")
        
        # Search for something
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium testing")
        search_box.submit()
        
        time.sleep(2)
        print("Search completed successfully!")
        
        driver.quit()
        return True
        
    except Exception as e:
        print(f"Chrome test failed: {e}")
        return False

if __name__ == "__main__":
    print("Selenium Test Script")
    print("-" * 30)
    
    # Test Chrome
    chrome_success = test_chrome()
    
    
    # Summary
    print("\n" + "=" * 30)
    print("Test Summary:")
    print(f"Chrome: {'✓ Working' if chrome_success else '✗ Failed'}")