
#import get to call a get request on the site
from requests import get

#get the first page of the east bay housing prices
response = get('https://fargo.craigslist.org/search/sss?query=truck&sort=rel&hasPic=1') #get rid of those lame-o's that post a housing option without a pic using their filter

from bs4 import BeautifulSoup
html_soup = BeautifulSoup(response.text, 'html.parser')

#get the macro-container for the housing posts
posts = html_soup.find_all('li', class_= 'result-row')
print(type(posts)) #to double check that I got a ResultSet
print(len(posts)) #to double check I got 120 (elements/page)

#grab the first post
post_one = posts[0]

#grab the price of the first post
post_one_price = post_one.a.text
post_one_price.strip()

#grab the time of the post in datetime format to save on cleaning efforts
post_one_time = post_one.find('time', class_= 'result-date')
post_one_datetime = post_one_time['datetime']

#title is a and that class, link is grabbing the href attribute of that variable
post_one_title = post_one.find('a', class_='result-title hdrlnk')
post_one_link = post_one_title['href']

#easy to grab the post title by taking the text element of the title variable
post_one_title_text = post_one_title.text

#grabs the whole segment of housing details. We will need missing value handling in the loop as this kind of detail is not common in posts
#the text can be split, and we can use indexing to grab the elements we want. number of bedrooms is the first element.
#sqft is the third element

post_one_odometer = post_one.find('span', class_ = 'odometer')#.text.split()[0]

print(post_one_price)
print(post_one_title_text)
print(post_one_odometer)