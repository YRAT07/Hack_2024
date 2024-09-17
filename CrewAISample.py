from crewai import Crew
from Agents import TripAgents
from Tasks import TripTasks

agents = TripAgents()
tasks = TripTasks()

file_agent = agents.file_reader_agent()
file_reader_task = tasks.file_reader_task(
      file_agent, "InputData.json", "MathOperations.log", "MathOperations.py")
    
from langchain_ollama import ChatOllama
import os
os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOllama(
    model = "mistral-nemo",
    base_url = "http://localhost:11434")

    
crew = Crew(
            agents=[file_agent,],
            tasks=[file_reader_task,],
            verbose=True,
            manager_llm=llm
        )

result = crew.kickoff()



print("Done")

print(result)

from crewai import Task
from textwrap import dedent
from crewai import Agent, Task, Crew

fileComparisonAgent = Agent(
            role="Compare files",
            goal="Compare contents of file and provide similarity or difference in contents",
            backstory="An expert in understanding JSON files, logs, python code, how execution of python works and ability to correlate all four",
            tools=[
            ],
            verbose=True,
            allow_delegation = False,
            llm=llm
        )

fileComparisonTask = Task(
            description=dedent(f"""
                You will be provided with 3 files contents appended as a single content.
                It will be a combination of JSON file (input file to a code), log file (data logged by the code while trying 
                  to execute code) and code file in python (which when executed on input file, logs the data in log file).
            
                               
            Provided content: {result}


                  You need to compare the code, input file and log file and report any discripencies, if found.
            """),
            agent=fileComparisonAgent,
            expected_output="A detailed analysis about discripency or correlation between logs, input and python code"
)

crew = Crew(
            agents=[fileComparisonAgent,],
            tasks=[fileComparisonTask,],
            verbose=True,
        )

result = crew.kickoff()

print(result)