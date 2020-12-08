import requests
import bs4

HEADER = {'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language':'en-US , en;q=0.5'
}

URL = "https://www.amazon.com/Sony-PlayStation-Pro-1TB-Console-4/dp/B07K14XKZH/"
webpage = requests.get(URL, headers=HEADER)
soup = bs4.BeautifulSoup(webpage.content, 'html5lib')

#function to extract product title
def get_title(soup):
    try:
        #Outer Object tag
        title = soup.find('span', attrs={'id':'productTitle'})
        
        #Inner Navigable string object
        title_value = title.string
        
        #Title as a string value
        title_string = title_value.strip()
    except AttributeError:
        title_string = ""
    return title_string

#function to extract product price 
def get_price(soup):
    try:
        #price object tag
        price = soup.find('span', attrs={'class':'a-size-base a-color-price'}).string.strip()
    except AttributeError:
        price = ""
    return price

#function to extract Product rating
def get_rating(soup):
    try:
        #rating object
        rating = soup.find('i', attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
    except AttributeError:
        rating = ""
    return rating

#function to extract Product User review
def get_review(soup):
    try:
        #review object tag
        review = soup.find('span', attrs={'id':'acrCustomerReviewText'}).string.split()
    except AttributeError:
        review = ""
    return review

#function to extract Product Availability status
def get_availability(soup):
    try:
        #availability object tag
        available = soup.find('div', attrs={'id':'availability'}).string.split()
        available = available.find('span').string.strip()
        if available is not None:
            available = print("In Stock")
        else:
            pass
    except AttributeError:
        available = ""
    return available

#function calls
print("Product Title=", get_title(soup))
print("Price=", get_price(soup))
print("Rating=", get_rating(soup))
print("User review=", get_review(soup))
print("Availability=", get_availability(soup))
print()