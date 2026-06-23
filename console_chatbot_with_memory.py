# contain a history of conversation but not remember in previous conversation.
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

chat_history = []

# conatin a history of chat 
while True:
    user_input=input("You:")
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ",result.content)
print("Chat History: ", chat_history)