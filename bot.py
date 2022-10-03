from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.flashscore.com.br/')

time.sleep(3)

elemento = driver.find_elements(By.CLASS_NAME, 'event__match')

window_before = driver.window_handles[0]

driver.find_element(By.XPATH, '//*[@id="onetrust-reject-all-handler"]').click()

time.sleep(2)


while True:

    try:

        driver.find_elements(By.CLASS_NAME, 'filters__tab')[1].click()

        time.sleep(3)

        for x in range(len(elemento)):

            driver.find_elements(By.CLASS_NAME, 'event__match')[x].click()

            time.sleep(5)

            window_after = driver.window_handles[1]

            driver.switch_to.window(window_after)

            try:
                estatistica = driver.find_element(By.LINK_TEXT, 'ESTATÍSTICAS')
                if estatistica.is_displayed():
                    estatistica.click()
                    time.sleep(3)
                    time1 = driver.find_element(
                        By.XPATH, '//*[@id="detail"]/div[5]/div[2]/div[3]/div[2]/a').text
                    time2 = driver.find_element(
                        By.XPATH, '//*[@id="detail"]/div[5]/div[4]/div[3]/div[1]/a').text
                    placar_time1 = driver.find_element(
                        By.XPATH, '//*[@id="detail"]/div[5]/div[3]/div/div[1]/span[1]').text
                    placar_time2 = driver.find_element(
                        By.XPATH, '//*[@id="detail"]/div[5]/div[3]/div/div[1]/span[3]').text
                    tempo = driver.find_element(
                        By.XPATH, '//*[@id="detail"]/div[5]/div[3]/div/div[2]/span[1]').text
                    posse_DeBola1 = driver.find_element(
                        By.XPATH, '//*[@id="detail"]/div[9]/div[1]/div[1]/div[1]').text
                    posse_DeBola2 = driver.find_element(
                        By.XPATH, '//*[@id="detail"]/div[9]/div[1]/div[1]/div[3]').text
                    tentativa_DeGol1 = driver.find_element(
                        By.XPATH, '//*[@id="detail"]/div[9]/div[2]/div[1]/div[1]').text
                    tentativa_DeGol2 = driver.find_element(
                        By.XPATH, '//*[@id="detail"]/div[9]/div[2]/div[1]/div[3]').text
                    chutes_fora1 = driver.find_element(
                        By.XPATH, '//*[@id="detail"]/div[9]/div[4]/div[1]/div[1]').text
                    chutes_fora2 = driver.find_element(
                        By.XPATH, '//*[@id="detail"]/div[9]/div[4]/div[1]/div[3]').text
                    ataques1 = driver.find_element(
                        By.XPATH, '//*[@id="detail"]/div[9]/div[12]/div[1]/div[1]').text
                    ataques2 = driver.find_element(
                        By.XPATH, '//*[@id="detail"]/div[9]/div[12]/div[1]/div[3]').text
                    ataques_perigosos1 = driver.find_element(
                        By.XPATH, '//*[@id="detail"]/div[9]/div[13]/div[1]/div[1]').text
                    ataques_perigosos2 = driver.find_element(
                        By.XPATH, '//*[@id="detail"]/div[9]/div[13]/div[1]/div[3]').text
                    msg = f'''{time1} x {time2}
⏰ {tempo}

Eventos Casa/Visitante
Ataques: {ataques1} / {ataques2}
Ataques Perigosos: {ataques_perigosos1} / {ataques_perigosos2}
Posse de Bola: {posse_DeBola1} x {posse_DeBola2}


Chutes Casa/Visitante
Tentativas de Gol: {tentativa_DeGol1} / {tentativa_DeGol2}
Chutes Fora: {chutes_fora1} / {chutes_fora2}
No Gol: {placar_time1} - {placar_time2}
Link do jogo na Flashscore: 
{driver.current_url}'''
                    
                    print(msg)                

                    time.sleep(10)
                    driver.close()
                    driver.switch_to.window(window_before)

            except NoSuchElementException:
                driver.close()
                driver.switch_to.window(window_before)
                print("OK")

    except:
        print('ERROR')
        driver.switch_to.window(window_before)
        driver.refresh()
        time.sleep(3)
        driver.execute_script("window.scrollTo(1000, 0)")

        time.sleep(5)

    time.sleep(10)
