from app.retrivers.keyword_retriver import keyword_search

query = "DJ music wedding"

documents = keyword_search(query=query, k=5)

print(f"Retrieved {len(documents)} documents\n")

for index, document in enumerate(documents, start=1):

    print(f"--- Result {index} ---")
    print("Content:", document.page_content)
    print("Metadata:", document.metadata)
    print()