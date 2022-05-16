from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.ig.com/cn/login"
driver.get(url)
time.sleep(10)
login_text = driver.find_element(By.XPATH, "//div[@class='login-form-input-wrapper']//input[@class='login-form-text-input text' and @tabindex='1']")
password = driver.find_element(By.XPATH, "//div[@class='login-form-input-wrapper']//input[@class='login-form-text-input text' and @tabindex='2']")

