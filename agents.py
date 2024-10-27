from crewai import Agent
from tools import yt_tool

from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"


blog_researcher = Agent(
    role='Blog Researcher',
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
    backstory="""You are a seasoned blog content researcher with a deep understanding of the blog creation. You excel at identifying and analyzing key points, analyzing trends, and providing relevant insights.""",
    allow_delegation=True,
    verbose=True,
    memory=True,
    tools=[yt_tool]
)

blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    backstory="""You are a seasoned blog writer with a deep understanding of the blog creation. You excel at crafting engaging and informative blog content.""",
    allow_delegation=False,
    verbose=True,
    memory=True,
    tools=[yt_tool]
)

