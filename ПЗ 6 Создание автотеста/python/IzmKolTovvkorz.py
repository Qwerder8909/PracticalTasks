from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
s=Service('C:/project/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://qahacking.guru/")
driver.set_window_size(1366,768)
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/nav/div[2]/ul/li[3]/a").click()
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/nav/div[2]/ul/li[3]/a").click()

driver.find_element(By.XPATH, "//*[@id=\"comjshop_list_product\"]/div[1]/div[1]/div/div/div[3]/div[7]/a[1]").click()
driver.find_element(By.XPATH, "//*[@id=\"comjshop\"]/form/table[1]/tbody/tr[2]/td[4]/div[2]/input").click()
driver.find_element(By.XPATH, "//*[@id=\"comjshop\"]/form/table[1]/tbody/tr[2]/td[4]/div[2]/input").clear()
driver.find_element(By.XPATH, "//*[@id=\"comjshop\"]/form/table[1]/tbody/tr[2]/td[4]/div[2]/input").send_keys("10")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div[2]/form/table[1]/tbody/tr[2]/td[4]/div[2]/span/img").click()
time.sleep(5)