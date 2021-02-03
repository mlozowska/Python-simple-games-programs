from bs4 import BeautifulSoup
import requests


url = 'https://weather.com/en-IN/weather/tenday/l/a8b0daa43d13b260354967e7b6792eae37e9924dee035d82922e416e63de4051'
response = requests.get(url)
# print(response)
data = response.text
# print(data)
soup = BeautifulSoup(data, 'html.parser')

weathers = soup.find_all('summary', {'class': 'Disclosure--Summary--AvowU DaypartDetails--Summary--2nJx1 Disclosure--hideBorderOnSummaryOpen--LEvZQ'})

for weather in weathers:
    days = soup.find('h2', {'class': 'DetailsSummary--daypartName--1Mebr'}).text
    # degrees = soup.find('span',{'data-testid':'TemperatureValue'}).text
    # types = soup.find('span',{'class':'DetailsSummary--extendedData--aaFeV'}).text
    # night_temp = soup.find('span',{'data-testid':'PercentageValue'}).text
    # print('Days: ', days, 'Temperature:', degrees, 'Type of weather:', types, 'Temperature at night:', night_temp)
    print(days)


