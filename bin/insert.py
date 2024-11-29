from src.models import create_embedding_model
from src.vector import parent_insert_documents
from src.langchain import load_code_folder_documents 

embedding = create_embedding_model()
documents = load_code_folder_documents(
  path="athennaio/docs/docs",
  glob="**/*",
  suffixes=[".mdx"],
  exclude=["_category.json"]
)

parent_insert_documents(
  embedding=embedding, 
  documents=documents,
  chunk_size=2000,
  chunk_overlap=100
)
