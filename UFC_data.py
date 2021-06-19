# %%
import time
from selenium import webdriver
import pprint
driver = webdriver.Chrome(executable_path='C:\\Users\\migue\\Downloads\\chromedriver_win32\\chromedriver.exe')
# URL to all fight events in the past
URL = "http://www.ufcstats.com/statistics/events/completed"
driver.get(URL)
# Contains the links of fight night events that occur at a given night.
# So each event/night contains multiple fights
fight_events_links = driver.find_elements_by_css_selector(".b-statistics__table-content [href]")
print(fight_events_links)
# Get the links to these fight night events containing multiple fights.
fight_event_links_ls = [fight_event_link.get_attribute('href') for fight_event_link in fight_events_links]
print("-------------")
# The first row is for upcoming fights, ignore it.
fight_event_links_ls = fight_event_links_ls[1:]
print("fight night events links")
print(fight_event_links_ls)
print(len(fight_event_links_ls))

# %%
# contains all links for the fights. the links contain the stats of that fight.

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


# all_fights_links_1_vs_1 = []
# counts = []
# for fight_night_event_idx in range(0, len(fight_event_links_ls)):
#     count = 0
#     link_fight_night = fight_event_links_ls[fight_night_event_idx]
#     # finding the elements with the class to find the link for particular fight.
#     driver.get(link_fight_night)
#     fights_links_in_fight_night = driver.find_elements_by_xpath("//tbody[@class='b-fight-details__table-body']/tr")
#     for fight_1_vs_1_link in fights_links_in_fight_night:
#         count += 1
#         # contains all fight 1 vs 1 links from which will get stats.
#         all_fights_links_1_vs_1.append(fight_1_vs_1_link.get_attribute("data-link"))
#     counts.append(count)
# %%
# if sum of counts which indicate how many links there are belonging to a fight
# is equal to the amount of links in all_fights_at_an_event_night
# then we good 
print("sum_counts = ", sum(counts))
print(len(all_fights_links_1_vs_1))






#######################
#######################

# for fight_night_event_idx in range(0,2):
#     count = 0
#     link_fight_night = fight_event_links_ls[fight_night_event_idx]
#     # print(link_fight_night)
#     # print(type(fight_event_links_ls[fight_night_event_idx]))
#     driver.get(link_fight_night)
#     fights_in_night = driver.find_elements_by_xpath("//tbody[@class='b-fight-details__table-body']/tr")
#     for fight in fights_in_night:
#         # count += 1
#         all_fights_at_an_event_night.append(fight.get_attribute("data-link"))
#     # print("count = ", count)
# print(all_fights_at_an_event_night)

# %%
