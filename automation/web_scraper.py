from selenium import webdriver
import psycopg2
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime

print("#################################")
print("INICIANDO PROCESSO AUTOMATIZADO DE BUSCA DE PRECOS COM SELENIUM")
print("#################################")

connection = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="postgres",
                        port="5432")

if(connection):
    print("Conectado ao banco de dados Postgres")

query = connection.cursor()

chrome_options = Options()


driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.magazineluiza.com.br/")

print(driver.title)

search_bar = driver.find_element(By.CSS_SELECTOR, '[data-testid="input-search"]')
produto = "Galaxy ZFlip 6"
search_bar.send_keys(produto)

submit_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="search-submit"]')

submit_button.click()

driver.implicitly_wait(10)

primeiro_objeto = driver.find_element(By.XPATH, '//ul[@data-testid="list"]/li[1]')
valor = primeiro_objeto.find_element(By.XPATH, '//p[@data-testid="price-value"]')



data = datetime.now()
query.execute(f"INSERT INTO precos (produto, preco, data) VALUES (\'{produto}\', \'{valor.text}\', \'{data}\')")
connection.commit()

print(valor.text)