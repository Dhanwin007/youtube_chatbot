
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_classic.retrievers.multi_query import MultiQueryRetriever

from app.vectorstore.neon import get_vector_store


load_dotenv()


def retrieve_documents(
    query,
    k=5,
    fetch_k=20,
    lambda_mult=0.5
):
    """
    Retrieve relevant and diverse transcript chunks
    using MMR + MultiQueryRetriever.
    """

    # 1. Initialize vector store
    vector_store = get_vector_store()

    # 2. Create MMR retriever
    mmr_retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": k,
            "fetch_k": fetch_k,
            "lambda_mult": lambda_mult
        }
    )

    # 3. Initialize Groq LLM for query generation
    groq_api_key = os.getenv("GROQ_API_KEY")
    groq_model = os.getenv("GROQ_MODEL")

    if not groq_api_key or not groq_model:
        raise ValueError(
            "GROQ_API_KEY or GROQ_MODEL missing from .env"
        )

    llm = ChatGroq(
        model=groq_model,
        temperature=0
    )

    # 4. Wrap MMR retriever with MultiQueryRetriever
    multi_query_retriever = MultiQueryRetriever.from_llm(
        retriever=mmr_retriever,
        llm=llm,
        include_original=True
    )

    # 5. Retrieve documents using multiple queries
    documents = multi_query_retriever.invoke(query)

    return documents
