import os
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.utilities.polygon import PolygonAPIWrapper
from langchain_community.tools import PolygonLastQuote, PolygonTickerNews, PolygonFinancials, PolygonAggregates
from langchain_core.runnables import RunnablePassthrough
from langchain_core.agents import AgentFinish
from langgraph.graph import END, Graph
from dotenv import load_dotenv

load_dotenv()

prompt = hub.pull("hwchase17/openai-functions-agent")
llm = ChatOpenAI(model="gpt-3.5-turbo")

polygon = PolygonAPIWrapper()
tools = [
    PolygonLastQuote(api_wrapper=polygon),
    PolygonTickerNews(api_wrapper=polygon),
    PolygonFinancials(api_wrapper=polygon),
    PolygonAggregates(api_wrapper=polygon),
]

agent_runnable = create_openai_functions_agent(llm, tools, prompt=prompt, verbose=True)
agent = RunnablePassthrough.assign(agent_outcome = agent_runnable)

def execute_tools(data):
    agent_action = data.pop('agent_outcome')
    tool_to_use = {t.name: t for t in tools}[agent_action.tool]
    observation = tool_to_use.invoke(agent_action.tool_input)
    data['intermediate_steps'].append((agent_action, observation))
    return data

def should_continue(data):
    if isinstance(data['agent_outcome'], AgentFinish):
        return "exit"
    else:
        return "continue"

workflow = Graph()
workflow.add_node("agent", agent)
workflow.add_node("tools", execute_tools)
workflow.set_entry_point("agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": 'tools',
        "exit": END
    }
)

workflow.add_edge('tools', 'agent')
chain = workflow.compile()
result = chain.invoke({
    "input": "What has been ABNB's daily closing price between May 1, 2024 and May 21, 2024?", "intermediate_steps": []
})
output = result['agent_outcome'].return_values['output']
print(output)