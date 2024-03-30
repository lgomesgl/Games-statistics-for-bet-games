from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome")
driver.get("https://fbref.com/en/")
driver.quit()

# player name
player_name = "Vinicius"