
import time
import requests
from bs4 import BeautifulSoup

def continue_crawl(search_history,target_url):
    if len(search_history)>25:
        print("Reached 25 url")
        return False
    elif search_history[len(search_history)-1]==target_url:
        print("Reached Target url")
        return False
    elif search_history[len(search_history)-1] in search_history[:len(search_history)-2]:
        print("Cycle present")
        return False
    else:
        return True


while continue_crawl(article_chain, target_url):


#print(continue_crawl(['https://en.wikipedia.org/wiki/Floating_point','https://en.wikipedia.org/wiki/shit','https://en.wikipedia.org/wiki/Floating_point'],
#                       'https://en.wikipedia.org/wiki/Philosophy'))

def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")

    # TODO: find the first link in the article, or set to None if
    # there is no link in the article.
    article_link = "a url, or None"

    if article_link:
        return article_link


def web_crawl():
    while continue_crawl(article_chain, target_url): 
        # download html of last article in article_chain
        # find the first link in that html
        first_link = find_first_link(article_chain[-1])
        # add the first link to article chain
        article_chain.append(first_link)
        # delay for about two seconds
        #YOUR CODE HERE!
        time.sleep(2)





content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
for element in content_div.find_all("p", recursive=False):
    if element.find("a", recursive=False):
        first_relative_link = element.find("a", recursive=False).get('href')
        break
