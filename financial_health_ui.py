import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('Financial Health Dashboard')

#Key Metrics (Section 1)
#data1 = pd.read_csv('data\sample_financial_data.csv', low_memory = False)
financial_data = [
    {'user_id': 'S001', 'month': 'Jan', 'user_name': 'Su', 'age': 25, 'SSN': '821-00-0265', 'occupation': 'Scientist', 'annual_income': 19114.12, 'monthly_inhand_salary': 1824.84333333333, 'num_bank_accounts': 3, 'num_credit_card': 4, 'interest_rate': 3, 'num_of_loan': 4, 'type_of_loan': 'Auto Loan, Credit-Builder Loan, Personal Loan, and Home Equity Loan', 'delay_from_due_date': 3, 'num_of_delayed_payment': 7, 'changed_credit_limit': 11.27, 'num_credit_inquiries': 4, 'credit_mix': 'Good', 'outstanding_debt': 809.98, 'credit_utilization_ratio': 26.822619623699, 'credit_history_age': '22 Years and 1 Months', 'payment_of_min_amount': 'No', 'total_EMI_per_month': 49.5749492148942, 'amount_invested_monthly': 80.4152954390025, 'payment_behaviour': 'High_spent_Small_value_payments', 'monthly_balance': 312.494088679437, 'credit_score': 'Good'},
    {'user_id': 'S001', 'month': 'Feb', 'user_name': 'Su', 'age': 25, 'SSN': '821-00-0265', 'occupation': 'Scientist', 'annual_income': 19114.12, 'monthly_inhand_salary': 1824.84333333333, 'num_bank_accounts': 3, 'num_credit_card': 4, 'interest_rate': 3, 'num_of_loan': 4, 'type_of_loan': 'Auto Loan, Credit-Builder Loan, Personal Loan, and Home Equity Loan', 'delay_from_due_date': 1, 'num_of_delayed_payment': 7, 'changed_credit_limit': 11.27, 'num_credit_inquiries': 4, 'credit_mix': 'Good', 'outstanding_debt': 809.98, 'credit_utilization_ratio': 31.9449600553842, 'credit_history_age': '23 Years and 2 Months', 'payment_of_min_amount': 'No', 'total_EMI_per_month': 49.5749492148942, 'amount_invested_monthly': 118.280221622367, 'payment_behaviour': 'Low_spent_Large_value_payments', 'monthly_balance': 284.629162496072, 'credit_score': 'Good'},
    {'user_id': 'S001', 'month': 'Mar', 'user_name': 'Su', 'age': 25, 'SSN': '821-00-0265', 'occupation': 'Scientist', 'annual_income': 19114.12, 'monthly_inhand_salary': 1824.84333333333, 'num_bank_accounts': 3, 'num_credit_card': 4, 'interest_rate': 3, 'num_of_loan': 4, 'type_of_loan': 'Auto Loan, Credit-Builder Loan, Personal Loan, and Home Equity Loan', 'delay_from_due_date': 3, 'num_of_delayed_payment': 7, 'changed_credit_limit': 11.27, 'num_credit_inquiries': 4, 'credit_mix': 'Good', 'outstanding_debt': 809.98, 'credit_utilization_ratio': 28.6093520220699, 'credit_history_age': '22 Years and 3 Months', 'payment_of_min_amount': 'No', 'total_EMI_per_month': 49.5749492148942, 'amount_invested_monthly': 81.699521264648, 'payment_behaviour': 'Low_spent_Medium_value_payments', 'monthly_balance': 331.209862853791, 'credit_score': 'Good'},
    {'user_id': 'S001', 'month': 'Apr', 'user_name': 'Su', 'age': 25, 'SSN': '821-00-0265', 'occupation': 'Scientist', 'annual_income': 19114.12, 'monthly_inhand_salary': 1824.84333333333, 'num_bank_accounts': 3, 'num_credit_card': 4, 'interest_rate': 3, 'num_of_loan': 4, 'type_of_loan': 'Auto Loan, Credit-Builder Loan, Personal Loan, and Home Equity Loan', 'delay_from_due_date': 5, 'num_of_delayed_payment': 4, 'changed_credit_limit': 6.27, 'num_credit_inquiries': 4, 'credit_mix': 'Good', 'outstanding_debt': 809.98, 'credit_utilization_ratio': 31.3778618695824, 'credit_history_age': '22 Years and 4 Months', 'payment_of_min_amount': 'No', 'total_EMI_per_month': 49.5749492148942, 'amount_invested_monthly': 199.458074391071, 'payment_behaviour': 'Low_spent_Small_value_payments', 'monthly_balance': 223.451309727368, 'credit_score': 'Good'},
    {'user_id': 'S001', 'month': 'May', 'user_name': 'Su', 'age': 25, 'SSN': '821-00-0265', 'occupation': 'Scientist', 'annual_income': 19114.12, 'monthly_inhand_salary': 1824.84333333333, 'num_bank_accounts': 3, 'num_credit_card': 4, 'interest_rate': 3, 'num_of_loan': 4, 'type_of_loan': 'Auto Loan, Credit-Builder Loan, Personal Loan, and Home Equity Loan', 'delay_from_due_date': 6, 'num_of_delayed_payment': 7, 'changed_credit_limit': 11.27, 'num_credit_inquiries': 4, 'credit_mix': 'Good', 'outstanding_debt': 809.98, 'credit_utilization_ratio': 24.797346908845, 'credit_history_age': '22 Years and 5 Months', 'payment_of_min_amount': 'No', 'total_EMI_per_month': 49.5749492148942, 'amount_invested_monthly': 41.4201530862173, 'payment_behaviour': 'High_spent_Medium_value_payments', 'monthly_balance': 341.489231032222, 'credit_score': 'Good'},
    {'user_id': 'S001', 'month': 'Jun', 'user_name': 'Su', 'age': 25, 'SSN': '821-00-0265', 'occupation': 'Scientist', 'annual_income': 19114.12, 'monthly_inhand_salary': 1824.84333333333, 'num_bank_accounts': 3, 'num_credit_card': 4, 'interest_rate': 3, 'num_of_loan': 4, 'type_of_loan': 'Auto Loan, Credit-Builder Loan, Personal Loan, and Home Equity Loan', 'delay_from_due_date': 8, 'num_of_delayed_payment': 4, 'changed_credit_limit': 9.27, 'num_credit_inquiries': 4, 'credit_mix': 'Good', 'outstanding_debt': 809.98, 'credit_utilization_ratio': 27.2622587105202, 'credit_history_age': '22 Years and 6 Months', 'payment_of_min_amount': 'No', 'total_EMI_per_month': 49.5749492148942, 'amount_invested_monthly': 62.4301723311953, 'payment_behaviour': 'High_spent_Medium_value_payments', 'monthly_balance': 340.479211787244, 'credit_score': 'Good'},
    {'user_id': 'S001', 'month': 'Jul', 'user_name': 'Su', 'age': 25, 'SSN': '821-00-0265', 'occupation': 'Scientist', 'annual_income': 19114.12, 'monthly_inhand_salary': 1824.84333333333, 'num_bank_accounts': 3, 'num_credit_card': 4, 'interest_rate': 3, 'num_of_loan': 4, 'type_of_loan': 'Auto Loan, Credit-Builder Loan, Personal Loan, and Home Equity Loan', 'delay_from_due_date': 3, 'num_of_delayed_payment': 7, 'changed_credit_limit': 11.27, 'num_credit_inquiries': 4, 'credit_mix': 'Good', 'outstanding_debt': 809.98, 'credit_utilization_ratio': 22.5375930317838, 'credit_history_age': '22 Years and 7 Months', 'payment_of_min_amount': 'No', 'total_EMI_per_month': 49.5749492148942, 'amount_invested_monthly': 178.344067412235, 'payment_behaviour': 'Low_spent_Small_value_payments', 'monthly_balance': 244.565316706204, 'credit_score': 'Good'},
    {'user_id': 'S001', 'month': 'Aug', 'user_name': 'Su', 'age': 25, 'SSN': '821-00-0265', 'occupation': 'Scientist', 'annual_income': 19114.12, 'monthly_inhand_salary': 1824.84333333333, 'num_bank_accounts': 3, 'num_credit_card': 4, 'interest_rate': 3, 'num_of_loan': 4, 'type_of_loan': 'Auto Loan, Credit-Builder Loan, Personal Loan, and Home Equity Loan', 'delay_from_due_date': 3, 'num_of_delayed_payment': 7, 'changed_credit_limit': 11.27, 'num_credit_inquiries': 4, 'credit_mix': 'Good', 'outstanding_debt': 809.98, 'credit_utilization_ratio': 23.9337948019655, 'credit_history_age': '22 Years and 8 Months', 'payment_of_min_amount': 'No', 'total_EMI_per_month': 49.5749492148942, 'amount_invested_monthly': 24.7852165090521, 'payment_behaviour': 'High_spent_Medium_value_payments', 'monthly_balance': 358.124167609387, 'credit_score': 'Good'},
]
data1 = pd.DataFrame(financial_data)

