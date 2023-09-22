import requests
from bs4 import BeautifulSoup

# add your link here
URL = "https://www.azcentral.com/"

# add your keywords here in this list, make sure to add commas! 
# also make sure it is lower case
keywords = [
    "phoenix",
    "weather",
    "police",
    "hotel"
]

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
href = soup.find_all('a', href=True)
links = set()

for tag in href:
    links.update([tag['href'] for word in keywords if word in tag['href'].lower()])

for link in links:
    if not "http" in link:
        print(URL + link)
    else:
        print(link)