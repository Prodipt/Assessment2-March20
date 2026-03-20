from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.shine.com/registration/")
driver.maximize_window()

driver.implicitly_wait(15)

driver.find_element(By.XPATH, "//input[@type='file']").send_keys(r"C:\Users\praso\Downloads\ChatGPT Image Mar 6, 2026, 11_45_38 PM.png")

print("Resume Uploaded Successfully ")

sleep(5)
driver.close()
driver.quit()