import requests
import bs4
from functions import get_title
from functions import get_price
from functions import get_rating
from functions import get_review
from functions import get_availability

HEADER = {'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language':'en-US , en;q=0.5'
}

URL = "https://www.amazon.in/Sony-PS4-Additional-Dualshock-Controller/dp/B07S3BD2W6/ref=sr_1_1?dchild=1&keywords=playstation+4&qid=1607434099&sr=8-1"
webpage = requests.get(URL, headers=HEADER)
soup = bs4.BeautifulSoup(webpage.content, 'html5lib')

#function calls
print("Product Title=", get_title(soup))
print("Price=", get_price(soup))
print("Rating=", get_rating(soup))
print("User review=", get_review(soup))
print("Availability=", get_availability(soup))
print()