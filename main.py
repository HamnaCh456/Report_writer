from crewai import Agent
from dotenv import load_dotenv
from crewai import Task
from crewai import Crew, Process
from crewai.llm import LLM
import os
from crewai_tools import SerperDevTool
import warnings
from crewai.llm import LLM
import tool
import streamlit as st

warnings.filterwarnings("ignore")


llm = LLM(
    model="gemini/gemini-2.5-flash",  # LiteLLM format: provider/model
    api_key="NA",
    temperature=0.5
)
os.environ["SERPER_API_KEY"] = "NA"
search_web_tool = SerperDevTool(n_results=10)
scraper_tools=tool.MyCustomTool()
researcher = Agent(
    role="Web Researcher",
    goal="Identify the most relevant and reliable sources on {topic}. Return a list of URLs with their titles and summaries.",
    verbose=True,
    memory=False,
    backstory=(
        "You're a skilled researcher responsible for sourcing information only from trustworthy websites. "
        "You use a web search tool to gather sources, and summarize them clearly."
    ),
    llm=llm,
    tools=[search_web_tool],
    allow_delegation=False
)

scraper_agent = Agent(
    role="Report Writer",
    goal="Write a factual, well-organized report using only content from the provided URLs from the researcher.",
    verbose=True,
    memory=False,
    backstory=(
        "You're a factual report writer. You extract information using the scraper tool and present it in a well-structured, unbiased format. "
        "No assumptions, only scraped facts."
    ),
    llm=llm,
    tools=[scraper_tools],
    allow_delegation=False
)
search_task = Task(
    description=(
        "Use the Serper search tool to find 1 highly relevant, up-to-date, and authentic web sources(which could include blogs on medium) about the topic: {topic}."
        "Try to give url of blog on medium or official documentation,in case if user asks about the product"
        "You may design the search query yourself about the topic :{topic} if necessary to get the blogs explicitly for example if a user is giving the {topic} related to product"
        "If the user query about some company then dont change the search query"
        "Make sure the sources are trustworthy and provide valuable information for writing a report."
    ),
    expected_output=(
        "Return a list of the 1 most relevant sources(give preference to official documentation and prewritten blogs) , each formatted as follows:\n"
        "- URL\n"
        "- Page Title\n"
        "- Short Snippet (1-2 sentences summary)\n\n"
        "Example:\n"
        "- URL: https://example.com/article1\n"
        "- Title: 'Introduction to Groq4 Technology'\n"
        "- Snippet: This article explains the architecture and performance benchmarks of Groq4..."
    ),
    agent=researcher,
    tools=[search_web_tool],
)

  
scrape_task = Task(
    description=(
        "Use the 1 URL from the search task to scrape content related to the topic: {topic}. "
        "scrape only the most relevant 1 URL to provide accurate ,factual report."
       
    ),
    expected_output=(
        "A complete report on the topic: {topic}, with Headings and bullet points where necessary,Citations (mention source URLs in parentheses or footnotes)"
    ),
    agent=scraper_agent, 
    tools=[scraper_tools],
    context=[search_task]
)
crew = Crew(
    agents=[researcher,scraper_agent],
    tasks=[search_task,scrape_task],#,scrape_task
    process=Process.sequential,
)

st.title("🕵️ Web Research & Report Generator")

product = st.text_input("Enter a topic or product name:")

if st.button("Generate Report") and product:
    with st.spinner("Researching and compiling report..."):
        result = crew.kickoff(inputs={"topic": product})
        report = result.tasks_output[1].raw
        st.write(report)
