import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv('..\Sample Datasets\sample_financial_data.csv', low_memory = False)

annual_amount = data1.groupby('Customer_ID')['Monthly_Inhand_Salary'].sum()
total_debt = data1.groupby('Customer_ID')['Outstanding_Debt'].sum()
net_profit = annual_amount - total_debt
profit_margin = (net_profit / annual_amount) * 100
total_investment = data1.groupby('Customer_ID')['Amount_invested_monthly'].sum()

st.title('Financial Health Dashboard')

def KPI_metrics(title, value, delta = None):
    st.markdown(f"""
        <div class = "metrics" style = "background-color: green; padding: 10px 20px; border-radius: 10px; text-align: center; margin-bottom: 10px;">
            <h3>{title}</h3>
            <p style = "font-size: 25px; margin: 0;">{value}</p>
        </div>
        """, unsafe_allow_html = True)

data1['ID'] = data1['ID'].astype('int64')

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

data2 = pd.read_csv('..\Sample Datasets\sample_spending_data.csv', low_memory = False)

def income_monthly(data2):
    fig, ax = plt.subplots()
    ax.plot(data2['month'], data2['monthly_income'], label = 'Income', color='blue')
    #ax.set_title('Monthly Income')
    ax.set_ylabel('Income')
    st.pyplot(fig)

st.header('Monthly Income')
income_monthly(data2)

def spending_monthly(data2):
    fig, ax = plt.subplots()
    spending_monthly_amount = data2['tuition'] + data2['housing'] + data2['transportation'] + data2['food'] + data2['books_supplies'] + data2['entertainment'] + data2['personal_care'] + data2['technology'] + data2['health_wellness'] + data2['miscellaneous']
    ax.plot(data2['month'], spending_monthly_amount, label = 'Income', color = 'red')
    #ax.set_title('Monthly Expenses')
    ax.set_ylabel('Expenses')
    st.pyplot(fig)

st.header('Monthly Spending')
spending_monthly(data2)

def comparison_income_spending(data2):
    fig, ax = plt.subplots()
    spending_monthly_amount = data2['transportation'] + data2['food'] + data2['books_supplies'] + data2['entertainment'] + data2['personal_care'] + data2['technology'] + data2['health_wellness'] + data2['miscellaneous']
    income_monthly_amount = data2['monthly_income'] + data2['financial_aid']
    ax.plot(data2['month'], income_monthly_amount, label = 'Income', color='blue')
    ax.plot(data2['month'], spending_monthly_amount, label = 'Expenses', color = 'red')
    #ax.set_title('Income vs Expenses')
    ax.set_ylabel('Amount')
    ax.legend(loc='upper right')
    st.pyplot(fig)

st.header('Income vs Expenses')
comparison_income_spending(data2)

def expenses_breakdown(data2):
    all_expenses = data2.groupby('month')[['transportation', 'food', 'books_supplies', 'entertainment', 'personal_care', 'technology', 'health_wellness', 'miscellaneous']].sum() 
    all_expenses = all_expenses.reindex(pd.CategoricalIndex(all_expenses.index, categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ordered=True))

    fig, ax = plt.subplots(figsize = (10, 6))
    all_expenses.plot(kind = 'bar', stacked = True, ax = ax) 
    ax.legend(loc = 'upper center', bbox_to_anchor = (0.5, -0.09), fancybox = True, shadow = True, ncol = 5)
    ax.set_xlabel('')
    st.pyplot(fig)

st.header('Expenses Breakdown')
expenses_breakdown(data2)

goals_data = [
    {'Goal': 'Buy a car', 'Target Amount': 250000, 'Current Saved Amount': 55000, 'Deadline': '2024-12-31', 'Category': 'Short-Term', 'Status': 'Ongoing'},
    {'Goal': 'Travel to Niagara falls', 'Target Amount': 100000, 'Current Saved Amount': 20000, 'Deadline': '2025-04-30', 'Category': 'Mid-Term', 'Status': 'Ongoing'},
    {'Goal': 'Buy a house', 'Target Amount': 500000, 'Current Saved Amount': 30000, 'Deadline': '2025-12-31', 'Category': 'Long-Term', 'Status': 'Ongoing'}
]

data3 = pd.DataFrame(goals_data)

st.subheader('FinancialGoals')
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