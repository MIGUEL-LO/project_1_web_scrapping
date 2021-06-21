import time
from selenium import webdriver
import pprint

executable_path = 'C:\\Users\\migue\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=executable_path)
URL = 'http://www.ufcstats.com/fight-details/6cd44e1b2d093ea4'
driver.get(URL)
page_container = driver.find_element_by_class_name("l-page__container")
fight_details = page_container.find_element_by_class_name("b-fight-details")
# %%
print(win_lose_fighter_name_elements)
print("\n")
for eles in win_lose_fighter_name_elements:
    fighter_w_or_l = eles.find_element_by_xpath()
    print(eles)
print("\n")


#%%
for win in win_lose_fighter_name_elements:
    w = win.text.split()
    print("win or na = ", w)
