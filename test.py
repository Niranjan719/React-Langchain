from charset_normalizer import VERSION
from langchain.agents import initialize_agent, AgentType,tool, AgentExecutor
# from langchain_agents import initialize_agent, AgentType,tool, AgentExecutor
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv



load_dotenv()

@tool
def get_text_length(text: str) -> int:
    """Returns the length of a text by characters"""
    print(f"get_text_length enter with text = {text}")
    text = text.strip("'\n").strip('"')

    return len(text)

if __name__ == "__main__":
    llm = ChatOpenAI()
    agent_executor : AgentExecutor = initialize_agent(tools=[get_text_length],llm=llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True,)
    res = agent_executor.invoke({'input':'What is the length of the text Dog ?'})
    print(res)