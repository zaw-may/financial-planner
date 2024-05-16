from crewai import Agent
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

class FinancialPlanningAgents():
    def financial_planner_agent(self):
        return Agent(
            role = 'Financial Planner Specialist',
            goal = """Help individual achieve their financial goals and secure their financial future""",
            backstory = """Provide ongoing financial advice and guidance to individual user,
            monitor progress towards goals and making adjustments as needed, explain financial concepts, 
            investment strategies and best practice for financial management.""",
            allow_delegation = True,
            verbose = True,
            max_iter = 15,
            tools = [SearchTools.search_internet],
        )
    
    def financial_advisor(self):
        return Agent(
            role = 'Financial Advisor',
            goal = "Assess the individuals\' current financial situation and analyze financial calculation",
            backstory = """Develop and implement comprehensive financial goals, tracking progressive, including budget management, credit management, 
            identify opportunities for tax optimization, asset protection""",
            allow_delegation = True,
            verbose = True,
            tools = [
                SearchTools.search_internet,
                CalculatorTools.calculate_credit_score,
                CalculatorTools.analyze_debt
            ],
        )
    
    def financial_analyst_agent(self):
        return Agent(
            role = 'Financial Analyst',
            goal = 'Provide financial analysis to support decision-making processes',
            backstory = """Analyze financial statements, performance metrics, and economic indicators 
            to assess the financial health, create financial models and forecasts, support strategic planning initiatives.""",
            allow_delegation = True,
            verbose = True,
            tools = [SearchTools.search_internet],
        )