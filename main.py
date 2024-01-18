#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By

from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

driver = webdriver.Firefox()
driver.get("https://intra.42.fr")
text_box = driver.find_element(By.ID, "username")
text_box.send_keys(username)
text_box = driver.find_element(By.ID, "password")
text_box.send_keys(password)
button = driver.find_element(By.NAME, "login")
button.click()
input("quit")
driver.quit()
