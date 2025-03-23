from googleapiclient.discovery import build
from django.conf import settings


def youtubetrailer(movie):
    youtube=build('youtube','v3',developerKey=settings.YOUTUBE_API_KEY)

    request=youtube.search().list(
        q=f'{movie} trailer',
        part='snippet',
        type='video'
    )

    response=request.execute()
    #print(response)

    if response.get('items'):
        try:
            video_id=response['items'][0]['id']['videoId']
            video_embed_url=f'https://www.youtube.com/embed/{video_id}'
            return video_embed_url
        except KeyError:
            print("error")
            return None
    else:
        return None 
    