annual_amount = data1.groupby('user_id')['monthly_inhand_salary'].sum()
total_debt = data1.groupby('user_id')['outstanding_debt'].sum()
net_profit = annual_amount - total_debt
profit_margin = (net_profit / annual_amount) * 100
total_investment = data1.groupby('user_id')['amount_invested_monthly'].sum()

def KPI_metrics(title, value):
    st.markdown(f"""
        <div class = "metrics" style = "background-color: green; padding: 10px 20px; border-radius: 10px; text-align: center; margin-bottom: 10px;">
            <h4>{title}</h4>
            <p style = "font-size: 25px; margin: 0;">{value}</p>
        </div>
        """, unsafe_allow_html = True)

st.header('Key Metrics')

col1, col2, col3 = st.columns(3)
with col1: 
    KPI_metrics('Total Income', '$' + f"{annual_amount.sum():.2f}")
with col2:
    KPI_metrics('Total Debt', '$' + f"{total_debt.sum():.2f}")
with col3:
    KPI_metrics('Net Profit', '$' + f"{net_profit.sum():.2f}")

col4, col5 = st.columns(2)
with col4:
    KPI_metrics('Profit Margin', str(round(profit_margin.sum(), 2)) + '%')
with col5:
    KPI_metrics('Total Investment', '$' + f"{total_investment.sum():.2f}")

