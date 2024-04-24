import requests
from bs4 import BeautifulSoup
import regex as re
import pandas as pd


with open('socialblade_top100.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
soup = BeautifulSoup(html_content, "html.parser")
youtube_links = soup.select('a[href^="/youtube/c"]')


# Print the found links
channel_hrefs = []
channel_ids = []
for link in youtube_links:
    href = link.get('href')
    channel_ids.append(href.split('/')[-1])
    print(channel_ids[-1])

     
# dictionary of lists
dict = {'channel_id': channel_ids}
     
df = pd.DataFrame(dict)
     
# saving the dataframe
df.to_csv('data/top100.csv')
