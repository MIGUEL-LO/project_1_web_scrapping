#%%
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\\migue\\Downloads\\chromedriver_win32\\chromedriver.exe')
URL = "http://www.ufcstats.com/statistics/events/completed"
driver.get(URL)
# accept_cookies = driver.find_elements_by_xpath('//button[@data-responsibility="acceptAll"]')

# for button in accept_cookies:
#     if button.text == "Accept all cookies":
#         relevant_button = button
# find all fight events.
fight_events_elements = driver.find_elements_by_css_selector(".b-statistics__table-content [href]")
# each fight night event has a link where multiple fights occured.
fight_night_links = [fight_event_link.get_attribute('href') for fight_event_link in fight_events_elements]
print(fight_night_links)
# for fight in fighter_elements:
#     # fighter_names.append(fighter_elements.find_element_by_tag_name("a").text)
#     print(fight.text)
    # print("---")
# print(fighter_names)
# %%
# now need to find all fights in the single fight_night_link
# for fight_night_link in fight_night_links:
#     driver.get(fight_night_link)
#     list_of_links_for_a_fight_in_a_fight_night = driver.find_elements_by_css_selector("b-fight-details__table-text [href]")
#     # each fight night event has a link where multiple fights occured.
#     links_to_individual_fight = [fight.get_attribute('href') for fight in list_of_links_for_a_fight_in_a_fight_night]
# print(links_to_individual_fight)
driver.get('http://www.ufcstats.com/event-details/0b64d0fed453ef7f')
fight = driver.find_elements_by_class_name('b-fight-details__table-text')
fight.text

# %%
