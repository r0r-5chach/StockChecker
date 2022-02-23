from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from mailer import mail_user
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.get("https://www.johnlewis.com/dyson-airwrap-complete-hair-styler/p4233412")
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME, "c-button-yMKB7").click()
driver.implicitly_wait(20)

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

if not soup.find(text="Out of stock") and not soup.find(text="Out of stock online"):
    mail_user("j.perry20011@gmail.com", "The Dyson Airwrap is in stock!", "Buy now!\n https://www.johnlewis.com/dyson"
                                                                          "-airwrap-complete-hair-styler/p4233412")

driver.quit()