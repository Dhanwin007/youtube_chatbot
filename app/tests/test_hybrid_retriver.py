
from app.retrivers.hybrid_retriver import hybrid_search


query = "wedding reception DJ"

results = hybrid_search(query, k=5)

print("Retrieved", len(results), "documents")

for index, document in enumerate(results, start=1):

    print(f"\n--- Result {index} ---")
    print("Content:", document.page_content)
    print("Start:", document.metadata.get("start"))
    print("End:", document.metadata.get("end"))
    print("Chunk:", document.metadata.get("chunk_index"))
