# RAG Athenna Framework 🤖

> Implementation of RAG techniques to teach GPT about Athenna Framework so he could answer any question that the developers might have.

> [!TIP]
> For more details about this repository check my blog post: [Using GPT with RAG to answer questions about Athenna](https://lenonsec.com/articles/01JDSEG9RA8HHSV7VBG2GXW9V4).

## Tools

The project uses the following tools to work:

- [LangChain](https://python.langchain.com/docs/introduction/)
- [Chroma as Vector DB](https://www.trychroma.com/)
- [GPT 3.5 Turbo as LLM](https://platform.openai.com/docs/models#gpt-3-5-turbo)
- [ADA 002 for Text Embedding](https://platform.openai.com/docs/models#embeddings)

## Running

To run the project first create a new Python environment and activate it. I'm using [Anaconda](https://www.anaconda.com/) for setting the python version that pipenv should use to set up the environment. The command bellow will automatically setup the environment with conda and pipenv:

```shell
make env
```

Now install all the project dependencies:

```shell
make install-all
```

Clone the repositories you want the model to code review:

```shell
make clone
```

### Base RAG Architecture

Insert the file chunks in Chroma database by running:

```shell
make base-insert
```

Ask something by running the following:

```shell
make base-ask
```

You can change your question inside `bin/base/ask.py`.

### Parent RAG Architecture

Insert the file chunks in Chroma database by running:

```shell
make parent-insert
```

Ask something by running the following:

```shell
make parent-ask
```

You can change your question inside `bin/parent/ask.py`.
