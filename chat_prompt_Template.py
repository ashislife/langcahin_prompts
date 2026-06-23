from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

prompt = ChatPromptTemplate([
    ("system", "You are a helpful assistant specialized in {domain}."),
    ("human", "Explain {topic}")
])

messages = prompt.format_messages(
    domain="AI",
    topic="LangChain"
)

result = model.invoke(messages)

print(result.content)