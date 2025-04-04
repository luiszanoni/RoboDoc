from selenium import webdriver
import psycopg2
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logs.logger import logger

def procuraPreco():
    print("###############################################################")
    print("INICIANDO PROCESSO AUTOMATIZADO DE BUSCA DE PRECOS COM SELENIUM")
    print("###############################################################")

    # connection = psycopg2.connect(database="postgres",
    #                         host="localhost",
    #                         user="postgres",
    #                         password="postgres",
    #                         port="5432")

    # if(connection):
    #     print("Conectado ao banco de dados Postgres")
    # query = connection.cursor()

    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-background-networking")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=chrome_options)


    produto = "Galaxy ZFlip 6"
    site = "https://www.magazineluiza.com.br/"

    driver.get(site)
    print('Acessando o site ' + site)

    search_bar = driver.find_element(By.CSS_SELECTOR, '[data-testid="input-search"]')
    search_bar.send_keys(produto)
    submit_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="search-submit"]')
    submit_button.click()

    driver.implicitly_wait(5)

    primeiro_objeto = driver.find_element(By.XPATH, '//ul[@data-testid="list"]/li[1]')
    valor = primeiro_objeto.find_element(By.XPATH, '//p[@data-testid="price-value"]')

    data = datetime.now()
    # query.execute(f"INSERT INTO precos (produto, preco, data) VALUES (\'{produto}\', \'{valor.text}\', \'{data}\')")
    # connection.commit()

    print(valor.text.replace("ou ", "") + " ", data)
    driver.quit()
    logger.info("Processo de consulta de preco automatico finalizado!")

if __name__ == "__main__":
    procuraPreco()  