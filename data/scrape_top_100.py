import requests
from bs4 import BeautifulSoup
import regex as re
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')


with open('socialblade_top100.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
soup = BeautifulSoup(html_content, "html.parser")
youtube_links = soup.select('a[href^="/youtube/c"]')


# Print the found links
channel_hrefs = []
channel_ids = []
for link in youtube_links:
    href = link.get('href')
    
    
    if href.split('/')[2] == 'c':
        try:
            response = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&maxResults=1&q={0}&key={1}".format(href.split('/')[-1], api_key))
            print(response.json())
            id = response.json()['items'][0]['id']['channelId']
            channel_ids.append(id)
        except:
            print("error on", href)
    else:
        channel_ids.append(href.split('/')[-1])
    print(channel_ids[-1])

dict = {'channel_id': channel_ids}
     
df = pd.DataFrame(dict)
     
# saving the dataframe
df.to_csv('data/top100.csv')
