import os


from dotenv import load_dotenv
load_dotenv()

from langchain_openai import AzureChatOpenAI

llm = AzureChatOpenAI(deployment_name=os.getenv("AZURE_DEP_NAME"),
                         openai_api_version=os.getenv("AZURE_VERSION"),
                          openai_api_key=os.getenv("AZURE_KEY"),
                           azure_endpoint=os.getenv("AZURE_ENDPOINT"))


