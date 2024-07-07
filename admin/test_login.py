import unittest
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAdmin(unittest.TestCase):

    def setUp(self):
        chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def test_login_failure_incorect_username_password(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        username_field.send_keys("dolly")
        
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("dolly123")
        
        login_button = driver.find_element(By.CSS_SELECTOR, ".oxd-button")

        login_button.click() 
        time.sleep(5)  
        
    def test_login_failure_incorect_password(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        username_field.send_keys("admin")
        
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("dolly123")
        
        login_button = driver.find_element(By.CSS_SELECTOR, ".oxd-button")

        login_button.click() 
        time.sleep(5)  
        
    def test_login_failure_incorect_username(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        username_field.send_keys("dolly")
        
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("admin123")
        
        login_button = driver.find_element(By.CSS_SELECTOR, ".oxd-button")

        login_button.click() 
        time.sleep(5)  
        
    def test_login_success(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        
        username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        username_field.send_keys("admin")
        
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("admin123")
        
        login_button = driver.find_element(By.CSS_SELECTOR, ".oxd-button")
 
        login_button.click() 
        time.sleep(5)  
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
   unittest.main()