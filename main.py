from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from financial_agents import FinancialPlanningAgents
from financial_tasks import FinancialPlanningTasks

from dotenv import load_dotenv
load_dotenv()

OpenAIModel = ChatOpenAI(model='gpt-3.5-turbo-0125')

print("Financial Planning Journey")
print("****************************")

payment_history = input("Your payment history (for example: 0.90)\n")
credit_utilization = input("Your credit utilization ratio (for example: 0.25)\n")
credit_history_length = input("Your credit history in terms of years (for example: 5)\n")
types_of_credit = input("Types of credit accounts such as 1 for credit cards, 2 for loans (for example: 1)\n")
new_credit_inquires = input("How many new credit inquires in the past 6 months (for example: 2)\n")
outstanding_debt = input("Your total outstanding debt (for example: 809.98)\n")
annual_income = input("Your yearly income (for example: 19114.12)\n")

agents = FinancialPlanningAgents()
tasks = FinancialPlanningTasks()

financial_planner_agent = agents.financial_planner_agent()
financial_advisor_agent = agents.financial_advisor()
financial_analyst_agent = agents.financial_analyst_agent()

provide_financial_concepts = tasks.provide_financial_concepts(financial_planner_agent)
claculate_financial_task = tasks.claculate_financial_task(financial_advisor_agent)
suggest_financial_health = tasks.suggest_financial_health(financial_analyst_agent)

crew = Crew(
    name = 'Financial Planning Crew',
    agents = [
        financial_planner_agent,
        financial_advisor_agent,
        financial_analyst_agent
    ],
    tasks = [
        provide_financial_concepts,
        claculate_financial_task,
        suggest_financial_health
    ],
    manager_llm=OpenAIModel,
    verbose=True
)

crew.add_process(
    Process(
        name = 'Calculate Credit Score',
        agent = financial_advisor_agent,
        tool = 'CalculatorTools.calculate_credit_score',
        inputs = {
            'payment_history': float(payment_history),
            'credit_utilization': float(credit_utilization),
            'credit_history_length': int(credit_history_length),
            'types_of_credit': int(types_of_credit),
            'new_credit_inquiries': int(new_credit_inquires)
        }
    )
)

crew.add_process(   
    Process(
        name = 'Analyze Debt',
        agent = financial_advisor_agent,
        tool = 'CalculatorTools.analyze_debt',
        inputs = {
            'outstanding_debt': float(outstanding_debt),
            'annual_income': float(annual_income),
            'credit_utilization_ratio': float(credit_utilization)
        }
    )
)

results = crew.kickoff()

print("Crew Work Results:")
print("*******************")
print(results)