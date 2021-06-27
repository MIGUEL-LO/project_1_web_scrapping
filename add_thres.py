#%%
import time
from bs4 import BeautifulSoup
import requests
import concurrent.futures


def links_to_fight_night_events_test(URL="http://www.ufcstats.com/statistics/events/completed"):
   
    # executable_path = '/usr/bin/chromedriver'
    source = requests.get(URL).text
    # URL to all fight events in the past
    # driver.get(URL)
    soup = BeautifulSoup(source, 'lxml')
    fight_table = soup.find('table')
    fight_links = fight_table.find_all("i")
    fight_event_links_ls = [fight_link.a['href'] for fight_link in fight_links]
    fight_event_links_ls = fight_event_links_ls[1:]
    return fight_event_links_ls
fight_event_links = links_to_fight_night_events_test()

#%%
# fight_event_link = fight_event_links[0]
####################

def links_to_fights_stats_1_vs_1_night(fight_event_link):
   
    try:
        all_fights_links_1_vs_1 = []
        # for fight_night_event_link in fight_event_links_ls:
        source = requests.get(fight_event_link).text

        soup = BeautifulSoup(source, 'lxml')
        fight_table = soup.find('table')
        fights_links_in_fight_night = fight_table.find_all("td", {"class": "b-fight-details__table-col b-fight-details__table-col_style_align-top"})
        for fight_link in fights_links_in_fight_night:
            tag_links = fight_link.find('a')
            if tag_links != None:
                all_fights_links_1_vs_1.append(tag_links['href'])
        
        # print(all_fights_links_1_vs_1)
        # return all_fights_links_1_vs_1
        # return all_fights_links_1_vs_1
        print(fights_links_in_fight_night)
    except:
        print("error")
# def links_to_fights_stats_1_vs_1(links_to_fights_stats_1_vs_1_night, fight_event_links):
# i = 0 
all_1_vs_links = []
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(links_to_fights_stats_1_vs_1_night, url) for url in fight_event_links]

    for f in concurrent.futures.as_completed(results): 
        print(f.result())
        # executor.map(links_to_fights_stats_1_vs_1_night, fight_event_links)
        
        # print(num)
    # for links in executor.map(links_to_fights_stats_1_vs_1_night, fight_event_links):
        # print(links)
# print(all_fights_links_1_vs_1)

# links_to_fights_stats_1_vs_1(links_to_fights_stats_1_vs_1_night(fight_event_link), fight_event_links)

# links_to_fights_stats_1_vs_1(fight_event_link)
#######################
#%%
def get_fight_stats(URL, driver):

    # executable_path = '/usr/bin/chromedriver'
    # driver = webdriver.Chrome(executable_path=executable_path)
    # URL = 'http://www.ufcstats.com/fight-details/6cd44e1b2d093ea4'
    driver.get(URL)
    w_or_l = []
    fighter_name = []

    total_strike_headers = []
    first_fighter_tot_strikes = []
    second_fighter_tot_strikes = []

    sig_strike_headers = []
    first_fighter_sig_strikes = []
    second_fighter_sig_strikes = []
   
    landed_by_target_headers = []
    first_fighter_landed_by_target = []
    second_fighter_landed_by_target = []
   
    landed_by_position_headers = []
    first_fighter_landed_by_position = []
    second_fighter_landed_by_position = []


    page_container = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "l-page__container")))

    fight_details = page_container.find_element_by_xpath("//div[@class='b-fight-details']")
    fight_details_person = fight_details.find_elements_by_class_name("b-fight-details__person")

    weight_division = [fight_details.find_element_by_class_name("b-fight-details__fight-title").text]

    for fighter_detail in fight_details_person:
            # Fight result and corresponding fighter name
        w_or_l_ = fighter_detail.find_element_by_tag_name("i").text
        name = fighter_detail.find_element_by_tag_name("a").text
        # w_or_l_fighter_name.append((w_or_l, name))
        w_or_l.append(w_or_l_)
        fighter_name.append(name)
    first_fighter_w_or_l =  [w_or_l[0]]
    first_fighter_name = [fighter_name[0]]
    second_fighter_w_or_l =  [w_or_l[1]]
    second_fighter_name = [fighter_name[1]]
    # print(w_or_l_fighter_name, "erm")



    # headers for tots and sig strikes
    # stats belonging to headers
    total_strikes_sig_strikes_headers = page_container.find_elements_by_xpath("//thead[@class='b-fight-details__table-head']")    
    # print(total_strikes_sig_strikes_headers)
    total_strikes_headers_eles = total_strikes_sig_strikes_headers[0]
    total_strikes_headers_eles_indiv = total_strikes_headers_eles.find_elements_by_tag_name("th")
