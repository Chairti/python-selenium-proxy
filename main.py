from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from randoms import random_province
from rdfname import fname
from rdlname import lname
from sex import randoms_sex
from rdemail import generate_random_email

province = random_province()
random_fname = lname()
random_lname = fname()
sex = randoms_sex()
email = generate_random_email()

def slow_type(element, text, delay=0.1):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

driver = webdriver.Chrome()
driver.get("https://www.example.com")

wait = WebDriverWait(driver, 15)

first_name_input = wait.until(EC.presence_of_element_located((By.ID, "firstName")))
slow_type(first_name_input, random_fname)

last_name_input = wait.until(EC.presence_of_element_located((By.ID, "lastName")))
slow_type(last_name_input, random_lname)

birth_year_input = wait.until(EC.presence_of_element_located((By.ID, "birthYear")))
slow_type(birth_year_input, "1995")

gender_input = wait.until(EC.presence_of_element_located((By.ID, "gender")))
slow_type(gender_input, sex)

province_input = wait.until(EC.presence_of_element_located((By.ID, "province")))
slow_type(province_input, province)

email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
slow_type(email_input, email)

checkbox = wait.until(EC.element_to_be_clickable((By.NAME, "subscribe")))
driver.execute_script("arguments[0].click();", checkbox)

politician = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'แพทองธาร ชินวัตร')]")))
politician.click()

submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'โหวต')]")))
submit_button.click()

time.sleep(50)
driver.quit()