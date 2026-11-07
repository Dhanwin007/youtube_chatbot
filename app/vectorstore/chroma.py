import os
import chromadb

from dotenv import load_dotenv
from langchain_chroma import Chroma

from app.vectorstore.embeddings import get_embedding_model


load_dotenv()

COLLECTION_NAME = "Yt_chatbot"


def get_vector_store():

    # client = chromadb.CloudClient(
    #     api_key=os.getenv("CHROMA_API_KEY"),
    #     tenant=os.getenv("CHROMA_TENANT"),
    #     database=os.getenv("CHROMA_DATABASE")
    # )

    embeddings = get_embedding_model()

    # vector_store = Chroma(
    #     client=client,
    #     collection_name=COLLECTION_NAME,
    #     embedding_function=embeddings,
    #     create_collection_if_not_exists=True
    # )
    vector_store = Chroma(
    collection_name=COLLECTION_NAME,
    embedding_function=embeddings,
    chroma_cloud_api_key=os.getenv("CHROMA_API_KEY"),
    tenant=os.getenv("CHROMA_TENANT"),
    database=os.getenv("CHROMA_DATABASE"),
)

    return vector_store


if __name__ == "__main__":

    vector_store = get_vector_store()

    print("LangChain Chroma connected!")
    print("Collection:", COLLECTION_NAME)
    print("Existing records:", vector_store._collection.count())