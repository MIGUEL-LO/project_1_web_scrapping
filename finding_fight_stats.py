#%%
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

executable_path = 'C:\\Users\\migue\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=executable_path)
URL = 'http://www.ufcstats.com/fight-details/6cd44e1b2d093ea4'
driver.get(URL)
w_or_l_fighter_name = []
total_strike_headers = []
#%%
try:
    page_container = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "l-page__container")))
    fight_details = page_container.find_element_by_xpath("//div[@class='b-fight-details']")
    fight_details_person = fight_details.find_elements_by_class_name("b-fight-details__person")
    weight_division = fight_details.find_element_by_class_name("b-fight-details__fight-head")
    weight_division = weight_division.find_element_by_tag_name("i")
    totals = page_container.find_element_by_xpath("//section[@class='b-fight-details__section js-fight-section']")
    tots_headers = totals.find_element_by_xpath("//table//thead/tr")
    columns = tots_headers.find_elements_by_xpath("th")
    # print(tots_headers.text)
    for fighter_detail in fight_details_person:
        # Fight result and corresponding fighter name
        w_or_l = fighter_detail.find_element_by_tag_name("i").text
        name = fighter_detail.find_element_by_tag_name("a").text
        w_or_l_fighter_name.append((w_or_l, name))

    for name in columns:
        total_strike_headers.append(name.text)
        # print(name.text)
        

finally:
    driver.quit()

print(w_or_l_fighter_name)
print(total_strike_headers)