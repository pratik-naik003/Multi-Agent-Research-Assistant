from langchain_cerebras import ChatCerebras
from dotenv import load_dotenv
from typing import TypedDict

from regex import F
load_dotenv()

model=ChatCerebras(model="qwen-3-32b")

class check(TypedDict):
   summary_of_paper_in_50_words:str
   imp_points:str

structure_output=model.with_structured_output(check)

paper=input("enter the paper text:")

result=structure_output.invoke(paper)
print("summary of paper:")
print(result['summary_of_paper_in_50_words']) 

print("Important Points :")
print(result['imp_points'])


    