#data2 = pd.read_csv('data\sample_spending_data.csv', low_memory = False)
spending_data = [
    {'user_id': 'S001', 'month': 'Jan', 'monthly_income': 748, 'financial_aid': 494, 'tuition': 4789, 'housing': 447, 'food': 353, 'transportation': 164, 'books_supplies': 201, 'entertainment': 60, 'personal_care': 43, 'technology': 99, 'health_wellness': 93, 'miscellaneous': 172},
    {'user_id': 'S001', 'month': 'Feb', 'monthly_income': 506, 'financial_aid': 931, 'tuition': 4087, 'housing': 998, 'food': 251, 'transportation': 175, 'books_supplies': 80, 'entertainment': 82, 'personal_care': 82, 'technology': 76, 'health_wellness': 152, 'miscellaneous': 56},
    {'user_id': 'S001', 'month': 'Mar', 'monthly_income': 1033, 'financial_aid': 64, 'tuition': 4249, 'housing': 517, 'food': 104, 'transportation': 64, 'books_supplies': 259, 'entertainment': 131, 'personal_care': 66, 'technology': 234, 'health_wellness': 63, 'miscellaneous': 104},
    {'user_id': 'S001', 'month': 'Apr', 'monthly_income': 1309, 'financial_aid': 840, 'tuition': 5575, 'housing': 923, 'food': 257, 'transportation': 115, 'books_supplies': 263, 'entertainment': 78, 'personal_care': 20, 'technology': 236, 'health_wellness': 39, 'miscellaneous': 78},
    {'user_id': 'S001', 'month': 'May', 'monthly_income': 843, 'financial_aid': 4, 'tuition': 4906, 'housing': 869, 'food': 226, 'transportation': 196, 'books_supplies': 66, 'entertainment': 82, 'personal_care': 98, 'technology': 289, 'health_wellness': 58, 'miscellaneous': 148},
    {'user_id': 'S001', 'month': 'Jun', 'monthly_income': 1205, 'financial_aid': 837, 'tuition': 3014, 'housing': 593, 'food': 183, 'transportation': 142, 'books_supplies': 112, 'entertainment': 77, 'personal_care': 59, 'technology': 209, 'health_wellness': 145, 'miscellaneous': 78},
    {'user_id': 'S001', 'month': 'Jul', 'monthly_income': 1004, 'financial_aid': 465, 'tuition': 5665, 'housing': 835, 'food': 126, 'transportation': 179, 'books_supplies': 297, 'entertainment': 23, 'personal_care': 52, 'technology': 238, 'health_wellness': 79, 'miscellaneous': 104},
    {'user_id': 'S001', 'month': 'Aug', 'monthly_income': 663, 'financial_aid': 798, 'tuition': 5418, 'housing': 420, 'food': 389, 'transportation': 97, 'books_supplies': 282, 'entertainment': 144, 'personal_care': 84, 'technology': 149, 'health_wellness': 123, 'miscellaneous': 167},
    {'user_id': 'S001', 'month': 'Sep', 'monthly_income': 1126, 'financial_aid': 771, 'tuition': 3126, 'housing': 823, 'food': 374, 'transportation': 125, 'books_supplies': 215, 'entertainment': 90, 'personal_care': 77, 'technology': 242, 'health_wellness': 112, 'miscellaneous': 99},
    {'user_id': 'S001', 'month': 'Oct', 'monthly_income': 1149, 'financial_aid': 387, 'tuition': 5744, 'housing': 849, 'food': 301, 'transportation': 112, 'books_supplies': 162, 'entertainment': 141, 'personal_care': 74, 'technology': 89, 'health_wellness': 107, 'miscellaneous': 108},
    {'user_id': 'S001', 'month': 'Nov', 'monthly_income': 558, 'financial_aid': 830, 'tuition': 4642, 'housing': 895, 'food': 349, 'transportation': 89, 'books_supplies': 273, 'entertainment': 45, 'personal_care': 83, 'technology': 79, 'health_wellness': 122, 'miscellaneous': 143},
    {'user_id': 'S001', 'month': 'Dec', 'monthly_income': 507, 'financial_aid': 474, 'tuition': 4996, 'housing': 750, 'food': 181, 'transportation': 107, 'books_supplies': 156, 'entertainment': 79, 'personal_care': 27, 'technology': 122, 'health_wellness': 39, 'miscellaneous': 87},
]
data2 = pd.DataFrame(spending_data)

