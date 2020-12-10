import requests
from bs4 import BeautifulSoup
import pyfiglet
ascii_banner = pyfiglet.figlet_format("L 4 c 3 f e r")
print(ascii_banner)
x=input("field--->")
y=input("country-->")
print("\n")
print(" search job from monster.com ")
URL = 'https://www.monster.com/jobs/search/?q='+x+'&where='+y
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
job_elems = results.find_all('section', class_='card-content')
i=0
for elems in job_elems:
    title_elem = elems.find('h2', class_='title')
    company_elem = elems.find('div', class_='company')
    location_elem = elems.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(i)
    i+=1
    print(title_elem.text.strip())
    link = title_elem.find('a')['href']
    print(f"link->{link}")
    print(company_elem.text.strip())
    print(location_elem.text.strip())
