import requests
import bs4

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

res = requests.get(base_url.format(1))

soup = bs4.BeautifulSoup(res.text,'lxml')

#print(soup.select(".product_pod"))

def two_star():

    two_star_titles = []

    for n in range(1,51):

        scrape_url = base_url.format(n)
        res = requests.get(scrape_url)
    
        soup = bs4.BeautifulSoup(res.text,"lxml")
        books = soup.select(".product_pod")
    
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            two_star_titles.append(book.select('a')[1]['title'])       

    return two_star_titles  

def show():

    books = two_star()
    print("All the two starts books title: ")
    for x in range(len(books)):
        print (books[x])


if __name__ == '__main__':

    show_titles = input("Would you like to see all the two starts books titles? Enter 'y' or 'n' ")
    
    if show_titles[0].lower()=='y':
      print("Loading...")
      print("\n")
      show()

    else:
        print(":(")