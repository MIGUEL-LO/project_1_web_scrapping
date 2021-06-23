#%%
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

executable_path = 'C:\\Users\\migue\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=executable_path)
URL = 'http://www.ufcstats.com/fight-details/6cd44e1b2d093ea4'
driver.get(URL)
w_or_l_fighter_name = []
total_strike_headers = []
fighter_name_total_strike = []
fighter_striking_stats = []
significant_strikes_col_names = []
significant_strikes_vals = []
#%%
try:
    page_container = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "l-page__container")))
    fight_details = page_container.find_element_by_xpath("//div[@class='b-fight-details']")
    fight_details_person = fight_details.find_elements_by_class_name("b-fight-details__person")
    weight_division = fight_details.find_element_by_class_name("b-fight-details__fight-head")
    weight_division = weight_division.find_element_by_tag_name("i")
    totals = page_container.find_element_by_xpath("//section[@class='b-fight-details__section js-fight-section']")
    tots_headers = totals.find_element_by_xpath("//table//thead/tr")
    striking_columns = tots_headers.find_elements_by_xpath("th")
    fight_scores = totals.find_element_by_xpath("//table//tbody/tr")
    fighter_names = fight_scores.find_elements_by_tag_name("a")
    fight_stats_tots = fight_scores.find_elements_by_xpath("td")
    significant_strikes_header = page_container.find_elements_by_xpath("//tbody[@class='b-fight-details__table-body']")[1]
    sig_fight_scores = totals.find_element_by_xpath("//table//tbody/tr")
    sig_fighter_names = sig_fight_scores.find_elements_by_tag_name("a")
    sig_fight_stats_tots = sig_fight_scores.find_elements_by_xpath("td")










    # sig_fighter_names = significant_strikes_header.find_elements_by_tag_name("a")
    # print(sig_fight_scores.text)

    # print(len(significant_strikes_header))
    # # for sig_fight_stat in significant_strikes_header:
    # #     # print(fight_stat)
    # sig_fight_stat = significant_strikes_header.find_elements_by_tag_name("p")
    # print("=========")
    # print(sig_fight_stat)
    # print("==========")
    # for s in sig_fight_stat:
    #     print(s.text)
        # significant_strikes_vals.append(s.text)


    # significant_strike_col_names = significant_strikes_header.find_elements_by_tag_name("th")
    # fight_scores_sig = significant_strikes_header.find_elements_by_xpath("//table//tbody/tr")[1]
    # print(fight_scores_sig.text)

    # fighter_names_sig = fight_scores_sig.find_elements_by_tag_name("a")
    # fight_stats_tots_sig = fighter_names_sig.find_elements_by_xpath("td")
    # print(fight_stats_tots_sig)

    # print(significant_strikes_header.text)
    # significant_strikes_header_names.append(significant_strikes_header.text)
    # print(len(significant_strikes_header))
    # for table in significant_strikes_header:
    #     print(table.text)
############################
    for fighter_detail in fight_details_person:
        # Fight result and corresponding fighter name
        w_or_l = fighter_detail.find_element_by_tag_name("i").text
        name = fighter_detail.find_element_by_tag_name("a").text
        w_or_l_fighter_name.append((w_or_l, name))

    for col in striking_columns:
        total_strike_headers.append(col.text)

    for name in fighter_names:
        fighter_name_total_strike.append(name.text)

    for fight_stat in fight_stats_tots:
        # print(fight_stat)
        stat = fight_stat.find_elements_by_tag_name("p")
        for s in stat:
            # print(s.text)
            fighter_striking_stats.append(s.text)

    for col_name in sig_fighter_names:
        significant_strikes_col_names.append(col_name.text)

    for fight_stat in sig_fight_stats_tots:
        stat = fight_stat.find_elements_by_tag_name("p")
        for s in stat:
            # print(s.text)
            significant_strikes_vals.append(s.text)



############################

        # print(name.text)
        # print("------")

finally:
    driver.quit()

print(w_or_l_fighter_name)
print(total_strike_headers)
print(fighter_name_total_strike)
print(fighter_striking_stats)
print(significant_strikes_col_names)
print(significant_strikes_vals)