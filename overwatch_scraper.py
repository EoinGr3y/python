import requests
import bs4
import re
import os
import datetime


def findMatches(urls, searchTerms):
    matchingArticles = []
    var test = []

    for url in urls:
        for searchTerm in searchTerms:
            matchingArticles.extend(getMatchingPosts(url, searchTerm))

    return matchingArticles

def getMatchingPosts(url, searchTerm):
    print('Url - ' + url + ', search term - ' + searchTerm)
    res = requests.get(url, headers={'User-agent': 'your bot 0.1'})
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    articles = soup.find_all("a", "title")
    matchingArticles = []

    for article in articles:
        if searchTerm in article.get_text():
            matchingArticles.append(article)

    return matchingArticles

def removeDuplicates(matchingArticles, filePathString):
    uniqueMatchingArticles = []
    with open(filePathString, 'r') as myFile:
        content = myFile.read()

        for matchedArticle in matchingArticles:
            if matchedArticle.get_text() not in content:
                uniqueMatchingArticles.append(matchedArticle)
    myFile.close()

    return uniqueMatchingArticles

def writeToFile(matchingArticles, filePathString):
    currentDate = datetime.datetime.now().strftime("%Y-%m-%d")

    with open(filePathString, 'a') as myFile:
        for matchedArticle in matchingArticles:
            text = matchedArticle.get_text()
            href = matchedArticle['href']
            articleEntry = '{0} - {1} - {2}\n'.format(currentDate, text, href)
            myFile.write(articleEntry)
    myFile.close()


urls = ['https://www.reddit.com/r/Overwatch/', 'https://www.reddit.com/r/OverwatchUniversity/']
searchTerms = ['Ana', 'McCree', 'Zenyatta']
matchingArticles = findMatches(urls, searchTerms)
uniqueMatchingArticles = removeDuplicates(matchingArticles, 'C:\\Users\\eoing\\Documents\\Notes\\Overwatch\\Articles.txt')

if uniqueMatchingArticles is not None:
    writeToFile(uniqueMatchingArticles, 'C:\\Users\\eoing\\Documents\\Notes\\Overwatch\\Articles.txt')
