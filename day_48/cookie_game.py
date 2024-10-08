# Importa o módulo selenium e as classes necessárias
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configurações do Chrome para manter o navegador aberto após a execução
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Inicializa o driver do Chrome e abre a URL do jogo de cookies
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

# Encontra o elemento do cookie pelo ID
cookie = driver.find_element(By.ID, value='cookie')

# Encontra todos os elementos de itens na loja e obtém seus IDs
items = driver.find_elements(By.CSS_SELECTOR, value='#store div')
items_ids = [item.get_attribute('id') for item in items]

# Define o tempo limite para 5 segundos e 5 minutos
timeout = time.time() + 5
five_min = time.time() + 60*5

# Loop principal do jogo
while True:
    # Clica no cookie
    cookie.click()

    # Verifica se o tempo limite foi atingido
    if time.time() > timeout:
        # Obtém todos os preços dos itens na loja
        all_prices = driver.find_elements(By.CSS_SELECTOR, value='#store b')
        item_prices = []

        # Extrai o custo de cada item
        for price in all_prices:
            element_text = price.text
            if element_text != '':
                cost = int(element_text.split('-')[1].strip().replace(',', ''))
                item_prices.append(cost)

        # Cria um dicionário de upgrades de cookies com seus custos
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = items_ids[n]

        # Obtém a quantidade atual de cookies
        money_element = driver.find_element(By.ID, value='money').text
        if ',' in money_element:
            money_element = money_element.replace(',', '')
        cookie_count = int(money_element)

        # Cria um dicionário de upgrades acessíveis
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Encontra o upgrade mais caro que pode ser comprado
        highest_price_affordable_upgrades = max(affordable_upgrades)
        print(highest_price_affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrades]

        # Compra o upgrade
        driver.find_element(By.ID, value=to_purchase_id).click()

        # Redefine o tempo limite para mais 5 segundos
        timeout = time.time() + 5

    # Verifica se 5 minutos se passaram
    if time.time() > five_min:
        # Obtém e imprime a taxa de cookies por segundo
        cookie_per_s = driver.find_element(By.ID, value='cps').text
        print(cookie_per_s)
        break
