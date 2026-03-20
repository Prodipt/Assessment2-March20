from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

UserName = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder = 'Username']")))
UserName.send_keys("standard_user")

Password = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder = 'Password']")))
Password.send_keys("secret_sauce")

Login = wait.until(EC.visibility_of_element_located((By.ID, 'login-button')))
Login.click()

print("\n")
print("Logged In Successfully!!!\n")

title = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class = 'title']")))
print("Page Title: ", title.text, "\n")

Products = driver.find_elements(By.XPATH, "//div[@class= 'inventory_item_name ']")

Prices = driver.find_elements(By.XPATH, "//div[@class= 'inventory_item_price']")

print("Here Are The Information Of Products!!!\n")

j=1
for i in range(len(Products)):
    print("Product: ", j ," ", Products[i].text, "of Price: ", Prices[i].text)
    j+=1

print("\n")

fourth = driver.find_element(By.XPATH, "//div[@class = 'inventory_item_img']")

fourth.click()

Add_to_cart = driver.find_element(By.ID, "add-to-cart")
Add_to_cart.click()

print(" 1 Item Added To Your Card Successfully!!! ")



driver.quit()