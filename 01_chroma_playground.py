import chromadb

# 1. Create a client that saves data to the "chroma_db" folder
client = chromadb.PersistentClient(path="chroma_db")

# 2. Get (or create) a collection - like a "table" of vectors
collection = client.get_or_create_collection(name="playground")

# 3. Upsert sentences (insert new ids, update existing ones)
collection.upsert(
    ids=["cook1", "cook2", "sport1", "sport2", "prog1", "prog2"],
    documents=[
        "I grilled a steak on the barbecue.",
        "I made a chocolate-flavored cake.",
        "Barcelona defeated Real Madrid 2–1.",
        "Deni Avdija made it to the NBA.",
        "Today I finished building my first app.",
        "Never ending recursion.",
    ],
)

# 4. Ask a question that shares NO words with the matching sentence
results = collection.query(
    query_texts=["Who won the football match?"],
    n_results=6,
)

print(results.keys())
for doc, dist in zip(results["documents"][0], results["distances"][0]):
    print(f"{dist:.3f}  |  {doc}")
print(collection.count())