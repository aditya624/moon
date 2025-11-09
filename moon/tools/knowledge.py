from langchain_huggingface import HuggingFaceEndpointEmbeddings
from moon.config import settings
from langchain_qdrant import QdrantVectorStore

from langfuse.langchain import CallbackHandler

class Knowledge(object):
    def __init__(self):
        self.embeddings = HuggingFaceEndpointEmbeddings(
            provider="hf-inference",
            huggingfacehub_api_token=settings.embedding.token,
            model=settings.embedding.model,
            model_kwargs={"normalize": True, "truncate": True}
        )

        self.vectorstore = QdrantVectorStore.from_existing_collection(
            embedding=self.embeddings,
            url=settings.qdrant.url,
            api_key=settings.qdrant.api_key,
            collection_name=settings.qdrant.collection
        )

        self.retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": settings.qdrant.top_k}
        )

    def search(self, query):
        docs = self.retriever.invoke(query, config={"callbacks":[CallbackHandler()]})
        context = ""
        for doc in docs:
            page_content = doc.page_content
            metadata = doc.metadata

            context += f"# Title: {metadata['title']}\n"
            context += f"## Link: {metadata['source']}\n"
            context += f"## Chunk of Content:\n{page_content}\n\n"

        return context