from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate #Importing PromptTemplate from langchain core to create a prompt template, we will use this prompt template to create a prompt for the model, we can use this prompt template to create a prompt for any model, we just need to change the input variables in the prompt template.

load_dotenv()

from langchain_mistralai import ChatMistralAI


model=ChatMistralAI(model="mistral-small-2506")

prompt= ChatPromptTemplate.from_messages([
    ("system", #This is a system message where we will provide the instructions to the model on how to extract information from the paragraph, we will also provide a template for the output format, we will use this template to extract information from the paragraph and provide a summary of the paragraph.
"""You are an expert information extraction assistant.

Your task is to carefully read the paragraph and extract the most useful information about the movie mentioned.

Instructions:

1. Identify key factual information present in the paragraph.
2. Do not invent information that is not mentioned.
3. If any field is missing in the paragraph, write "Not specified".
4. After extracting the information, write a short summary in 2–3 sentences.

Paragraph:
{paragraph}

Provide the output in the following format:

Movie Name:
Director:
Genre:
Main Cast:
Story Premise:
Setting/Location:
Key Themes:
Central Conflict:

Quick Summary:
(2–3 sentence concise summary of the paragraph)
"""),
    
("human", #This is a human message, we will use this message to provide the paragraph to the model, we will replace the {paragraph} placeholder with the actual paragraph we want to extract information from.

"""Extract information from the paragraph:
{paragraph}""") #{paragraph} is a placeholder  where I will put the paragraph
])

paragraph= input("Enter a paragraph about a movie: ")

final_prompt= prompt.invoke(
    {"paragraph": paragraph}
)

response= model.invoke(final_prompt)

print(response.content)