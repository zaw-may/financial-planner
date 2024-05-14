from langchain.tools import tool


class CalculatorTools():

    @tool("Make a calculation")
    def calculate(operation):
        """Useful to perform any mathematical calculations, 
        like sum, minus, multiplication, division, etc.
        The input to this tool should be a mathematical 
        expression, a couple examples are `200*7` or `5000/2*10`
        """
        return eval(operation)
  
    def calculate_credit_score(payment_history, credit_utilization, credit_history_length, types_of_credit, new_credit_inquiries):
        weights = {
            'payment_history': 0.35,
            'credit_utilization': 0.30,
            'credit_history_length': 0.15,
            'types_of_credit': 0.10,
            'new_credit_inquiries': 0.10
        }

        credit_score = (
            payment_history * weights['payment_history'] +
            credit_utilization * weights['credit_utilization'] +
            credit_history_length * weights['credit_history_length'] +
            types_of_credit * weights['types_of_credit'] +
            new_credit_inquiries * weights['new_credit_inquiries']
        )    

        return credit_score
    
    def analyze_debt(outstanding_debt, annual_income, credit_utilization_ratio):
        debt_to_income_ratio = outstanding_debt / annual_income
        credit_utilization = credit_utilization_ratio
        
        return debt_to_income_ratio, credit_utilization

  
