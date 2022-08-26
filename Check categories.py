

import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://rozetka.com.ua/"
browser: WebDriver = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

name_rozetka_16_el = ["Комп'ютери та ноутбуки", 'Смартфони, ТВ і Електроніка', 'Товари для геймерів', 'Побутова техніка', 'Товари для дому', 'Інструменти та автотовари', 'Сантехніка та ремонт', 'Дача, сад, город', 'Спорт і захоплення', 'Fashion', "Краса та здоров'я", 'Товари для дітей', 'Зоотовари', 'Офіс, школа, книги', 'Алкогольні напої та продукти', 'Товари для бізнесу та послуги']
proverka_name = []
for index in range (16):
        elements_by_rosetka = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "ul[class*=menu-categories_type_main]>li")))
        elements_by_rosetka[index].click()
        name_rozetka_elements = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h1[class*=ng-star-inserted]"))).text
        proverka_name.append(name_rozetka_elements)
        time.sleep(5)
        browser.back()
assert name_rozetka_16_el == proverka_name, f'The title does not match here what is happened {proverka_name}'
browser.quit()

