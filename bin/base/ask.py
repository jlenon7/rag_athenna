from src.vector import base_ask 
from src.models import create_llm_model, create_embedding_model

llm = create_llm_model()
embedding = create_embedding_model()

result, context = base_ask(
  llm=llm, 
  embedding=embedding, 
  question="How I could change the routes directory in Athenna Framework?"
)

print(result["answer"])
