from langchain_cerebras import ChatCerebras
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

model=ChatCerebras(model='qwen-3-32b')

code=input("put your code here:")
prompt=ChatPromptTemplate(
    SystemMessage(content='you are a coder assistant who have the good coding skills when user ask the anything about the coding or suppose user say plase debug this code then debug the code and give proper explanation of the code'),
    HumanMessage(content='explan me this code{code}')
)

final_prompt=prompt.invoke({'code':code})

result=model.invoke(final_prompt)
print(result)
