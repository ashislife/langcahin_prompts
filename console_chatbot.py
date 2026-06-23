# Proble with memory (not remember in previous conversation) 

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

while True:
    user_input=input("You:")
    if user_input=='exit':
        break
    result=model.invoke(user_input)
    print("AI: ",result.content)


