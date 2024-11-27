from os import environ
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

def create_llm_model():
  return ChatOpenAI(
    max_tokens=200,
    model_name="gpt-3.5-turbo",
    api_key=environ.get("OPENAI_API_KEY")
  )

def create_embedding_model():
  return OpenAIEmbeddings(
    api_key=environ.get("OPENAI_API_KEY"),
    disallowed_special=()
  )
