import os
from crewai import Agent, LLM
from crewai.tools import tool
from dotenv import load_dotenv
load_dotenv()


os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

html_gen_agent = Agent(
    role='HTML Code Generator',
    goal="Generate HTML code as per the user's query",
    backstory="You are an expert HTML code generator for {topic}. You are also expert in industry standard HTML code generation. You will be given the user's query and you will generate the HTML code as per the requirements.",
    verbose=True,
    allow_delegation=True,
    llm=LLM(
        model="gemini/gemini-1.5-flash-8b",
        temperature=0.2
    )
)
