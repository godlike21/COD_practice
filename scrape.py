import requests
import bs4
from functions import get_title
from functions import get_price
from functions import get_rating
from functions import get_review
from functions import get_availability
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

HEADER = {'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language':'en-US , en;q=0.5'
}


URL = 'https://www.amazon.in/'
driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)
driver.get(URL)
search_button = driver.find_element_by_id("twotabsearchtextbox")
search_term = str(input("What do you want?\n: "))
search_button.send_keys(search_term)
search_button.send_keys(Keys.ENTER)

#webpage = requests.get(URL, headers=HEADER)
soup = bs4.BeautifulSoup(driver.page_source, 'html5lib')

links = soup.find_all('a', attrs={'class':'a-link-normal s-no-outline'})
links_list = []
for link in links:
    links_list.append(link.get('href'))

for link in links_list:
    new_webpage = driver.get(URL + link)
    new_soup = bs4.BeautifulSoup(driver.page_source, 'html5lib')

    #function calls
    print("Product Title=", get_title(new_soup))
    print("Price=", get_price(new_soup))
    print("Rating=", get_rating(new_soup))
    print("User review=", get_review(new_soup))
    print("Availability=", get_availability(new_soup))
    print()
    print()