from collections.abc import Sequence
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser 
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

def load_pdf_chunks(file_name: str, chunk_size: int, chunk_overlap: int):
  loader = PyPDFLoader(f"storage/{file_name}.pdf", extract_images=False)
  pages = loader.load_and_split()

  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    length_function=len,
    add_start_index=True
  )

  return text_splitter.split_documents(pages)

def load_code_folder_chunks(path: str, glob: str, suffixes: Sequence[str], chunk_size: int, chunk_overlap: int, exclude: Sequence[str] = None, language: Language = None):
  loader = GenericLoader.from_filesystem(
    f"storage/repositories/{path}",
    glob=glob,
    suffixes=suffixes,
    exclude=exclude,
    parser=LanguageParser(language=language, parser_threshold=500)
  )

  documents = loader.load()

  splitter = None

  if language is None:
    splitter = RecursiveCharacterTextSplitter(
      chunk_size=chunk_size,
      chunk_overlap=chunk_overlap,
      length_function=len,
      add_start_index=True
    )
  else:
    splitter = RecursiveCharacterTextSplitter.from_language(
      language=language,
      chunk_size=chunk_size,
      chunk_overlap=chunk_overlap,
      length_function=len,
      add_start_index=True
    )
    

  return splitter.split_documents(documents)
