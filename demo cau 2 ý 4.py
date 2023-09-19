from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.get("https://eop.edu.vn/")

dangnhap = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
dangnhap.click()

ten_dang_nhap = driver.find_element(By.ID, "input-username")
ten_dang_nhap.send_keys("")
        
mat_khau = driver.find_element(By.ID, "input-password")
mat_khau.send_keys("2020600522@6")
'''
ten_dang_nhap = driver.find_element(By.ID, "input-username")
ten_dang_nhap.send_keys("2020600522")
        
mat_khau = driver.find_element(By.ID, "input-password")
mat_khau.send_keys("")

ten_dang_nhap = driver.find_element(By.ID, "input-username")
ten_dang_nhap.send_keys("20206005222")
        
mat_khau = driver.find_element(By.ID, "input-password")
mat_khau.send_keys("20206005226")

ten_dang_nhap = driver.find_element(By.ID, "input-username")
ten_dang_nhap.send_keys("2020600522")
        
mat_khau = driver.find_element(By.ID, "input-password")
mat_khau.send_keys("2020600522@6")
'''
dang_nhap = driver.find_element(By.ID, "login-btn")
dang_nhap.click()

