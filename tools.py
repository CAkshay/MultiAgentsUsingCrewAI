from crewai_tools import YoutubeChannelSearchTool

user_data = {}

def store_user_input(user_input):
    user_data['input'] = user_input

def get_user_input():
    return user_data.get('input', None)

yt_tool = YoutubeChannelSearchTool(youtube_channel_handle=get_user_input())

