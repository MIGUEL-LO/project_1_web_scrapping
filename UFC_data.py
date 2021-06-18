# %%
import time
from selenium import webdriver
import pprint
#%%
driver = webdriver.Chrome(executable_path='C:\\Users\\migue\\Downloads\\chromedriver_win32\\chromedriver.exe')
URL = "http://www.ufcstats.com/statistics/events/completed"
driver.get(URL)
#%%
# find all fight night events in the first page of history available.
fight_events_links = driver.find_elements_by_css_selector(".b-statistics__table-content [href]")
# each fight night event has a link where multiple fights occured.
# Get access to the event containing these fights.
# to then access indvidual fights and pull info out
fight_event_links_ls = [fight_event_link.get_attribute('href') for fight_event_link in fight_events_links]
print("-------------")
fight_event_links_ls = fight_event_links_ls[1:]
print("fight night events links")
print(fight_event_links_ls)
print(len(fight_event_links_ls))


# %%
all_fights_at_an_event_night = []
for fight_night_event_link in fight_event_links_ls:
    driver.get(fight_night_event_link)
    all_fights_at_an_event_night.append(driver.find_elements_by_xpath("//tbody[@class='b-fight-details__table-body']/tr"))

print('-------')
print(all_fights_at_an_event_night)
# fight_1_vs_1_links = []

# for fight_1_vs_1 in all_fights_at_an_event_night:
#     fight_1_vs_1_links.append(fight_1_vs_1.get_attribute("data-link"))

# print("-------")
# print("all fights 1 vs 1 links:\n")
# print(fight_1_vs_1_links)
# # # fighters can draw not always green box
# for i in range 
# driver.get('http://www.ufcstats.com/event-details/0b64d0fed453ef7f')
# #     # driver.get(fight_event_links_ls[i])
# fights_at_an_event = driver.find_elements_by_xpath("//tbody[@class='b-fight-details__table-body']/tr")
# count = 0
# for fight in fights_at_an_event:
#     count += 1
#     print(fight.get_attribute("data-link"))
#     print("count = ", count)
#     print("--------------")
# for fight in fights_at_an_event:
#     print(fight.text)
#     driver.quit()

# fight_1_1 = fights_at_an_event.get_attribute("data-link")
# fight_event_links_ls = [fight_event_link.get_attribute('data-link') for fight_event_link in fights_at_an_event]

    # fights_data_loc_link = [fight_1_vs_1.get_attribute('href') for fight_1_vs_1 in fights_at_an_event]
# print(fight_event_links_ls)
# print(fights_data_loc_link)
# print(len(fights_data_loc_link))
# %%
