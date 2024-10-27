from crewai import Task
from agents import blog_researcher, blog_writer
from tools import yt_tool


research_taks = Task(
    description="""Get the relevant video transcription for the topic {topic} from the provided Yt channel""",
    agent=blog_researcher,
    tools=[yt_tool],
    expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content.'
)

write_task = Task(
    description="""Write a detailed blog post based on the following input: {topic}""",
    agent=blog_writer,
    expected_output='Summarize the info from the youtube channel video on the topic{topic} and create the content for the blog',
    tools=[yt_tool],
    async_execution=False,
    output_file='new-blog-post.md'
)

