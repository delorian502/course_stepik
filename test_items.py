from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    page_1 = Ec.visibility_of_element_located(browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket"))#++++++исправить++++++++++  
    print(page_1) 
