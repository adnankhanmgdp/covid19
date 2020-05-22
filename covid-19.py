import os
import time
try:
	from covid import Covid
	from colorama import Fore, Style, Back
except ImportError:
	print("INSTALLING DEPENDENCIES...")
	os.system('python -m pip install -r requirements.txt')

from covid import Covid
from colorama import Fore, Style, Back
os.system('clear')
covid=Covid()
def covid_worldwide():
	print('Covid-19 Cases Worldwide')
	print(Fore.RED, 'Total Active Cases=',Back.WHITE,Style.BRIGHT,'\b\b', covid.get_total_active_cases(),Style.RESET_ALL)
	print(Fore.RED, 'Total Confirmed Cases=',Back.WHITE,Style.BRIGHT,'\b\b',  covid.get_total_confirmed_cases(),Style.RESET_ALL)
	print(Fore.GREEN, 'Total Recoverd Cases=',Back.MAGENTA,Style.BRIGHT,'\b\b',  covid.get_total_recovered(),Style.RESET_ALL)
	print(Fore.RED, 'Total Deaths=',Back.WHITE,Style.BRIGHT,'\b\b',  covid.get_total_deaths(),Style.RESET_ALL)
	print("\n")
	for i in range(0,20):
		print("_",end="")
		time.sleep(0.2)
	print(Style.RESET_ALL, "\n")

def country_wide(country):
	cont=covid.get_status_by_country_name(country)
	data={key:cont[key] for key in cont.keys() and {"confirmed", "active", "deaths", "recovered"}}
	print('\nCovid-19 Cases in ',Back.YELLOW,Fore.MAGENTA, '\b\b\b', country.upper(), Style.RESET_ALL, '\n')
	time.sleep(0.5)
	print(Fore.RED, "Confirmed=",Back.WHITE,Style.BRIGHT,'\b\b',  data['confirmed'],Style.RESET_ALL)
	time.sleep(0.5)
	print(Fore.RED, "Active=",Back.WHITE,Style.BRIGHT,'\b\b',  data['active'],Style.RESET_ALL)
	time.sleep(0.5)
	print(Fore.GREEN, "Recovered=",Back.MAGENTA,Style.BRIGHT,'\b\b',  data['recovered'],Style.RESET_ALL)
	time.sleep(0.5)
	print(Fore.RED, "Deaths=",Back.WHITE,Style.BRIGHT,'\b\b', data['deaths'], Style.RESET_ALL)
covid_worldwide()
country=input('Enter your Country: ')
try:
    country_wide(country)
except:
	print(Fore.RED, 'No Info for this country!', Style.RESET_ALL)
	time.sleep(1.5)
	print('\n\n',Back.BLUE, 'Countries: ', Style.RESET_ALL,'\n',Fore.RED)
	a=covid.list_countries()
	b=len(a)
	for i in range(0,b):
		c=a[i]
		print(c['name'])
print(Style.RESET_ALL)
	
