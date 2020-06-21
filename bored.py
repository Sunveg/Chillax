from bs4 import BeautifulSoup
import requests
import time

def select():
    selection = int(input())
    if selection == 1:
        type = "feature"
        return type
    elif selection == 2:
        type = "tv_series"
        return type
    elif selection == 3:
        type=""
        return type
    else:
        print("Wrong selection :(\nEnter again\n")
        return "wrong"

time.sleep(1)
print("\nBored bruh?")
time.sleep(1)
print("\nHere are some movies/series for you")
time.sleep(1)
print("Enter the duration separated by space   e.g YYYY YYYY\n")
years = input()
start_year, end_year = years.split(' ')
print("\nENTER:\n1 : Movie list\n2 : TV series\n3 : Mixed\n")

temp = select()
while temp == "wrong":
    temp = select()

url = 'https://www.imdb.com/search/title/?release_date=' + start_year +',' + end_year + '&title_type=' + temp 

source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

print(f'\nTop 50 list from {start_year} to {end_year} according to popularity')
time.sleep(1)
print("Go watch them all !\n")
time.sleep(1)

content = soup.find('div', attrs={"class":"lister-list"})

for movie in content.findAll('h3', attrs={"class":"lister-item-header"}):
    year = movie.find_next('span', attrs={"class":"lister-item-year text-muted unbold"})
    rating = movie.find_next('div', attrs={"name":"ir"})
    time.sleep(0.2)
    print(f'{movie.span.text} {movie.a.text} {year.text}  IMDB : {rating.strong.text}')

time.sleep(1)
print("\n\nENJOYYYYYYY :) !!!!")
time.sleep(1)

