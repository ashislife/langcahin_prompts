# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# import streamlit as st
# from langchain_core.prompts import PromptTemplate,load_prompt

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="Qwen/Qwen2.5-0.5B-Instruct",
#     task="text-generation"
# )

# model = ChatHuggingFace(llm=llm)
# messages=[
#     SystemMessage(content="You are a helpful assistant ."),
#     HumanMessage(content="Tell me about Langchain"),
# ]
# result=model.invoke(messages)

# messages.append(AIMessage(content=result.content))
# print(messages)

# ----------------------------------<>----------------------------------------------------------------------

# That show in result which one is human or AI or System message 


from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-5.2",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

chat_history = [SystemMessage(content="You are a helpful assistant.")   ]

# conatin a history of chat 
while True:
    user_input=input("You:")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)
print("Chat History: ", chat_history)