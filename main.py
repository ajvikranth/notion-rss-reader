from notion_cru import createPage, readDatabase, updatePage
import rss_scraper
from datetime import datetime, timedelta, date
import sys

"""
News format
news={
    'Name':'Creators can now turn live gameplay clips into Reels on Facebook Gaming',
    'pubDate':'2022-07-21',
    'description':"Facebook Gaming has rolled out a new 'Clips to Reels' feature for all creators to to convert live gameplay clips into Reels",
    'link':"https://economictimes.indiatimes.com/tech/technology/creators-can-now-turn-live-gameplay-clips-into-reels-on-facebook-gaming/articleshow/93022445.cms"
    }
"""
def main():
    url='https://economictimes.indiatimes.com/news/india/rssfeeds/81582957.cms'  

    news=rss_scraper.scraper(url)

    if news is None:
        sys.exit('scrapping failed')

    # gets all db-ids that need to be updated(older than 2 days)

    ids=[]
    read_database=readDatabase()

    if read_database is None:
        sys.exit('database read failed')

    for result in read_database:
        date_object=datetime.strptime(result['created_time'], '%Y-%m-%dT%H:%M:%S.%f%z')
        
        if date.today()-date_object.date()>timedelta(2):
            ids.append(result['id'])
            
    # updates the old news and creates news if there is no old news to be updated
    ids_len=len(ids)
    news_len=len(news)

    # if old news are more than new news
    if ids_len> news_len:
        ids_len=news_len

    for i in range(ids_len):
        upd_res=updatePage(ids[i],news[i])
        if upd_res is True:
            print('create failed for ',news[i]['Name'])        
    for j in range(ids_len,len(news)-ids_len):
        cre_res=createPage(news[j])
        if cre_res is True:
            print('create failed for ',news[j]['Name'])    

if __name__ == "__main__":
    main()