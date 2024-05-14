from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from financial_agents import FinancialPlanningAgents
from financial_tasks import FinancialPlanningTasks

from dotenv import load_dotenv
load_dotenv()

