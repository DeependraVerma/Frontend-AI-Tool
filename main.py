from crewai import Crew,Process
from tasks.html_task import html_code_task
from agents.html_agent import html_gen_agent

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[html_gen_agent],
    tasks=[html_code_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'Login Page'})
print(result)