import requests
from bs4 import BeautifulSoup



#scraping function
def scraper(url):
    article_list=[]
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')        
        for ariticle in articles:
            title = ariticle.find('title').text
            description = ariticle.find('description').string
            s = BeautifulSoup(description, features='lxml')
            try:
                s.a.decompose()
                description=s.text
            except:
                pass
                        
            link = ariticle.find('link').text
            published = ariticle.find('pubDate').text
            article = {
                'Name': title,
                'description': description,
                'link': link,
                'pubDate': published
                }
            article_list.append(article)
        return article_list
        
        
        
    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)

