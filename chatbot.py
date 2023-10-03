from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import os
import pyautogui

# Caminho para a pasta de destino
pasta_destino = r'C:\Users\arthu\Downloads\DOWNLOADS_'
url_site = 'https://secure.d4sign.com.br/login.html'

# Inicialize o driver do Selenium (certifique-se de ter o WebDriver adequado instalado e configurado)
driver = webdriver.Chrome()

# Abra a página da web
driver.get(url_site)
driver.maximize_window()

# Fazer login
campo_email = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[1]/form/div[2]/input')
campo_senha = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[1]/form/div[3]/div[2]/div[1]/input[1]')
botao_logar = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[1]/form/div[3]/button')

campo_email.send_keys("wendy.dias@proocupacional.com.br")
campo_senha.send_keys("28012016")
botao_logar.click()

# Espere até que uma condição seja satisfeita, por exemplo, que uma página específica seja carregada
wait = WebDriverWait(driver, 30)

# Abra a página de download
cofrepcmso = driver.find_element(By.XPATH, "//small[contains(text(), 'PCMSO - PRO OCUPACIONAL')]").click()
time.sleep(2)

elementos_finalizados = driver.find_elements(By.XPATH, "//span[text()='FINALIZADO']")

# Percorra todos os elementos "FINALIZADO" e realize o download

wait = WebDriverWait(driver, 30)
time.sleep(2)
fecha1 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div/button")))
fecha1.click()
time.sleep(2)
wait = WebDriverWait(driver, 30)
time.sleep(1)
clicarfecha2 = driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/div[1]/button")
clicarfecha2.click()
wait = WebDriverWait(driver, 30)
open1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/div[4]/button")
open1.click()
time.sleep(2)
open2 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/div[4]/ul/li[5]/a")))
open2.click()
wait = WebDriverWait(driver, 30)
elemento_data = driver.find_elements(By.XPATH, '//small[contains(text(), "29 Sep 2023")]')
trespontosdownload = driver.find_elements(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div[4]/table/tbody/tr[1]/td[6]/div/i")
quantidade_elementos = len(elemento_data)

time.sleep(2)

for elemento, trespontos in zip(elemento_data, trespontosdownload):
    try:

        data_elemento = elemento.text

        if "29 Sep 2023" in data_elemento:
           
           for i in range(1, quantidade_elementos + 1): 
            # Clicar nos três pontos
            xpath_trespontos = f"/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div[4]/table/tbody/tr[{i}]/td[6]/div/i"
            trespontos_elemento = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, xpath_trespontos))) #problema ta aqui arthur # aqui, ele nao ta mudando o xpath, ta sempre pegando o primeiro tres pontos
            trespontos_elemento.click()

            print(f"Clicou nos três pontos do elemento {i}") 

            time.sleep(2)
            # Realizar as ações após clicar nos três pontos
            pyautogui.press("TAB")
            time.sleep(1)
            pyautogui.press("TAB")
            time.sleep(1)
            pyautogui.press("TAB")
            time.sleep(1)
            pyautogui.press("TAB")
            time.sleep(1)
            pyautogui.press("TAB")
            time.sleep(1)   
            pyautogui.press("ENTER")
            time.sleep(9)
            pyautogui.press("ESC")
            time.sleep(2)

            print(f"Ações concluídas para o elemento {i}")
            
        else:
                print(f"A Data{data_elemento} não corresponde")

    except Exception as e:
        print(f"Erro: {e}")

 #if driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/div[2]/div/div[4]/table/tbody/tr[20]/td[2]/small").text == "29 Sep 2023":


    try:
        time.sleep(2)
        avancarbotton = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/ul/li[7]/a")
        avancarbotton.click()
        
    except NoSuchElementException:
        print("Aqui estou sendo executado pq nao achei o avancarbotton")        
else:
    print("aqui estou sendo executado porque eu nao sou igual o texto 29 sep 2023")
    wait = WebDriverWait(driver, 30)
    time.sleep(3)
    pyautogui.hotkey('winleft', 'r')
    time.sleep(2)
    pyautogui.write('shell:downloads')
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.hotkey('ctrl', 'e')
    time.sleep(2)
    pyautogui.write('PCMSO')
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'x')
    time.sleep(3)
    pyautogui.hotkey('winleft', 'r')
    time.sleep(3)
    pyautogui.write('C:/Users/arthu/Downloads/DOWNLOADS_')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)   
    pyautogui.hotkey('ctrl', 'v')


# Fechar o navegador
driver.quit()
