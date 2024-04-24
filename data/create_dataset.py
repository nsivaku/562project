import requests

if __name__ == "__main__":

    urls = {
        "search_channel": "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={0}&maxResults=1&order=date&type=video&key={1}",
        "top10": "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={0}&maxResults=10&order=date&type=video&key={1}"
    }
    
    top_10_videos_url = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCgoFStVyEsm8tBZP5NC-aBQ&maxResults=10&order=date&type=video&key=AIzaSyDnVwGFI4KcpzlkPTqSAcvuI-Ot8rEP0kw"
    "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=MrBeast&maxResults=1&order=date&type=video&key=AIzaSyDnVwGFI4KcpzlkPTqSAcvuI-Ot8rEP0kw"