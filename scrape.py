import webbrowser
import requests
import bs4

website = 'https://twitter.com/sam_beckman'
res = requests.get(website)
print("Status: ", res.status_code == requests.codes.ok)
twitter = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(twitter))
print(twitter.)
