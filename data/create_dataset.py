import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the value of API_TOKEN environment variable
api_token = os.getenv('API_TOKEN')

if __name__ == "__main__":

    urls = {
        "top100": "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={0}&maxResults=100&order=date&type=video&key={1}"
    }
    
    df = pd.read_csv("data/top100.csv")
    
    for index, row in df.iterrows():
        channel_id = row['channel_id']
        top_100_videos_url = urls["top100"].format(channel_id, api_token)
        response = requests.get(top_100_videos_url)
        print(response.json())
        break
    
    
    
    # top_10_videos_url = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCgoFStVyEsm8tBZP5NC-aBQ&maxResults=10&order=date&type=video&key=AIzaSyDnVwGFI4KcpzlkPTqSAcvuI-Ot8rEP0kw"
