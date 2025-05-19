from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from randoms import random_province
from rdfname import fname
from rdlname import lname

province = random_province()
random_fname = lname()
random_lname = fname()
# เปิดเบราว์เซอร์ Chrome
driver = webdriver.Chrome()

# ไปที่หน้า google.com
driver.get("https://www.google.com")

# รอโหลดหน้าเว็บ
time.sleep(2)

# หา input ช่องค้นหา (ค้นหาด้วย name="q")
search_box = driver.find_element(By.NAME, "q")

# พิมพ์คำที่ต้องการค้นหา
search_box.send_keys("จังหวัดที่สุ่มได้คือ:", province, random_fname, random_lname )

# กด Enter เพื่อค้นหา
search_box.send_keys(Keys.RETURN)

# รอผลลัพธ์แสดงขึ้น
time.sleep(30)

# ปิดเบราว์เซอร์
driver.quit()
