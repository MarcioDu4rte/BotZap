# Importar as bibliotecas
from selenium import webdriver
import time
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Navegar até o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

# definir contatos e grupos e mensagem a ser enviada
contatos = ['Grupo só meu', 'Édina Comercial']
mensagem = 'Teste envio mensagem automatizada!'

# Buscar contatos ou grupos


def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath(
        '//*[@id="side"]/div[1]/div/label/div/div[2]')
    time.sleep(2)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(1)


def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    time.sleep(2)
    campo_mensagem.click()
    campo_mensagem.send_keys(mensagem)
    campo_mensagem.send_keys(Keys.ENTER)
    time.sleep(1)

# Enviar mensagens para o contato ou grupo


for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)

# xpath busca: //*[@id="side"]/div[1]/div/label/div/div[2]

# xpath enviar mensagem: //*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]
