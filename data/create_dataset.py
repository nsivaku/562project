import requests
import pandas as pd
from tqdm import tqdm
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

if __name__ == "__main__":

    urls = {
        "top101": "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={0}&maxResults=100&order=date&type=video&key={1}",
        "subCount": "https://www.googleapis.com/youtube/v3/channels?part=statistics&id={0}&fields=items/statistics/subscriberCount&key={1}"
    }
    
    
    df = pd.read_csv("data/top100.csv")
    
    final_df = pd.DataFrame(columns=['channel_id', 'video_id', 'video_title', 'previous_video_view', 'previous_video_comments', 'sub_count'])
    
    
    for index, row in tqdm(df.iterrows(), total=df.shape[0]):
        channel_id = row['channel_id']

        top_101_videos_url = urls["top101"].format(channel_id, api_key)
        sub_count_url = urls["subCount"].format(channel_id, api_key)
        
        # print(top_101_videos_url)
        response = requests.get(top_101_videos_url)
        data = response.json()
        print(data)
        videos = data['items']
        
        sub_count = requests.get(sub_count_url).json()['items'][0]['statistics']['subscriberCount']
        for i, vid in enumerate(videos):
            # add row to dataframe with channel_id, video_id, video_title, previous_video_view, previous_video_comments
            if i == len(videos) - 1:
                break
            
            id = vid['id']['videoId']
            
            image_url = vid['snippet']['thumbnails']['high']['url']
            img_data = requests.get("https://img.youtube.com/vi/{0}/hqdefault.jpg".format(id)).content
            with open(f'thumbnails/{id}.jpg', 'wb') as f:
                f.write(img_data)
                
            title = vid['snippet']['title']
            
            prev_vid_data = requests.get("https://www.googleapis.com/youtube/v3/videos?part=statistics&id={0}&key={1}".format(id, api_key)).json()
            prev_vid_data_counts = prev_vid_data['items'][0]['statistics']
            try:
                prev_view_count = prev_vid_data_counts['viewCount']
            except:
                prev_view_count = -1
            try:
                prev_comment_count = prev_vid_data_counts['commentCount']
            except:
                prev_comment_count = -1
            
            # add row
            final_df.loc[len(final_df.index)] = [channel_id, id, title, int(prev_view_count), int(prev_comment_count), int(sub_count)]
            
        # print(response.json())

    final_df.to_csv("data/top100_videos.csv")
    
    
    
    # top_10_videos_url = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCgoFStVyEsm8tBZP5NC-aBQ&maxResults=10&order=date&type=video&key=AIzaSyDnVwGFI4KcpzlkPTqSAcvuI-Ot8rEP0kw"
