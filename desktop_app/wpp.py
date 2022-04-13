from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




options = webdriver.ChromeOptions();
options.add_argument(r"user-data-dir=C:\Users\carid\AppData\Local\Google\Chrome\User Data\Default")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
navegador = webdriver.Chrome(options=options)


link = "https://web.whatsapp.com/send?phone=+5584994738659&text= :)"

navegador.get(link)
try:
    side = WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.ID,"side")))
    
except:
    print("Ocorreu um Erro a o carregar chat do cliente: X")

print("Carregando Botao de envio")
try:
    sender_button = WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')))
    print("Botao de enviar, carregou")
    navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()


except BaseException:
    print("Ocorreu um Erro a o enviar mensagem no Whatsapp do cliente: X")
