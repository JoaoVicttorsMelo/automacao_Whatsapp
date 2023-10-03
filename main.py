import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains

elemento = ''

contato_envio = input("informe o próprio contato do Whatsapp: ")

list_contatos = []

while True:
    contatos = input("digite um nome:")
    list_contatos.append(contatos)

    pergunta = input("Deseja adicionar mais um nome? (s/n): ")
    if pergunta.lower() != 's':
        break

mensagem = input("Digite a mensagem que você deseja enviar: ")


service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com")




time.sleep(60)

nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/button/div[2]/span').click() #clicar na lupa
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(contato_envio) #Selecionar meu numero
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

quantidade_contato = len(list_contatos)
if quantidade_contato % 5 == 0:
    quantidade_bloco = quantidade_contato / 5
else:
    quantidade_bloco = int(quantidade_contato / 5) + 1

# Seleciona a mensagem e abre a caixa para encaminhar
for i in range(quantidade_contato):
    i_inicial = i * 5
    i_final = (i + 1) * 5
    lista_enviar = list_contatos[i_inicial:i_final]

    ActionChains(nav).move_to_element(elemento).perform()
    elemento.find_element('class name', '_3u9t-').click()
    time.sleep(0.5)
    nav.find_element('xpath', '//*[@id="app"]/div/span[4]/div/ul/div/li[4]/div').click()
    nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[4]').click()
    time.sleep(1)
    # escreve o nome dos contatos dentro da lista
    for nome in lista_enviar:
        nav.find_element('xpath',
                         '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(
            nome)
        time.sleep(1)
        nav.find_element('xpath',
                         '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(
            Keys.ENTER)
        time.sleep(1)
        nav.find_element('xpath',
                         '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(
            Keys.BACK_SPACE)
        time.sleep(1)
    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div').click()
    time.sleep(8)

#Gambiarra para o Selenium não fechar automaticamente
while (True):
    pass
