from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(ChromeDriverManager().install())

chrome_browser = webdriver.Chrome()


chrome_browser.maximize_window
chrome_browser.get("https://www.gamestop.com/")
chrome_browser.find_element_by_name("q").click()
chrome_browser.find_element_by_name("q").send_keys("ps5")
WebDriverWait(chrome_browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "product-suggestion")))
form = chrome_browser.find_elements_by_class_name('product-suggestion')
innerform = form[2].click()
chrome_browser.find_element_by_class_name('add-to-cart-buttons').click()
print('')