
from app.retrivers.semantic_retriver import retrieve_documents


query = "Explain everything discussed about the wedding."

documents = retrieve_documents(
    query=query,
    k=5,
    fetch_k=20,
    lambda_mult=0.5
)

print(f"Retrieved {len(documents)} unique documents\n")

for index, document in enumerate(documents, start=1):

    print(f"--- Result {index} ---")
    print("Content:", document.page_content)
    print("Start:", document.metadata["start"])
    print("End:", document.metadata["end"])
    print("Chunk:", document.metadata["chunk_index"])
    print()
