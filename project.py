import requests
from bs4 import BeautifulSoup

url = input("Insert a url: ")
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

link_elements = soup.find_all('a', href=True)
links = [a['href'] for a in link_elements]

for link in links:
    print(link)