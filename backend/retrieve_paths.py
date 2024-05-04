import pandas as pd
import os
import requests
import time
import random
from selenium.common.exceptions import StaleElementReferenceException
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WEBDRIVER_DELAY_TIME_INT = 10

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
#chrome_options.headless = True
# options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(options=options)

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, WEBDRIVER_DELAY_TIME_INT)

# for page_idx in tqdm(range(1, 11)):
main_url = f'http://giaothong.hochiminhcity.gov.vn/map.aspx'
driver.get(main_url)

# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tab-1175-btnInnerEl"]')))
# traffic_data = driver.find_element(By.XPATH, '//*[@id="tab-1175-btnInnerEl"]')
# traffic_data.click()

wait.until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="checkbox-1206-inputEl"]')))
check_box = driver.find_element(By.XPATH, '//*[@id="checkbox-1206-inputEl"]')
driver.execute_script("arguments[0].click();", check_box)
urls = []
url = ''
place_list = []

if __name__ == '__main__':
  for i in range(1, 500):
    try:
      path_icon = f'//*[@id="map-panel-1015"]/div[2]/div/div[2]/div/div[2]/div[2]/div[{i}]/img'
      element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, path_icon))
            )
      driver.execute_script("arguments[0].click();", element)
      time.sleep(2)

      path_widen = "a[id^='button-'][data-qtip='Mở rộng ']"
      
      element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, path_widen))
          )
      driver.execute_script("arguments[0].click();", element)
      
      #   wait.until(EC.presence_of_element_located(
      #     (By.XPATH, "//*[contains(@id, 'cameraplayer-') and contains(@id, '-body')]")))
        
      #   WebDriverWait(driver, 10).until(
      #       EC.visibility_of_element_located(
      #           (By.XPATH, "//*[contains(@id, 'cameraplayer-') and contains(@id, '-body')]"))
      #   )
        
      original_window = driver.current_window_handle

        # Store all window handles in a list
      all_windows = driver.window_handles

      new_window = [
          window for window in all_windows if window != original_window][0]
      driver.switch_to.window(new_window)
      
      flag = False
      while flag == False:
        flag = WebDriverWait(driver, 10).until(
            lambda d: d.find_element(
                By.XPATH, "//*[contains(@id, 'cameraplayer-') and contains(@id, '-body')]").find_element(
                By.TAG_NAME, 'div').find_element(By.TAG_NAME, 'img').get_attribute('src') not in urls
        )

      if flag:
          img_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(@id, 'cameraplayer-') and contains(@id, '-body')]/div/img"))
          )
          place_element = WebDriverWait(driver, 10).until(
              EC.presence_of_element_located(
                  (By.XPATH, "//*[contains(@id, 'cameraplayer-') and contains(@id, '-body')]/div/span"))
          )
          place_list.append(place_element.text)
          url = driver.execute_script(
              "return arguments[0].getAttribute('src');", img_element)

    #   url = camera_screen_div.find_element(By.TAG_NAME, 'div').find_element(
    #       By.TAG_NAME, 'img').get_attribute('src')
      if len(url) != 0:
        # id = url.split('/')[4][19:].split('&')[0]
        # if id not in urls:
          with open('address_id.txt', 'a+', encoding='utf-8') as f:
                f.write(place_list[-1] + ' separator ' + url + '\n')
      urls.append(url)
      driver.close()
      driver.switch_to.window(original_window)
      time.sleep(2)
    except Exception as e:
      print(f"Error message is {e}")
