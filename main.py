#Run the following in Colab
!pip install youtube-transcript-api

from youtube_transcript_api import YouTubeTranscriptApi

#This will only work for videos having subtitles
url = "https://www.youtube.com/watch?v=fHw188SBb9k"


# Extract the video ID from the URL
video_id = url.split("watch?v=")[1]


transcript = YouTubeTranscriptApi.get_transcript(video_id)


output=''
for x in transcript:
  sentence = x['text']
  output += f'{sentence} '

print(output)
