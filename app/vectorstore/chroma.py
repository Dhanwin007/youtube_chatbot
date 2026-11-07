
import os

import chromadb
from dotenv import load_dotenv


load_dotenv()

COLLECTION_NAME = "Yt_chatbot"


def get_chroma_collection():

    client = chromadb.CloudClient(
        api_key=os.getenv("CHROMA_API_KEY"),
        tenant=os.getenv("CHROMA_TENANT"),
        database=os.getenv("CHROMA_DATABASE")
    )

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=None
    )

    return client, collection


if __name__ == "__main__":

    client, collection = get_chroma_collection()

    print("Connected to Chroma Cloud!")
    print("Collection:", collection.name)
    print("Existing records:", collection.count())
