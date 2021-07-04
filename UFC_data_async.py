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
        fight_night_event_dates.append(fight_night_event_url_row.find("span", {"class": "b-statistics__date"}).get_text(strip=True))
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
    w_or_l = []
    fighter_names = []
    # for fight_detail_person in fight_1vs1_response:
    req = requests.get(fight_1vs1_response)
    sp = BeautifulSoup(req.text, 'lxml')    
    fight_details_persons = sp.find_all("div", {"class": "b-fight-details__person"})
    weight_division = sp.find("i", {"class": "b-fight-details__fight-title"}).get_text(strip=True)
    for fighter_details in fight_details_persons:
        w_or_l.append(fighter_details.find("i").text.split())
        fighter_names.append(fighter_details.find("a").text)
    # print(weight_division)
    # print(fighter_names)
    # print(w_or_l)
    first_fighter_w_or_l = w_or_l[0]
    first_fighter_name = fighter_names[0]
    second_fighter_w_or_l = w_or_l[1]
    second_fighter_name = fighter_names[1]

    total_strikes_headers = []
    total_strikes_sig_strikes_headers = sp.find_all("thead", {"class": "b-fight-details__table-head"})    
    total_strikes_headers_eles = total_strikes_sig_strikes_headers[0]
    total_strikes_headers_ele = total_strikes_headers_eles.find_all("th")
    # print(total_strikes_headers_eles_indiv)
    for total_strikes_header in total_strikes_headers_ele:
        total_strikes_headers.append(total_strikes_header.get_text(strip=True))
    # return total_strikes_headers
    sig_strikes_headers = []
    sig_strikes_headers_eles = total_strikes_sig_strikes_headers[1]
    sig_strikes_headers_ele = sig_strikes_headers_eles.find_all("th")

    for sig_strikes_header in sig_strikes_headers_ele:
        sig_strikes_headers.append(sig_strikes_header.get_text(strip=True))

    first_fighter_tot_strikes = []
    second_fighter_tot_strikes = []
    total_strikes_sig_strikes_stats_ele = sp.find_all("tbody", {"class": "b-fight-details__table-body"})    
    total_strikes_stats_ele = total_strikes_sig_strikes_stats_ele[0]
    total_strikes_stats_ele_vals = total_strikes_stats_ele.find_all("p")
    for i, stat_val in enumerate(total_strikes_stats_ele_vals):
        if i % 2 == 0:
            first_fighter_tot_strikes.append(stat_val.get_text(strip=True))
        else:
            second_fighter_tot_strikes.append(stat_val.get_text(strip=True))

    first_fighter_sig_strikes = []
    second_fighter_sig_strikes = []

    sig_strikes_stats_ele = total_strikes_sig_strikes_stats_ele[2]
    sig_strikes_stats_ele_vals = sig_strikes_stats_ele.find_all("p")

    for i, stat_val in enumerate(sig_strikes_stats_ele_vals):
        if i % 2 == 0:
            first_fighter_sig_strikes.append(stat_val.get_text(strip=True))
        else:
            second_fighter_sig_strikes.append(stat_val.get_text(strip=True))

    landed_by_target_headers = []
    first_fighter_landed_by_target = []
    second_fighter_landed_by_target = []

    strikes_landed_by_target_postion = sp.find_all("div", {"class":"b-fight-details__charts-row"})
    strikes_landed_by_target = strikes_landed_by_target_postion[:3]    
    strikes_landed_by_position = strikes_landed_by_target_postion[3:]

    for target in strikes_landed_by_target:
        strikes_landed_by_target = target.find_all("i")
        first_fighter_landed_by_target.append(strikes_landed_by_target[0].get_text(strip=True))
        landed_by_target_headers.append(strikes_landed_by_target[1].get_text(strip=True))
        second_fighter_landed_by_target.append(strikes_landed_by_target[2].get_text(strip=True))

    landed_by_position_headers = []
    first_fighter_landed_by_position = []
    second_fighter_landed_by_position = []
    for possition in strikes_landed_by_position:
        strikes_landed_by_position = possition.find_all("i")
        first_fighter_landed_by_position.append(strikes_landed_by_position[0].get_text(strip=True))
        landed_by_position_headers.append(strikes_landed_by_position[1].get_text(strip=True))
        second_fighter_landed_by_position.append(strikes_landed_by_position[2].get_text(strip=True))
        # landed_by_position_headers.append(strikes_landed_by_position_names_d_c_g.text)
        # first_fighter_landed_by_position.append(strikes_landed_by_position_fighter_1.text)
        # second_fighter_landed_by_position.append(strikes_landed_by_position_fighter_2.text)

    return weight_division, first_fighter_w_or_l, second_fighter_w_or_l, first_fighter_name, second_fighter_name, total_strikes_headers, first_fighter_tot_strikes, second_fighter_tot_strikes, sig_strikes_headers, first_fighter_sig_strikes, second_fighter_sig_strikes, landed_by_target_headers, first_fighter_landed_by_target, second_fighter_landed_by_target, landed_by_position_headers, first_fighter_landed_by_position, second_fighter_landed_by_position



weight_division, first_fighter_w_or_l, second_fighter_w_or_l, first_fighter_name, second_fighter_name, total_strikes_headers, first_fighter_tot_strikes, second_fighter_tot_strikes, sig_strikes_headers, first_fighter_sig_strikes, second_fighter_sig_strikes, landed_by_target_headers, first_fighter_landed_by_target, second_fighter_landed_by_target, landed_by_position_headers, first_fighter_landed_by_position, second_fighter_landed_by_position = find_stats_from_fight()
print(weight_division, "\n")
print(first_fighter_w_or_l, "\n")
print(second_fighter_w_or_l, "\n")
print(first_fighter_name, "\n")
print(second_fighter_name, "\n")
print(total_strikes_headers, "\n")
print(first_fighter_tot_strikes, "\n")
print(second_fighter_tot_strikes, "\n")
print(sig_strikes_headers, "\n")
print(first_fighter_sig_strikes, "\n")
print(second_fighter_sig_strikes, "\n")
print(landed_by_target_headers, "\n")
print(first_fighter_landed_by_target, "\n")
print(second_fighter_landed_by_target, "\n")
print(landed_by_position_headers, "\n")
print(first_fighter_landed_by_position, "\n")
print(second_fighter_landed_by_position, "\n")
# %%
