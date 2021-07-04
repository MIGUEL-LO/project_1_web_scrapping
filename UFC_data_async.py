# %%
from re import I
from bs4 import BeautifulSoup
import grequests
import requests 
import multiprocessing
# %%
def get_urls_to_fight_night_events_and_dates():
    URL = "http://www.ufcstats.com/statistics/events/completed"
    # URL = "http://www.ufcstats.com/statistics/events/completed?page=all"
    # sp = BeautifulSoup()
    request = requests.get(URL)
    sp = BeautifulSoup(request.text, 'lxml')
    fight_night_event_urls_table_fights = sp.find("tbody")
    fight_night_event_urls_rows = fight_night_event_urls_table_fights.find_all("tr", {"class": "b-statistics__table-row"})
    fight_night_event_urls_rows = fight_night_event_urls_rows[1:]

    fight_night_event_urls = []
    fight_night_event_dates = []
    for fight_night_event_url_row in fight_night_event_urls_rows:
        fight_night_event_urls.append(fight_night_event_url_row.find("a").get("href"))
        fight_night_event_dates.append(fight_night_event_url_row.find("span", {"class": "b-statistics__date"}).text.split())
        # print(fight_night_event_url_row_a)

    return fight_night_event_urls, fight_night_event_dates

def getting_urls_dates():

    fight_night_event_urls, fight_night_event_dates = get_urls_to_fight_night_events_and_dates()
    # print(fight_night_event_urls, "\n")
    # print(fight_night_event_dates, "\n")
    # print(len(fight_night_event_urls))
    # print(len(fight_night_event_dates))


def get_request_async_from_fight_night_event_urls(fight_night_event_urls):
    reqs = [grequests.get(url) for url in fight_night_event_urls]
    resp = grequests.map(reqs, size=10)
    return resp

# {==================================
def finding_respones_to_fight_night():
    fight_night_event_responses = get_request_async_from_fight_night_event_urls(fight_night_event_urls)
    print(fight_night_event_responses)
    for fight_event_night in fight_night_event_responses:
        if fight_event_night.status_code != 200:
            print("ERRRORRRRRR")
        # else:
            # print("no")
# }=======================================

def get_urls_to_fights_from_fight_night_events(fight_night_event_responses):
    # this should be here
    # fight_night_event_responses = get_request_async_from_fight_night_event_urls(fight_night_event_urls)

    fight_1vs1_urls = []
    for fight_night_event_response in fight_night_event_responses:
        sp = BeautifulSoup(fight_night_event_response.text, 'lxml')
        fight_table = sp.find("tbody", {"class": "b-fight-details__table-body"})
        fight_1vs1_urls_elements = fight_table.find_all("tr", {"class": "b-fight-details__table-row b-fight-details__table-row__hover js-fight-details-click"})
        for fight_1vs1_urls_element in fight_1vs1_urls_elements:
            fight_1vs1_urls.append(fight_1vs1_urls_element.get("data-link"))
    return fight_1vs1_urls


fight_1vs1_urls = get_urls_to_fights_from_fight_night_events(fight_night_event_responses)
# print(fight_1vs1_urls)
# print(len(fight_1vs1_urls))


def get_request_async_from_fight_urls(fight_1vs1_urls):
    reqs = [grequests.get(url) for url in fight_1vs1_urls]
    resp = grequests.map(reqs, size=10)
    return resp


fight_1vs1_responses = get_request_async_from_fight_urls(fight_1vs1_urls)
print(fight_1vs1_responses)

# for res in fight_1vs1_responses:
    # print(res.status_code)

for fight_1vs1 in fight_1vs1_responses:
    if fight_1vs1.status_code != 200:
        print("ERRRORRRRRR")
    # else:
        # print("is good")
# %%
# need to find the details from the fight in the response
def find_stats_from_fight(fight_1vs1_response="http://www.ufcstats.com/fight-details/78afed76d0e9a639"):
    # this should be here.
    # fight_1vs1_responses = get_request_async_from_fight_urls(fight_1vs1_urls)
    # for fight_1vs1_response in fight_1vs1_responses:
        # sp = BeautifulSoup(fight_1vs1_response.text, 'lxml')
        # fight_details_persons = sp.find_all("div", {"class": "b-fight-details__person"})
    w_or_l = []
    fighter_names = []
    # for fight_detail_person in fight_1vs1_response:
    req = requests.get(fight_1vs1_response)
    sp = BeautifulSoup(req.text, 'lxml')    
    fight_details_persons = sp.find_all("div", {"class": "b-fight-details__person"})

    for fighter_details in fight_details_persons:
        w_or_l.append(fighter_details.find("i").text.split())
        fighter_names.append(fighter_details.find("a").text)
    print(fighter_names)
    print(w_or_l)


print(find_stats_from_fight())


# %%
