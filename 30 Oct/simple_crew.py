import os
from dotenv import load_dotenv

from crewai import Agent,Task,Crew,Process,LLM

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

llm =LLM(
    model="openrouter/mistralai/mistral-7b-instruct:free",
    temperature=0.3,
    max_tokens=300,
    api_key=api_key,
    base_url=base_url,
)


researcher = Agent(
        role="Researcher",
        goal="Gather the latest trends and insights on a topic",
        backstory="You are a world-class researcher who finds the most relevant information quickly",
        verbose=True
    )
writer = Agent(
        role="Writer",
        goal="Write a concise summary report based on research findings",
        backstory="You are a skilled technical writer,turning research into readable reports",
        verbose=True
    )
t1 = Task(
        description="Investigate the latest developments in CrewAI and agent-frameworks",

        agent=researcher

    )
t2 = Task(
        description="Write a summary report based on the researcher's output",
        agent=writer
    )
crew = Crew(
        agents=[researcher,writer],
        tasks=[t1,t2],
        process=Process.sequential,
        verbose=True
    )

result = crew.kickoff(inputs={"topic":"CrewAI multi-agent frameworks"})
print("Final result:",result)





