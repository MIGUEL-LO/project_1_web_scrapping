# %%
from typing import final
from selenium import webdriver
import concurrent.futures

def links_to_fight_night_events(URL="http://www.ufcstats.com/statistics/events/completed"):
    
    executable_path = '/usr/bin/chromedriver'
    
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

fight_event_link, driver = links_to_fight_night_events()
print(fight_event_link[-1])
# %%
def fight_link_in_fight_night(fight_event_link, driver):
    # fight_event_link, driver = fight_event_link_driver
    # fight_event_link_last = fight_event_link[-1]
    print(fight_event_link)
    
    driver.get(fight_event_link)
    fight_links_in_fight_night_ = driver.find_elements_by_xpath("//tbody[@class='b-fight-details__table-body']/tr")
    all_fights_links_1_vs_1 = []
    for fight_1_vs_1_link in fight_links_in_fight_night_:
    # contains all fight 1 vs 1 links from which will get stats.
       all_fights_links_1_vs_1.append(fight_1_vs_1_link.get_attribute("data-link"))
 

    return all_fights_links_1_vs_1 

    
# fights = fight_link_in_fight_night(fight_event_link, driver)
# print(fights)

fight_event_link, driver = links_to_fight_night_events()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(fight_link_in_fight_night, (fight_event_link, driver))
print(all_fights_links_1_vs_1)
# fights_links_in_fight_night = []
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     fights_links_in_fight_night.append(executor.map(fight_link_in_fight_night, links_to_fight_night_events))

#%%

def links_to_fights_stats_1_vs_1(fight_event_links_ls, driver):
    
    try :

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
    finally:
        driver.quit()

links_to_fight_night_events_, driver = links_to_fight_night_events()

links_to_fights_stats_1_vs_1(links_to_fight_night_events_, driver)