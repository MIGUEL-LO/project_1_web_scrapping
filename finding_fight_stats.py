import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_fight_stats(URL, driver):

    # executable_path = '/usr/bin/chromedriver'
    # driver = webdriver.Chrome(executable_path=executable_path)
    # URL = 'http://www.ufcstats.com/fight-details/6cd44e1b2d093ea4'
    driver.get(URL)
    w_or_l_fighter_name = []
    
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

    weight_division = fight_details.find_element_by_class_name("b-fight-details__fight-title").text

    for fighter_detail in fight_details_person:
            # Fight result and corresponding fighter name
        w_or_l = fighter_detail.find_element_by_tag_name("i").text
        name = fighter_detail.find_element_by_tag_name("a").text
        w_or_l_fighter_name.append((w_or_l, name))
    
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


    driver.quit()

    return weight_division, w_or_l_fighter_name, total_strike_headers, first_fighter_tot_strikes, second_fighter_tot_strikes, sig_strike_headers, first_fighter_sig_strikes, second_fighter_sig_strikes, landed_by_target_headers, first_fighter_landed_by_target, second_fighter_landed_by_target, landed_by_position_headers, first_fighter_landed_by_position, second_fighter_landed_by_position

executable_path = '/usr/bin/chromedriver'
driver = webdriver.Chrome(executable_path=executable_path)
URL = 'http://www.ufcstats.com/fight-details/6cd44e1b2d093ea4'

a = get_fight_stats(URL, driver)

for i in a:
    print(i)