#
    for tot_header in total_strikes_headers_eles_indiv:
        total_strike_headers.append(tot_header.text)
#
    sig_strikes_headers_eles = total_strikes_sig_strikes_headers[1]
    sig_strikes_headers_eles_indiv = sig_strikes_headers_eles.find_elements_by_tag_name("th")
#
    for sig_header in sig_strikes_headers_eles_indiv:
        sig_strike_headers.append(sig_header.text)
#
#
    total_strikes_sig_strikes_stats_ele = page_container.find_elements_by_xpath("//tbody[@class='b-fight-details__table-body']")    
    total_strikes_stats_ele =  total_strikes_sig_strikes_stats_ele[0]
    total_strikes_stats_ele_vals = total_strikes_stats_ele.find_elements_by_tag_name("p")


    for i, stat_val in enumerate(total_strikes_stats_ele_vals):
        if i % 2 == 0:
            first_fighter_tot_strikes.append(stat_val.text)
        else:
            second_fighter_tot_strikes.append(stat_val.text)

    # print(first_fighter_tot_strikes, "\n")
    # print(second_fighter_tot_strikes, "\n")


    sig_strikes_stats_ele = total_strikes_sig_strikes_stats_ele[2]
    sig_strikes_stats_ele_vals = sig_strikes_stats_ele.find_elements_by_tag_name("p")

    for i, stat_val in enumerate(sig_strikes_stats_ele_vals):
        if i % 2 == 0:
            first_fighter_sig_strikes.append(stat_val.text)
        else:
            second_fighter_sig_strikes.append(stat_val.text)
    # print(first_fighter_sig_strikes, "\n")
    # print(second_fighter_sig_strikes, "\n")

    strikes_landed_by_target_postion = page_container.find_elements_by_xpath("//div[@class='b-fight-details__charts-row']")
    strikes_landed_by_target = strikes_landed_by_target_postion[:3]    
    strikes_landed_by_position = strikes_landed_by_target_postion[3:]


    for target in strikes_landed_by_target:
        strikes_landed_by_target = target.find_elements_by_tag_name("i")
        strikes_landed_by_target_fighter_1 = strikes_landed_by_target[0]
        strikes_landed_by_target_names_h_b_l = strikes_landed_by_target[1]
        strikes_landed_by_target_fighter_2 = strikes_landed_by_target[2]
        landed_by_target_headers.append(strikes_landed_by_target_names_h_b_l.text)
        first_fighter_landed_by_target.append(strikes_landed_by_target_fighter_1.text)
        second_fighter_landed_by_target.append(strikes_landed_by_target_fighter_2.text)
 
    # print("targ = ", landed_by_target_headers, "\n")
    # print(first_fighter_landed_by_target, "\n")
    # print(second_fighter_landed_by_target, "\n")


    for possition in strikes_landed_by_position:
        strikes_landed_by_position = possition.find_elements_by_tag_name("i")
        strikes_landed_by_position_fighter_1 = strikes_landed_by_position[0]
        strikes_landed_by_position_names_d_c_g = strikes_landed_by_position[1]
        strikes_landed_by_position_fighter_2 = strikes_landed_by_position[2]
        landed_by_position_headers.append(strikes_landed_by_position_names_d_c_g.text)
        first_fighter_landed_by_position.append(strikes_landed_by_position_fighter_1.text)
        second_fighter_landed_by_position.append(strikes_landed_by_position_fighter_2.text)

    # print("targ = ", landed_by_position_headers, "\n")
    # print(first_fighter_landed_by_position, "\n")
    # print(second_fighter_landed_by_position, "\n")


    # driver.quit()

    return weight_division, first_fighter_w_or_l, second_fighter_w_or_l, first_fighter_name, second_fighter_name, total_strike_headers, first_fighter_tot_strikes, second_fighter_tot_strikes, sig_strike_headers, first_fighter_sig_strikes, second_fighter_sig_strikes, landed_by_target_headers, first_fighter_landed_by_target, second_fighter_landed_by_target, landed_by_position_headers, first_fighter_landed_by_position, second_fighter_landed_by_position

