from crewai import Task

class FinancialPlanningTasks():
    def provide_financial_concepts(self, agent):
        return Task(
            description = f'Collect latest financial information, including investment, real estate news, taxes rates, and risk management for financial growth.',
            agent = agent,
            async_execution = True,
            expected_output = """A list of financial documentation with titles, URLs and a brief summary for each.
                Example Output:
                [
                    {
                        'title': 'How To Trade Stocks: Six Steps To Get Started',
                        'url': 'https://example.com/article1',
                        'summary': 'Trading stocks can be a fascinating and lucrative way to grow your wealth. However, the stock market...'
                    },
                    {{...}}
                ]
            """
        )
    
    def claculate_financial_task(self, agent, context):
        return Task(
            description = 'Assess the individual\'s current financial situation with specific data variables and calculate for score',
            agent = agent,
            async_execution = True,
            context = context,
            expected_output = """A markdown-formatted analysis for each calculation, including detailed bullet points. 
                The result should be bold letter and underlined.
                Example Output:
                ## Credit Score \n\n
                Alert: Credit_Score \n\n
            """
        )

    def suggest_financial_health(self, agent, context):
        return Task(
            description = 'Suggest and summarize the financial concepts and the individual\'s current financial situation',
            agent = agent,
            async_execution = True,
            context = context,
            expected_output = """A complete recommendation in markdown format, with a consisten style and layout.
                Example Output:
                # Recommendation for your current financial situation \n\n
                - Option1 \n
                - Option2 \n
            """
        )