import requests
from bs4 import BeautifulSoup
import pyfiglet
from termcolor import colored

banner = pyfiglet.figlet_format("GoLookUp Scraper", font='small')
coloredBanner = colored(banner, 'green')
print(coloredBanner)

#The URL where you type in the first and last name
searchurl = "https://golookup.com/lander/people/default/processPeopleSearch"
#The Results URL that pulls up the informaiton
resultsurl = "https://golookup.com/lander/people/default/results"

def userInput(): 
    global firstName
    global lastName
    global state
    while True:
        prompt = colored("First name: ", 'magenta')
        firstName = input(prompt)
        if firstName.isdigit():
            print("Error")
            continue
        else:
           break  
    prompt_2 = colored("Last name: ", 'magenta')    
    lastName = input(prompt_2)
    prompt_3 = colored("What's the state? Skip if you want to do all states: ", 'magenta')
    state = input(prompt_3)
userInput()



#The Payload that's sent to the Search URL
payload={
    'nosplit': 1,
    
    'firstName': firstName,
    'lastName': lastName,
    'state': state,


}

#The header that disguises you. Without this, the website will block you
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

#Session connecting the SearchURL and the ResultsURL together
def results():
 with requests.Session() as s:
    try: #Looks for if there's "no results" first
        s.post(searchurl, headers=headers, data=payload)
        r = s.get(resultsurl, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        results = soup.find(id='content')
        info = results.find_all('div', class_='alert alert-danger')
        print(info[0].text)
    except: #If there is a result, this block will show it
        s.post(searchurl, headers=headers, data=payload)
        r = s.get(resultsurl, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        results = soup.find(id='results')
        info = results.find_all('div', class_='tr clearfix process-record mobile-margin-5')
        print(info[0].text)

results()

input()