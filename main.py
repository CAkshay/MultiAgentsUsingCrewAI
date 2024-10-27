from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_taks, write_task
import streamlit as st
from tools import store_user_input

crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_taks, write_task],
    verbose=True,
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

def main():
    st.title("Blog generation with multi agents using CrewAI")
    
    # Take user input
    user_input = st.text_input("Enter the Youtube channel name")
    query = st.text_input("Enter the topic of the blog")

    if st.button("Submit"):
        if user_input and query:
            # Store user input using a function from tools.py
            store_user_input(user_input)
            blog = crew.kickoff(inputs={'topic': query})
            st.write(blog)

if __name__ == "__main__":
    main()
