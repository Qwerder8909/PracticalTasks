from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
s=Service('C:/project/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://qahacking.guru/")
time.sleep(5)
driver.set_window_size(1366,768)
fullName = driver.find_element(By.ID, "mod-rscontact-full-name-91")
driver.execute_script('return arguments[0].scrollIntoView(true);', fullName)
driver.find_element(By.ID, "mod-rscontact-full-name-91").click()
driver.find_element(By.ID, "mod-rscontact-full-name-91").send_keys("demo")
driver.find_element(By.ID, "mod-rscontact-email-91").click()
driver.find_element(By.ID, "mod-rscontact-email-91").send_keys("demo@demo.rt")
driver.find_element(By.ID, "mod-rscontact-mobile-phone-91").click()
driver.find_element(By.ID, "mod-rscontact-mobile-phone-91").send_keys("89548754758")
driver.find_element(By.ID, "mod-rscontact-subject-91").click()
driver.find_element(By.ID, "mod-rscontact-subject-91").send_keys("demo")
driver.find_element(By.ID, "mod-rscontact-submit-btn-91").click()
time.sleep(5)