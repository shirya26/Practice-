from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)


# driver.find_element(By.xpath("//div[@class='exampleClass']"))
ele = driver.find_element(By.CLASS_NAME,"MV3Tnb")
print(ele.text)
driver.quit()
