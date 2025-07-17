from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time

driver = webdriver.Chrome()
driver.get("https://monkeytype.com")


time.sleep(5)

pyautogui.click()
time.sleep(1)

words = driver.find_elements(By.CLASS_NAME, "word")
text_to_type = " ".join(word.text for word in words)

for char in text_to_type:
    pyautogui.write(char)
