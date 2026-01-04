from langchain_cerebras import ChatCerebras
from dotenv import load_dotenv
from langgraph.graph import StateGraph ,START,END
from langchain_core.prompts import PromptTemplate
from typing import TypedDict
load_dotenv()


model=ChatCerebras(model='qwen-3-32b')

template="""you are a teacher who explain the history topic the student give you the {topic} and also the student tell the topic difficulty level {level} and student also tell you in how many words you nned tom explain the words{number_of_words}"""


prompt=PromptTemplate(
    template=template,
    input_variables=['topic','level','number_of_words']
)

final_prompt=prompt.invoke({'topic':'history of shivaji maharaj','level':'easy','number_of_words':'100'})

result=model.invoke(final_prompt)
print(result.content)
