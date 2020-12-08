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
        price = soup.find('span', attrs={'class':'a-size-medium a-color-price priceBlockBuyingPriceString'}).string.strip()
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
        available = soup.find('div', attrs={'id':'availability'})
        available = available.find('span').string.strip()

    except AttributeError:
        available = "Not available"
    return available
