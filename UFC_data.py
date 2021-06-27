from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from IPython.display import display
from sqlalchemy import create_engine


class UFC:
    def __init__(self, URL="http://www.ufcstats.com/statistics/events/completed"):
        self.URL = URL

    def links_to_fight_night_events(self):

        executable_path = '/usr/bin/chromedriver'
        driver = webdriver.Chrome(executable_path=executable_path)
        # URL to all fight events in the past
        driver.get(self.URL)
        pages_buttons_class = driver.find_element_by_class_name("b-statistics__paginate")
        pages_eles = pages_buttons_class.find_elements_by_tag_name("li")
        all_button = pages_eles[-1]
        all_button.click()
        URL = driver.current_url
        driver.get(URL)

        # Contains the links of fight night events that occur at a given night.
        # So each event/night contains multiple fights
        fight_events_links = driver.find_elements_by_css_selector(".b-statistics__table-content [href]")

        # Get the links to these fight night events containing multiple fights.
        fight_event_links_ls = [fight_event_link.get_attribute('href') for fight_event_link in fight_events_links]
        fight_event_links_ls = fight_event_links_ls[1:]

        return fight_event_links_ls, driver 


    def links_to_fights_stats_1_vs_1(self, fight_event_links_ls, driver):
        # fight_event_links_ls, driver = self.links_to_fight_night_events()
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
            return all_fights_links_1_vs_1, driver
        else:
            return 0
    
    
    def get_fight_stats(self, URL, driver):
        
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
    # URL, driver
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

    def creating_UFC_df(self, fight_links_stats, driver):
        # i = 0
        j = 0
        id = 0
        for fight_link in fight_links_stats:
            # if i < 1:

            try:
                weight_division, first_fighter_w_or_l, second_fighter_w_or_l, first_fighter_name, second_fighter_name, total_strike_headers, first_fighter_tot_strikes, second_fighter_tot_strikes, sig_strike_headers, first_fighter_sig_strikes, second_fighter_sig_strikes, landed_by_target_headers, first_fighter_landed_by_target, second_fighter_landed_by_target, landed_by_position_headers, first_fighter_landed_by_position, second_fighter_landed_by_position = self.get_fight_stats(fight_link, driver)
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
            # i += 1

        df = df.drop(columns=['FIGHTER'])
        df.drop(df.filter(regex="Unname"),axis=1, inplace=True)

        return df

    def upload_db(self, df):

        db_name = "postgres"
        db_user = "postgres"
        db_pass = "postgres"
        db_host = "database-2.ce8hdmrsyawr.eu-west-2.rds.amazonaws.com"
        db_port = "5432"

        DB_URI = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
        engine = create_engine(DB_URI)
        engine.connect()
        df.to_sql(name="UFC_data_test", con=engine, schema="public", if_exists="replace", index=False)

        return 0 

if __name__ == "__main__":
    data_UFC = UFC()
    links_to_fight_night_events_, driver = data_UFC.links_to_fight_night_events()


    fight_links_stats, driver = data_UFC.links_to_fights_stats_1_vs_1(links_to_fight_night_events_, driver)
    # print(fight_links_stats, "\n")
    UFC_df = data_UFC.creating_UFC_df(fight_links_stats, driver)
    # display(UFC_df)
    upload_db_ = data_UFC.upload_db(UFC_df)
