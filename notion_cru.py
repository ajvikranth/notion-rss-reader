
import requests, json
from dotenv import load_dotenv
import os

load_dotenv()

token=os.getenv('token')
databaseId=os.getenv('databaseId')


headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def readDatabase():
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"

    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()

    print(res.status_code)
    if res.status_code!=200:
     return None
    return data['results']    



def createPage(news):

    createUrl = 'https://api.notion.com/v1/pages'

    newPageData = {
        "parent": { "database_id": databaseId},
        "properties": {
            "Name": {
                "title": [
                     {
                       "type": "text",
                       "text": {
                             "content": news['Name']
                            }
                     }  
                ]
            },
            "pubDate": {

                         "date": {
                             "start": news['pubDate']
                         }
                    },           
            "description": {
                         "rich_text": [
                              {
                                   "text": {
                                        "content": news['description']
                                   }
                              }
                         ]
                    },                       
            "link": {
                         "url": news['link'] 
                    }

        }
    }
    
    data = json.dumps(newPageData)

    res = requests.request("POST", createUrl, headers=headers, data=data)

    print(res.status_code)
    if res.status_code!=200:
     return True

def updatePage(pageId, news):
    updateUrl = f"https://api.notion.com/v1/pages/{pageId}"

    updateData = {
        "properties": {
            "Name": {
                "title": [
                     {
                       "type": "text",
                       "text": {
                             "content": news['Name']
                            }
                     }  
                ]
            },
            "pubDate": {

                         "date": {
                             "start": news['pubDate']
                         }
                    },           
            "description": {
                         "rich_text": [
                              {
                                   "text": {
                                        "content": news['description']
                                   }
                              }
                         ]
                    },                       
            "link": {
                         "url": news['link']
                    }

        }
    }

    data = json.dumps(updateData)

    response = requests.request("PATCH", updateUrl, headers=headers, data=data)

    print(response.status_code)

    if response.status_code!=200:
     return True















