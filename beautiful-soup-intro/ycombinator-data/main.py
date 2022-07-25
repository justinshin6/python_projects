from bs4 import BeautifulSoup
import requests

# use requests to get information from YCombinator website
response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

# initialize soup 
soup = BeautifulSoup(yc_webpage, 'html.parser')

# find all articles in the YCombinator website 
articles = soup.find_all(name='a', class_='titlelink')

# set up article_texts and article_links
article_texts, article_links = [], []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get('href')
    article_links.append(article_link)

# set up article_upvotes 
article_upvotes = [int(score.getText().split(' ')[0]) for score in soup.find_all(class_='score', name='span')]

def get_largest_point_article(list_upvotes, texts):
    '''
    Returns the article with the largest amount of points (upvotes)

    Parameters: 
    - list: the list of the upvotes 
    - texts: the list of the article texts (titles)

    Returns:
    - the article with the highest number of upvotes 
    '''
    largest_index = list_upvotes.index(max(list_upvotes))
    return texts[largest_index]

def get_lowest_point_article(list_upvotes, texts):
    '''
    Returns the article with the lowest amount of points (upvotes)

    Parameters: 
    - list: the list of the upvotes 
    - texts: the list of the article texts (titles)

    Returns:
    - the article with the lowest number of upvotes 
    '''
    largest_index = list_upvotes.index(min(list_upvotes))
    return texts[largest_index]


if __name__ == '__main__':
    get_largest_point_article(article_upvotes, article_texts)
    get_lowest_point_article(article_upvotes, article_texts)