# 10-Day Weather for Warsaw, Masovian Voivodeship, Poland 
from bs4 import BeautifulSoup
import requests

url = 'https://weather.com/en-IN/weather/tenday/l/a8b0daa43d13b260354967e7b6792eae37e9924dee035d82922e416e63de4051'
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')

weathers = soup.find_all('summary', {
    'class': 'Disclosure--Summary--AvowU DaypartDetails--Summary--2nJx1 Disclosure--hideBorderOnSummaryOpen--LEvZQ'})

for weather in weathers:
    dates = weather.find('h2', {'class': 'DetailsSummary--daypartName--1Mebr'}).text
    day_temp = weather.find('span', {'class': 'DetailsSummary--highTempValue--3x6cL'}).text
    night_temp = weather.find('span', {'class': 'DetailsSummary--lowTempValue--1DlJK'}).text
    types = weather.find('span',{'class':'DetailsSummary--extendedData--aaFeV'}).text
    humidity = weather.find('span', {'data-testid': 'PercentageValue'}).text
    wind = weather.find('span', {'class': 'Wind--windWrapper--1Va1P undefined'}).text

    print('\nDay:', dates, '\nDay Temperature:', day_temp, '\nNight Temperature:', night_temp, '\nHumidity:', humidity,
          '\nWind:', wind, '\nType of weather:', types)
