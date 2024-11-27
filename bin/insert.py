from src.vector import insert_chunks
from langchain_text_splitters import Language
from src.models import create_embedding_model
from src.langchain import load_code_folder_chunks 

chunks = load_code_folder_chunks(
    path="athennaio/docs/docs",
    glob="**/*",
    suffixes=[".mdx"],
    exclude=["_category.json"],
    chunk_size=2000,
    chunk_overlap=100
  )

insert_chunks(
  embedding=create_embedding_model(),
  chunks=chunks
)
