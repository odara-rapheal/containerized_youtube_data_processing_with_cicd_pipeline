from googleapiclient.discovery import build
from django.conf import settings

YOUTUBE_API_KEY = 'AIzaSyBYkSoT639R7svjPeXidd0V2uIiutvya84'  # Add your YouTube API key here

def fetch_video_details(video_id):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    request = youtube.videos().list(
        part='snippet,statistics',
        id=video_id
    )
    response = request.execute()
    if response['items']:
        video_data = response['items'][0]
        return {
            'title': video_data['snippet']['title'],
            'description': video_data['snippet']['description'],
            'view_count': video_data['statistics'].get('viewCount', 0),
            'like_count': video_data['statistics'].get('likeCount', 0)
        }
    return None

def fetch_video_comments(video_id, max_results=100):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    comments = []
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=max_results,
        textFormat='plainText'
    )
    while request:
        response = request.execute()
        for item in response.get('items', []):
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
        request = youtube.commentThreads().list_next(request, response)
    return comments
