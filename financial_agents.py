from crewai import Agent

class FinancialPlanningAgents():
    def financial_planner_agent(self):
        return Agent(
            role = 'Financial Planner',
            goal = """Help individual achieve their financial goals and secure their financial future""",
            backstory = """Provide ongoing financial advice and guidance to individual user,
            monitor progress towards goals and making adjustments as needed, explain financial concepts, 
            investment strategies and best practice for financial management.""",
            allow_delegation = True,
            verbose = True,
            max_iter = 15,
            tools = [],
        )
    
    def estate_planner_agent(self):
        return Agent(
            role = 'Estate Planner',
            goal = 'Analyze estate information and planning process',
            backstory = """Develop and implement comprehensive estate plans, including wills, trusts, powers of attorney, 
            identiry opportunities for tax optimization, asset protection""",
            allow_delegation = True,
            verbose = True,
            tools = [],
        )
    
    def insurance_planner_agent(self):
        return Agent(
            role = 'Insurance Planner',
            goal = 'Assist the individual with appropriate insurance coverage and risk management strategies',
            backstory = """Provide guidance on various types of insurance, including health insurance, property insurance, 
            recommend insurance products and coverage options, review existing insurance policies periodically 
            to evaluate coverage adequancy and cost-effectiveness.""",
            allow_delegation = True,
            verbose = True,
            tools = [],
        )
    
    def financial_analyst_agent(self):
        return Agent(
            role = 'Financial Analyst',
            goal = 'Provide financial analysis to support decision-making processes',
            backstory = """Analyze financial statements, performance metrics, and economic indicators 
            to assess the financial health, create financial models and forecasts, support strategic planning initiatives.""",
            allow_delegation = True,
            verbose = True,
            tools = [],
        )