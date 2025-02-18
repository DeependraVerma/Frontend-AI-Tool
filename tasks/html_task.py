from crewai import Task
from agents.html_agent import html_gen_agent

html_code_task = Task(
    name="Generate HTML code for - {topic}",
    description="Generate HTML code as per the user's query",
    agent=html_gen_agent,
    expected_output="A structured HTML code as per the user's query for industry standard use."
)