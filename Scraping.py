import requests
from bs4 import BeautifulSoup, SoupStrainer
import json
import pandas as pd
from httplib2 import Http
from selenium import webdriver
import time
from random import randint, random
import pandas as pd

driver = webdriver.Edge('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
driver.get('https://www.oddsshark.com/nba/scores')
time.sleep(2)

driver.find_element_by_css_selector('.button.button--stretch.button--hollow-primary').click()
time.sleep(random())

for i in range(0, 8):
    driver.find_element_by_css_selector('.DayPicker-NavButton.DayPicker-NavButton--prev').click()
    time.sleep(random())

driver.find_element_by_xpath("//div[@aria-label='Tue Oct 22 2019']").click()
time.sleep(randint(1, 3))

all_games_list = []
games_links = driver.find_elements_by_xpath('//a[@class="scores-matchup__link"]')
for link in games_links:
    print(link.get_attribute('href'))
    all_games_list.append(link)
time.sleep(randint(1, 3))

for i in range(0, 141):
    driver.find_element_by_css_selector('.button.button--arrow-right.button--hollow-primary.datebuttons__button').click()
    time.sleep(randint(1,3))
    games_links = driver.find_elements_by_xpath('//a[@class="scores-matchup__link"]')
    for link in games_links:
        print(link.get_attribute('href'))
        all_games_list.append(link)
    time.sleep(0.4)



all_games_list = pd.read_fwf('all_games.txt', header=None).values.tolist()

print(all_games_list[1])
data_game = []
data_erro = []
for item in range(0, len(all_games_list)):
    r = requests.get(all_games_list[item][0])
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all('script', attrs={'type': 'application/json'})
    try:
        data = data[0].contents[0]
        dict_data = json.loads(data[:])


        DATE = dict_data['oddsshark_gamecenter']['matchup']['event_date'][:10]
        TEAM_ABBREVIATION = dict_data['oddsshark_gamecenter']['matchup']['home_abbreviation']
        OPP_TEAM_ABBREVIATION = dict_data['oddsshark_gamecenter']['matchup']['away_abbreviation']
        PTS = dict_data['oddsshark_gamecenter']['scoreboard']['data']['home_score']
        OPP_PTS = dict_data['oddsshark_gamecenter']['scoreboard']['data']['away_score']
        WINS_LOSSES = dict_data['oddsshark_gamecenter']['scoreboard']['data']['home_record']
        OPP_WINS_LOSSES = dict_data['oddsshark_gamecenter']['scoreboard']['data']['away_record']

        ODDS_ML_OPENING = dict_data['oddsshark_gamecenter']['odds']['data'][0]['money_line_spread']['home']['money_line']
        ODDS_ML_BOGDOG = dict_data['oddsshark_gamecenter']['odds']['data'][1]['money_line_spread']['home']['money_line']
        ODDS_ML_BUMBET = dict_data['oddsshark_gamecenter']['odds']['data'][2]['money_line_spread']['home']['money_line']
        ODDS_ML_BETONLINE = dict_data['oddsshark_gamecenter']['odds']['data'][3]['money_line_spread']['home']['money_line']
        ODDS_ML_INTERTOPS = dict_data['oddsshark_gamecenter']['odds']['data'][4]['money_line_spread']['home']['money_line']
        OPP_ODDS_ML_OPENING = dict_data['oddsshark_gamecenter']['odds']['data'][0]['money_line_spread']['away']['money_line']
        OPP_ODDS_ML_BOGDOG = dict_data['oddsshark_gamecenter']['odds']['data'][1]['money_line_spread']['away']['money_line']
        OPP_ODDS_ML_BUMBET = dict_data['oddsshark_gamecenter']['odds']['data'][2]['money_line_spread']['away']['money_line']
        OPP_ODDS_ML_BETONLINE = dict_data['oddsshark_gamecenter']['odds']['data'][3]['money_line_spread']['away']['money_line']
        OPP_ODDS_ML_INTERTOPS = dict_data['oddsshark_gamecenter']['odds']['data'][4]['money_line_spread']['away']['money_line']

        MEAN_PTS = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['scoring']['home']['offensive']['total_score']['stat']
        MEAN_PTS_QTR1 = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['scoring']['home']['offensive']['first_quarter_scoring']['stat']
        MEAN_PTS_QTR2 = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['scoring']['home']['offensive']['second_quarter_scoring']['stat']
        MEAN_PTS_QTR3 = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['scoring']['home']['offensive']['third_quarter_scoring']['stat']
        MEAN_PTS_QTR4 = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['scoring']['home']['offensive']['fourth_quarter_scoring']['stat']
        MEAN_FG_PCT = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['shooting']['home']['offensive']['field_goal_percentage']['stat']
        MEAN_FT_PCT = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['shooting']['home']['offensive']['free_throw_percentage']['stat']
        MEAN_FG3_PCT = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['shooting']['home']['offensive']['three_point_percentage']['stat']
        MEAN_AST = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['other']['home']['offensive']['assists']['stat']
        MEAN_REB = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['rebounds']['home']['offensive']['total_rebounds']['stat']
        MEAN_TOV = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['other']['home']['offensive']['turnovers']['stat']

        OPP_TEAM_MEAN_PTS = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['scoring']['away']['offensive']['total_score']['stat']
        OPP_TEAM_MEAN_PTS_QTR1 = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['scoring']['away']['offensive']['first_quarter_scoring']['stat']
        OPP_TEAM_MEAN_PTS_QTR2 = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['scoring']['away']['offensive']['second_quarter_scoring']['stat']
        OPP_TEAM_MEAN_PTS_QTR3 = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['scoring']['away']['offensive']['third_quarter_scoring']['stat']
        OPP_TEAM_MEAN_PTS_QTR4 = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['scoring']['away']['offensive']['fourth_quarter_scoring']['stat']
        OPP_TEAM_MEAN_FG_PCT = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['shooting']['away']['offensive']['field_goal_percentage']['stat']
        OPP_TEAM_MEAN_FT_PCT = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['shooting']['away']['offensive']['free_throw_percentage']['stat']
        OPP_TEAM_MEAN_FG3_PCT = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['shooting']['away']['offensive']['three_point_percentage']['stat']
        OPP_TEAM_MEAN_AST = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['other']['away']['offensive']['assists']['stat']
        OPP_TEAM_MEAN_REB = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['rebounds']['away']['offensive']['total_rebounds']['stat']
        OPP_TEAM_MEAN_TOV = dict_data['oddsshark_gamecenter']['edgeFinder']['data']['other']['away']['offensive']['turnovers']['stat']

        data_game.append((DATE, TEAM_ABBREVIATION, OPP_TEAM_ABBREVIATION, PTS, OPP_PTS, WINS_LOSSES, OPP_WINS_LOSSES,
                          MEAN_PTS, MEAN_PTS_QTR1, MEAN_PTS_QTR2, MEAN_PTS_QTR3, MEAN_PTS_QTR4, MEAN_FG_PCT, MEAN_FT_PCT, MEAN_FG3_PCT,
                          MEAN_AST, MEAN_REB, MEAN_TOV,
                          OPP_TEAM_MEAN_PTS, OPP_TEAM_MEAN_PTS_QTR1, OPP_TEAM_MEAN_PTS_QTR2, OPP_TEAM_MEAN_PTS_QTR3, OPP_TEAM_MEAN_PTS_QTR4,
                          OPP_TEAM_MEAN_FG_PCT, OPP_TEAM_MEAN_FT_PCT, OPP_TEAM_MEAN_FG3_PCT,
                          OPP_TEAM_MEAN_AST, OPP_TEAM_MEAN_REB, OPP_TEAM_MEAN_TOV,
                          ODDS_ML_BETONLINE, ODDS_ML_BOGDOG, ODDS_ML_BUMBET, ODDS_ML_INTERTOPS, ODDS_ML_OPENING,
                          OPP_ODDS_ML_BOGDOG, OPP_ODDS_ML_BUMBET, OPP_ODDS_ML_OPENING, OPP_ODDS_ML_BETONLINE, OPP_ODDS_ML_INTERTOPS))
        print(all_games_list[item][0])

    except:
        print(f'ERRO: {all_games_list[item][0]}')
        data_erro.append(all_games_list[item][0])
    time.sleep(random())

df = pd.DataFrame(data_game, columns=['DATE', 'TEAM_ABBREVIATION', 'OPP_TEAM_ABBREVIATION', 'PTS', 'OPP_PTS', 'WINS_LOSSES', 'OPP_WINS_LOSSES',
                  'MEAN_PTS', 'MEAN_PTS_QTR1', 'MEAN_PTS_QTR2', 'MEAN_PTS_QTR3', 'MEAN_PTS_QTR4', 'MEAN_FG_PCT', 'MEAN_FT_PCT', 'MEAN_FG3_PCT',
                  'MEAN_AST', 'MEAN_REB', 'MEAN_TOV',

                  'OPP_TEAM_MEAN_PTS', 'OPP_TEAM_MEAN_P'
                                       'TS_QTR1', 'OPP_TEAM_MEAN_PTS_QTR2', 'OPP_TEAM_MEAN_PTS_QTR3', 'OPP_TEAM_MEAN_PTS_QTR4',
                  'OPP_TEAM_MEAN_FG_PCT', 'OPP_TEAM_MEAN_FT_PCT', 'OPP_TEAM_MEAN_FG3_PCT',
                  'OPP_TEAM_MEAN_AST', 'OPP_TEAM_MEAN_REB', 'OPP_TEAM_MEAN_TOV',
                  'ODDS_ML_BETONLINE', 'ODDS_ML_BOGDOG', 'ODDS_ML_BUMBET', 'ODDS_ML_INTERTOPS', 'ODDS_ML_OPENING',
                  'OPP_ODDS_ML_BOGDOG', 'OPP_ODDS_ML_BUMBET', 'OPP_ODDS_ML_OPENING', 'OPP_ODDS_ML_BETONLINE', 'OPP_ODDS_ML_INTERTOPS'])

print(df)
df.to_csv('dataset1920.csv')
