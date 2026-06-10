from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model = 'gpt-4',temperature=0,max_completion_tokens = 10) # temperature is a parameter that controls the randomness of a language model's output.Lower values(0.0 - 0.3:- more determinstic and predictable, higher values(0.7 - 1.5 : more random,creative and diverse.) max completion tokens roughly khe skte hai ki yeh words hote hai.
res = model.invoke("what is the capital of india")
print(res.content)