from src.vector import parent_ask
from src.models import create_llm_model, create_embedding_model

llm = create_llm_model()
embedding = create_embedding_model()

chunk_size = 2000
chunk_overlap = 100

result = parent_ask(
  llm=llm,
  embedding=embedding,
  chunk_size=chunk_size,
  chunk_overlap=chunk_overlap,
  question="How I could change the routes directory in Athenna Framework?"
)

print(result)
