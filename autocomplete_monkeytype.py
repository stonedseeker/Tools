from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time

# Set up Chrome driver
driver = webdriver.Chrome()
driver.get("https://monkeytype.com")

# Wait for page to load
time.sleep(5)

# Click anywhere to focus the typing area
pyautogui.click()
time.sleep(1)

# Extract the words to type
words = driver.find_elements(By.CLASS_NAME, "word")
text_to_type = " ".join(word.text for word in words)

# Optional: print it
print(f"Typing: {text_to_type}")

# Type with a small delay to simulate human typing
for char in text_to_type:
    pyautogui.write(char)
    time.sleep(0.005)  # 20 ms per character ~ 300 WPM

# Cleanup
time.sleep(5)
driver.quit()



