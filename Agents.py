from crewai import Agent
from CalculatorTools import CalculatorTools
from ReadFileTools import ReadFileTools
from crewai import Agent, Task, Crew
from langchain_ollama import ChatOllama
from langchain.llms import Ollama
import os
os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOllama(
    model = "mistral-nemo",
    base_url = "http://localhost:11434")

class TripAgents():

    def file_reader_agent(self):
        return Agent(
            role="File reader",
            goal="Read local file from the path provided",
            backstory="An expert in reading files and returning the content",
            tools=[
                ReadFileTools.readFile,
            ],
            verbose=True,
            allow_delegation = False,
            llm=llm
        )
