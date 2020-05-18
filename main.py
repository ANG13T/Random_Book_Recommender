import requests
from bs4 import BeautifulSoup
import random

allBooks = []
allBooksLength = 0
file = open("recommendedBooks.txt","a") 

url = "https://medium.com/world-literature/creating-the-ultimate-list-100-books-to-read-before-you-die-45f1b722b2e5"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
titles = soup.find_all('em')
for title in titles:
    title = str(title)
    words = title.split('<')
    words = words[1].split('>')
    words = words[1]
    allBooks.append(words)

allBooks = allBooks[1:]
allBooksLength = len(allBooks)
randomNumber = random.randint(0, allBooksLength)
randomBook = allBooks[randomNumber]
print("Recommended Book:")
print(randomBook)
file.write(randomBook + '\n')
file.close()





