from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://game-selenium.netlify.app/")

time.sleep(2)

# Vai até missão 4 (ajuste se precisar clicar antes)
driver.find_element(By.XPATH, "//button[contains(text(),'Missão 4')]").click()

time.sleep(2)

dados = [
    ["001","Intel","i5-10400","CPU","1200","900","10ª geração"],
    ["002","AMD","Ryzen 5 5600G","CPU","1100","850","AM4"],
    ["003","NVIDIA","RTX 3060","GPU","2500","2000","12GB"],
    ["004","AMD","RX 6600","GPU","1800","1400","8GB"],
    ["005","Kingston","16GB","RAM","300","200","DDR4"],
    ["006","Corsair","32GB","RAM","600","450","DDR4"],
    ["007","Samsung","1TB","SSD","500","350","NVMe"],
    ["008","WD","500GB","SSD","300","200","SATA"],
    ["009","Corsair","600W","Fonte","400","280","80 Plus"],
    ["010","ASUS","B450","Placa-mãe","700","500","AM4"]
]

for item in dados:
    campos = driver.find_elements(By.TAG_NAME, "input")

    for i in range(len(item)):
        campos[i].clear()
        campos[i].send_keys(item[i])

    driver.find_element(By.XPATH, "//button[contains(text(),'Cadastrar')]").click()
    time.sleep(1)

# Finalizar missão
driver.find_element(By.XPATH, "//button[contains(text(),'Fiz a missão')]").click()

time.sleep(3)
driver.quit()