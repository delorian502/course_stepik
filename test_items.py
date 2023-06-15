from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_text_on_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(30)
    page_1 = Ec.visibility_of_element_located(browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket"))#+++++  
    
    button_text = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").text
    print(button_text)
    
    
    assert page_1 
    
    
