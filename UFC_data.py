import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\\migue\\Downloads\\chromedriver_win32\\chromedriver.exe')
URL = "http://www.ufcstats.com/statistics/events/completed"
driver.get(URL)

# find all fight events in history available.
fight_events_links = driver.find_elements_by_css_selector(".b-statistics__table-content [href]")
# each fight night event has a link where multiple fights occured.
# Get access to the even containing these fights.
# to then access indvidual fights and pull info out
fight_event_links_ls = [fight_event_link.get_attribute('href') for fight_event_link in fight_events_links]
print(fight_event_links_ls)
print(len(fight_event_links_ls))
# fighters can draw not always green box
# fix
for i in range(1, len(fight_event_links_ls)):
    # driver.get('http://www.ufcstats.com/event-details/0b64d0fed453ef7f')
    driver.get(fight_event_links_ls[i])
    fights_at_an_event = driver.find_elements_by_css_selector(".b-flag b-flag_style_green [href]")
    fights_data_loc_link = [fight_1_vs_1.get_attribute('href') for fight_1_vs_1 in fights_at_an_event]
print(fights_data_loc_link)