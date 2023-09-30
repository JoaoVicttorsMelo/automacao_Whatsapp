import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com")

mensagem = """só um teste de programa!
valeu
"""

list_contatos =["11955206595", "Kaua", "Jullya irmã", "Tio Leandro", "Mãe Aliny"]

time.sleep(60)

nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/button/div[2]/span').click() #clicar na lupa
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys("11955206595") #Selecionar meu numero
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER) #Selecionar tecla enter
time.sleep(1)

pyperclip.copy(mensagem)
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.CONTROL + "v") #Selecionar tecla enter
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER) #Selecionar tecla enter
time.sleep(2)

lista_elemento = nav.find_elements('class name', '_1uv-a')
for item in lista_elemento:
    mensagem = mensagem.replace("\n", "")
    texto = item.text.replace("\n", "")
    if mensagem in texto:
        elemento = item
        break
ActionChains(nav).move_to_element(elemento).perform()
elemento.find_element('class name', '_3u9t-').click()


#Gambiarra para o Selenium não fechar automaticamente
while (True):
    pass
