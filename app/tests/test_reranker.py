from app.retrivers.reranker import rerank_documents
from app.retrivers.hybrid_retriver import hybrid_search


query = "wedding reception DJ"

# Retrieve candidates using existing hybrid retrieval
documents = hybrid_search(query, k=10)

print("\nBEFORE RERANKING")
for document in documents:
    print(
        document.metadata.get("document_id"),
        document.metadata.get("chunk_index"),
        document.metadata.get("start")
    )

# Rerank candidates using Cohere
reranked_documents = rerank_documents(
    query=query,
    documents=documents,
    top_n=5
)

print("\nAFTER RERANKING")

for document in reranked_documents:
    print(
        "Score:", document.metadata.get("relevance_score"),
        "| Chunk:", document.metadata.get("chunk_index"),
        "| Timestamp:", document.metadata.get("start")
    )