from .models import Scores
import urllib.request
from bs4 import BeautifulSoup
import re
from datetime import date

# scraping start
today = date.today().isoformat().replace('-', '')
html = urllib.request.urlopen('http://baseball.yahoo.co.jp/npb/schedule/?&date=' + today)
soup = BeautifulSoup(html, 'html.parser')

inning_html = soup.find_all("td", class_=re.compile("yjMSt"))
inning_r = [inning.string for inning in inning_html]
inning_list = []
for i in inning_r:
    i = i.replace("回", "")
    i = i.replace("表", "t")
    i = i.replace("裏", "b")
    i = i.replace("結果", "after")
    i = i.replace("中止", "canceled")
    i = i.replace("試合前", "before")
    inning_list.append(i)

home_team_html = soup.find_all("td", class_="yjMS bb")
home_teams = [home_team.string for home_team in home_team_html]
home_team_list = team_convert(home_teams)

visitor_team_html = soup.find_all("td", class_="yjMS bt bb")
visitor_teams = [visitor_team.string for visitor_team in visitor_team_html]
visitor_team_list = team_convert(visitor_teams)

score_html = soup.find_all("td", class_="score_r")
scores = [score.string for score in score_html]
home_score_list = scores[1::2]
visitor_score_list = scores[0::2]

start_at_html = soup.find_all("td", class_="yjSt bl")
start_at_list = [start_at.string for start_at in start_at_html][1::2]

def team_convert(teams):
    team_list = []
    for t in teams:
        if t = 'ヤクルト':
            team = 'S'
        elif t = '巨人':
            team = 'G'
        elif t = '阪神':
            team = 'T'
        elif t = '広島':
            team = 'C'
        elif t = '中日':
            team = 'D'
        elif t = 'DeNA':
            team = 'DB'
        elif t = 'ソフトバンク':
            team = 'H'
        elif t = '日本ハム':
            t = 'F'
        elif t = 'ロッテ':
            team = 'M'
        elif t = '西武':
            team = 'L'
        elif t = 'オリックス':
            team = 'Bs'
        elif t = '楽天':
            team = 'E'
        team_list.append(team)
    return team_list

# 0:00 refresh data
def refresh():
    Scores.objects.all().delete()

# update data per minute
def save_data():
    for inning, home_team, home_score ,visitor_team, visitor_score, start_at in zip(inning_list, home_team_list, home_score_list, visitor_team_list, visitor_score_list, start_at_list):
        Scores.objects.update_or_create(
            inning = str(inning),
            home_team = str(home_team),
            home_score = str(home_score),
            visitor_team = str(visitor_team),
            visitor_score = str(visitor_score),
            start_at = str(start_at),
            )
