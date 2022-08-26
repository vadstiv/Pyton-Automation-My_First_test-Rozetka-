from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://rozetka.com.ua/"
browser: WebDriver = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

search_string = browser.find_element(By.CSS_SELECTOR,"input[class*=search-form__input]")
search_string.send_keys("Меблі")
cnopka = browser.find_element(By.CSS_SELECTOR,"button[class*=button_color_green]").click()

proverka = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"h1[class*=portal__heading]"))).text
proverka1 = "Меблі"
assert proverka == proverka1, f"Tesst not been successfull - {proverka}"
browser.quit()



