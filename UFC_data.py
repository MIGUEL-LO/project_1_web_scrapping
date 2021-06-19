# %%
import time
from selenium import webdriver
import pprint
def links_to_fight_night_events(URL="http://www.ufcstats.com/statistics/events/completed"):

    executable_path = 'C:\\Users\\migue\\Downloads\\chromedriver_win32\\chromedriver.exe'

    driver = webdriver.Chrome(executable_path=executable_path)
    # URL to all fight events in the past
    # URL = "http://www.ufcstats.com/statistics/events/completed"
    driver.get(URL)
    # Contains the links of fight night events that occur at a given night.
    # So each event/night contains multiple fights
    fight_events_links = driver.find_elements_by_css_selector(".b-statistics__table-content [href]")
    # print(fight_events_links)
    # Get the links to these fight night events containing multiple fights.
    fight_event_links_ls = [fight_event_link.get_attribute('href') for fight_event_link in fight_events_links]
    # print("-------------")
    # The first row is for upcoming fights, ignore it.
    fight_event_links_ls = fight_event_links_ls[1:]
    # print("fight night events links")
    # print(fight_event_links_ls)
    # print(len(fight_event_links_ls))
    return fight_event_links_ls, driver
# %%
# contains all links for the fights. the links contain the stats of that fight.
def links_to_fights_stats_1_vs_1(fight_event_links_ls, driver):

    all_fights_links_1_vs_1 = []
    counts = []
    for fight_night_event_link in fight_event_links_ls:
        count = 0
        # link_fight_night = fight_event_links_ls[fight_night_event_idx]
        # finding the elements with the class to find the link for particular fight.
        driver.get(fight_night_event_link)
        fights_links_in_fight_night = driver.find_elements_by_xpath("//tbody[@class='b-fight-details__table-body']/tr")
        for fight_1_vs_1_link in fights_links_in_fight_night:
            count += 1
            # contains all fight 1 vs 1 links from which will get stats.
            all_fights_links_1_vs_1.append(fight_1_vs_1_link.get_attribute("data-link"))
        counts.append(count)
    
    if sum(counts) == len(all_fights_links_1_vs_1):
        return all_fights_links_1_vs_1
    else:
        return 0


def links_to_fights_stats_1_vs_1_test_range(fight_event_links_ls, driver):

    all_fights_links_1_vs_1 = []
    counts = []
    for fight_night_event_idx in range(0, 1):
        count = 0
        link_fight_night = fight_event_links_ls[fight_night_event_idx]
        # finding the elements with the class to find the link for particular fight.
        driver.get(link_fight_night)
        fights_links_in_fight_night = driver.find_elements_by_xpath("//tbody[@class='b-fight-details__table-body']/tr")
        for fight_1_vs_1_link in fights_links_in_fight_night:
            count += 1
            # contains all fight 1 vs 1 links from which will get stats.
            all_fights_links_1_vs_1.append(fight_1_vs_1_link.get_attribute("data-link"))
        counts.append(count)

    if sum(counts) == len(all_fights_links_1_vs_1):
        return all_fights_links_1_vs_1
    else:
        return 0
# %%
# links_to_fight_night_events, driver = links_to_fight_night_events()
# fight_links = links_to_fights_stats_1_vs_1_test_range(links_to_fight_night_events, driver)
# print(fight_links)
# print(len(fight_links))

# %%

# Need to classify data by weightclass, then who won,
# what did they to win
# if the box is greeen in the class name, find the name of the fighter.
# Using the name of the fighter pull out all of the totals and significant strikes data.
import time
from selenium import webdriver
import pprint
executable_path = 'C:\\Users\\migue\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=executable_path)
URL = 'http://www.ufcstats.com/fight-details/6cd44e1b2d093ea4'
driver.get(URL)
win_fighter = driver.find_element_by_xpath("//div[@class='b-fight-details__person']")
fighter_w = win_fighter.find_element_by_xpath(".//i").text
fighter_w_name = win_fighter.find_element_by_xpath(".")
# %%
