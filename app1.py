import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data
np.random.seed(42)
dates = pd.date_range(start='2024-01-01', periods=30)
income = np.random.randint(0, 3000, size=(30,))
expenses = np.random.randint(100, 1000, size=(30,))

# DataFrame
df = pd.DataFrame({'Date': dates, 'Income': income, 'Expenses': expenses})

# Calculate Net Income and other financial metrics
df['Net Income'] = df['Income'] - df['Expenses']
total_spending = df['Expenses'].sum()
total_income = df['Income'].sum()
net_income = df['Net Income'].sum()
budget = 50000  # Example budget
net_worth = 150000  # Example net worth
budget_used_percent = (total_spending / budget) * 100

# Set up Streamlit layout
st.set_page_config(layout="centered")

# Line chart for income and expenses
st.title("Financial Dashboard")
st.subheader("Monthly Income and Spendings")

fig, ax = plt.subplots()
ax.plot(df['Date'], df['Expenses'], label='Spendings', color='red')
ax.plot(df['Date'], df['Income'], label='Income', color='blue')
ax.set_xlabel("Date")
ax.set_ylabel("Amount ($)")
ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2)
plt.xticks(pd.date_range(start='2024-01-01', periods=5, freq='W'))
st.pyplot(fig)

# Financial Metrics

st.subheader("Financial Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Spendings", f"${total_spending}")
    st.write("Amount spent so far this month")

with col2:
    st.metric("Net Income", f"${net_income}")
    st.write("This month")

with col3:
    st.metric("Budget", f"{budget_used_percent:.2f}%")
    st.write("Percentage of budget used this month")

with col4:
    st.metric("Net Worth", f"${net_worth}")
    st.write("This month")

# Goals Section with Donut Charts
st.subheader("Short Term Goals")
goal_data = {
    "Goal 1": [75, 25],  # 75% completed
    "Goal 2": [50, 50],  # 50% completed
    "Goal 3": [30, 70],  # 30% completed
}

cols = st.columns(3)
for idx, (goal, values) in enumerate(goal_data.items()):
    with cols[idx]:
        st.write(f"**{goal}**")
        fig, ax = plt.subplots()
        wedges, texts = ax.pie(values, startangle=90, colors=['#1f77b4', '#d3d3d3'], wedgeprops=dict(width=0.3))
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)