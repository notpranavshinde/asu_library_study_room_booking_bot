from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException


firefox_options = Options()
firefox_options.add_argumen("--disable-notifications")
driver = webdriver.Firefox(options=firefox_options)
driver.get("https://asu.libcal.com/reserve/hayden-study")
roomC40 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(((By.CSS_SELECTOR, '[data-resource-id="eid_117804"]'))))
roomC40.click()
slots = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, f"//td[@data-resource-id='eid_117804']//div[@class='fc-timeline-event-harness']")))
unavailablity = True
for i in range(len(slots)):
    slot = WebDriverWait(driver, 10).until(EC.presence_of_element_located(((By.XPATH, f"//td[@data-resource-id='eid_117804']//div[@class='fc-timeline-event-harness'][{i+1}]//a"))))
    slot_status = slot.get_attribute('aria-label')
    unavailablity = "Unavailable/Padding" in slot_status
    if unavailablity is False:
        print(slot_status)
        slot.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@id = "submit_times"]'))).click()
        break

if unavailablity is True: print("No slots available")
else:
    # username = input("input asurite id: ")
    # password = input("input password: ")
    username = config.username
    password = config.password

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id = "username"]'))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id = "password"]'))).send_keys(password)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@name = "submit"]'))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@type = "submit"]'))).click()
    # id_number = input("Enter ASU ID NUMBER: ")
    id_number = config.id_number
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@class="form-control notempty"]'))).send_keys(id_number)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@type = "submit"]'))).click()
