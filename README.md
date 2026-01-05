This project is in Building phase

first we create the schem using the class in that class basicaly we added the what kind of structured output we needed and then accrding  

there are two ways to get the structured output one is using typedict and second is using pydantic
1)using typeddict

steps for structured output
1)import the model 
2)create one schemas basically using the typed dict and pydantic by using base class 
3)we call the structured output function by passing the class  that we create at the time of defined schema 
4)then we design the prompt 

2)using pydantic
steps to create the structured the output using the pydantic 
1)import model
2)create pydantic class uing the basemodel class 

#output parsers
1)string ouput parser 
the string output parser is type of parser which eenforce the LLm to convert than output into the  string 
2)json outpt parser
this is this type of output parser is used to enforce the LLm to convert the input the JSON format

3)pydantic outputparser
this parser convert the input into the pydantic object 

4)structured output parser
this is used to convert the input into json structured output