# executable_path = '/usr/bin/chromedriver'
# driver = webdriver.Chrome(executable_path=executable_path)
# URL = 'http://www.ufcstats.com/fight-details/6cd44e1b2d093ea4'
# #

# a = get_fight_stats(URL, driver)

# for i in a:
#     print(i)



    # = print(links_to_fight_night_events())
# print(current_url)
# fight_event_links_ls, driver = print(links_to_fight_night_events())
# print(driver)
#%%
        # i += 1
# links_to_fight_night_events_2, driver = links_to_fight_night_events_test()
# links_to_fight_night_events_test_e = links_to_fight_night_events_2
# print(links_to_fight_night_events_test_e, "\n")

# fight_links_stats, driver = links_to_fights_stats_1_vs_1(links_to_fight_night_events_test_e, driver)
# print(fight_links_stats, "\n")

links_to_fight_night_events_, driver = links_to_fight_night_events()
fight_links_stats, driver = links_to_fights_stats_1_vs_1(links_to_fight_night_events_, driver)
print(fight_links_stats, "\n")


# fight_links_stats, driver_ = links_to_fights_stats_1_vs_1(links_to_fight_night_events_, driver)
# print(fight_links_stats)
#%%
fight_links_stats_test = fight_links_stats[2]

#%%
import pandas as pd
from IPython.display import display

# %%



i = 0
j = 0
id = 0
for fight_link in fight_links_stats:


    try:
        weight_division, first_fighter_w_or_l, second_fighter_w_or_l, first_fighter_name, second_fighter_name, total_strike_headers, first_fighter_tot_strikes, second_fighter_tot_strikes, sig_strike_headers, first_fighter_sig_strikes, second_fighter_sig_strikes, landed_by_target_headers, first_fighter_landed_by_target, second_fighter_landed_by_target, landed_by_position_headers, first_fighter_landed_by_position, second_fighter_landed_by_position = get_fight_stats(fight_link, driver)
        if j == 0:

            first_row = [id] + weight_division + first_fighter_w_or_l + first_fighter_name + first_fighter_tot_strikes + first_fighter_sig_strikes + first_fighter_landed_by_target + first_fighter_landed_by_position
            second_row = [id] + weight_division + second_fighter_w_or_l + second_fighter_name + second_fighter_tot_strikes + second_fighter_sig_strikes + second_fighter_landed_by_target + second_fighter_landed_by_position

            columns_headers = ['id' ,'Weight devision', 'Result', 'Fighters name'] + total_strike_headers + sig_strike_headers + landed_by_target_headers + landed_by_position_headers
            df = pd.DataFrame(columns=columns_headers)
            df.loc[0] = first_row
            df.loc[1] = second_row
            # display(df)
            j += 1
        else:
            first_row = [id] + weight_division + first_fighter_w_or_l + first_fighter_name + first_fighter_tot_strikes + first_fighter_sig_strikes + first_fighter_landed_by_target + first_fighter_landed_by_position
            second_row = [id] + weight_division + second_fighter_w_or_l + second_fighter_name + second_fighter_tot_strikes + second_fighter_sig_strikes + second_fighter_landed_by_target + second_fighter_landed_by_position

            first_series = pd.Series(first_row, index=df.columns)
            second_series = pd.Series(second_row, index=df.columns)

            df = df.append(first_series, ignore_index=True)
            df = df.append(second_series, ignore_index=True)
            # display(df)
        # i += 1
        id += 1
    except:
        print("error at id = ", id)

        # print(weight_division, "\n")
        # print(w_or_l_fighter_name, "\n")
        # print(total_strike_headers, "\n")
        # print(first_fighter_tot_strikes, "\n")
        # print(second_fighter_tot_strikes, "\n")
        # print(sig_strike_headers, "\n")
        # print(first_fighter_sig_strikes, "\n")
        # print(second_fighter_sig_strikes, "\n")
        # print(landed_by_target_headers, "\n")
        # print(first_fighter_landed_by_target, "\n")
        # print(second_fighter_landed_by_target, "\n")
        # print(landed_by_position_headers, "\n")
        # print(first_fighter_landed_by_position, "\n")
        # print(second_fighter_landed_by_position, "\n")
        # print("------------------")

# %%
# print(len(fight_links_stats))
# %%
df