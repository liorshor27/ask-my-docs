# Ask My Docs 📚

A Retrieval-Augmented Generation (RAG) system that answers questions
about your own documents, exposed through a REST API.

> Work in progress — built step by step as a learning project.

## How RAG Works

Large Language Models don't know private or recent information.
RAG solves this by retrieving relevant text from a dedicated database
and passing it to the model as context.

1. **Chunking** — split source documents into smaller pieces
2. **Embeddings** — convert each chunk into a vector that represents its meaning
3. **Vector Database** — store the vectors in ChromaDB
4. **Retrieval** — embed the user's question and find the closest chunks
5. **Generation** — send the question + retrieved chunks to an LLM

✍️ We have to use the same embedding model because each model creates its own unique vector space. 
If we use one model to embed the data and a different one for the user's question, it's like comparing 
coordinates from two completely different maps—the database simply won't find the connection.

## Tech Stack

- **Python**
- **ChromaDB** — local vector database
- **all-MiniLM-L6-v2** — default embedding model
- *(planned)* **FastAPI** — REST API
- *(planned)* **Gemini API** — LLM for answer generation

## Getting Started

```bash
git clone https://github.com/<your-username>/ask-my-docs.git
cd ask-my-docs
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python 01_chroma_playground.py
```

## Roadmap

- [x] Project setup
- [x] ChromaDB playground — semantic search basics
- [ ] Document ingestion & chunking
- [ ] Answer generation with an LLM
- [ ] REST API with FastAPI
- [ ] Tests & documentation
 
## What I Learned
- **Semantic search finds meaning, not keywords:** I asked *"Is there a recipe for banana muffin?"* and the top result was *"I made a chocolate-flavored cake"*, even though the two sentences share no words. The embedding model placed them close together in vector space because both are about sweet baked goods.
- **`add` vs. `upsert`:** Running `add` again with existing IDs didn't raise an error, it silently ignored them (`count()` stayed at 6). This means updated documents would keep their old content. `upsert` solves this by inserting new IDs and updating existing ones.