#Comparison Income vs Expenses (Section 2)
def comparison_income_spending(data2):
    fig, ax = plt.subplots()
    spending_monthly_amount = data2['transportation'] + data2['food'] + data2['books_supplies'] + data2['entertainment'] + data2['personal_care'] + data2['technology'] + data2['health_wellness'] + data2['miscellaneous']
    income_monthly_amount = data2['monthly_income'] + data2['financial_aid']
    ax.plot(data2['month'], income_monthly_amount, label = 'Income', color='blue')
    ax.plot(data2['month'], spending_monthly_amount, label = 'Expenses', color = 'red')
    ax.legend(loc='upper right')
    st.pyplot(fig)

st.header('Income vs Expenses')
comparison_income_spending(data2)

#Expenses Breakdown (Section 2)
def expenses_breakdown(data2):
    all_expenses = data2.groupby('month')[['transportation', 'food', 'books_supplies', 'entertainment', 'personal_care', 'technology', 'health_wellness', 'miscellaneous']].sum() 
    all_expenses = all_expenses.reindex(pd.CategoricalIndex(all_expenses.index, categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ordered=True))
    fig, ax = plt.subplots(figsize = (10, 6))
    all_expenses.plot(kind = 'bar', stacked = True, ax = ax) 
    ax.legend(loc = 'upper center', bbox_to_anchor = (0.5, -0.1), fancybox = True, shadow = True, ncol = 5)
    ax.set_xlabel('')
    st.pyplot(fig)

st.header('Expenses Breakdown')
expenses_breakdown(data2)

#Financial Goals (Section 3)
goals_data = [
    {'Goal': 'Buy a car', 'Target Amount': 250000, 'Current Saved Amount': 55000, 'Deadline': '2024-12-31', 'Category': 'Short-Term', 'Status': 'Ongoing'},
    {'Goal': 'Travel to Niagara falls', 'Target Amount': 100000, 'Current Saved Amount': 20000, 'Deadline': '2025-04-30', 'Category': 'Mid-Term', 'Status': 'Ongoing'},
    {'Goal': 'Buy a house', 'Target Amount': 500000, 'Current Saved Amount': 30000, 'Deadline': '2025-12-31', 'Category': 'Long-Term', 'Status': 'Ongoing'}
]
data3 = pd.DataFrame(goals_data)

st.subheader('Financial Goals')
st.write(data3)

def goals_progress(data3):
    fig, axes = plt.subplots(1, 3, figsize = (10, 6))
    for idx, row in data3.iterrows():
        progress = row['Current Saved Amount'] / row['Target Amount'] * 100
        ax = axes[idx]
        ax.set_aspect('equal')
        ax.pie([progress, 100 - progress], labels = ['Progress', 'Remaining'], autopct = '%1.1f%%', colors = ['green', '#d3d3d3'])
        ax.set_title(row['Goal'])
    st.pyplot(fig)

goals_progress(data3)