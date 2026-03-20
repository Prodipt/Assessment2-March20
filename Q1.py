
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.prokabaddi.com/")
driver.maximize_window()

driver.implicitly_wait(15)

driver.find_element(By.LINK_TEXT, "Standings").click()


name = driver.find_element(By.XPATH, "(//div[@class = 'team-name'])[8]")

Total = driver.find_element(By.XPATH, "(//div[@class = 'table-data matches-play'])[8]")

Won = driver.find_element(By.XPATH, "(//div[@class = 'table-data matches-won'])[8]")

Lost = driver.find_element(By.XPATH, "(//div[@class = 'table-data matches-lost'])[8]")

ScoreDiff = driver.find_element(By.XPATH, "(//div[@class = 'table-data score-diff'])[8]")

Points = driver.find_element(By.XPATH, "(//div[@class = 'table-data points'])[8]")

print("Name of the Teams: ",name.text)
print("Total Matches :",Total.text)
print("Matches Won : " ,Won.text)
print("Matches Lost: " ,Lost.text)
print("Score Difference: ",ScoreDiff.text)
print("Total Points: ", Points.text)



driver.close()
driver.quit()