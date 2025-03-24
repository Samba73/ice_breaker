import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile

load_dotenv()

if __name__ == "__main__":

    summary_template = """
        Given the Linkedin information {information} about a person from I want you to create:
        1. a short summary
        2. 2 interesting facts about them
"""
summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

# llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
llm = ChatOllama(model="llama3.2")

chain = summary_prompt_template | llm | StrOutputParser()

linkedin_data = scrape_linkedin_profile(
                                        linkedin_profile_url="https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json",
                                        mock=True
                                        )

res = chain.invoke(input={"information": linkedin_data})

print(res)