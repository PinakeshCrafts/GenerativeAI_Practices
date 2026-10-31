from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7,
)

response = llm.invoke("Explain what a virtual environment is in 2 lines.")
print(response.content)