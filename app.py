from fastapi import APIRouter, FastAPI
import os
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.vectorstores.pgvector import PGVector, DistanceStrategy
from langchain.embeddings import OpenAIEmbeddings
app = FastAPI()
router = APIRouter()
from typing import Annotated, List, Optional, Dict

# Run export OPENAI_API_KEY=sk-YOUR_OPENAI_API_KEY...
# Or you can get openAI api key by reading local .env file
# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv())

OPENAI_API_KEY  = os.environ['OPENAI_API_KEY']
CONNECTION_STRING = os.environ['CONNECTION_STRING']

embeddings = OpenAIEmbeddings()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 2000,
    chunk_overlap  = 500,
    length_function = len,
    is_separator_regex = False,
)

@router.post("/upload/")
async def dev_question(urls: List[str], metadata: Optional[List[Dict]] = None):
    output = []

    if not metadata:
        metadata = [{} for _ in range(len(urls))] # To handle empty metadata

    loader = UnstructuredURLLoader(urls=urls) # We may need to split it for further integration
    documents = loader.load()

    for file, meta in zip(documents, metadata):
        text = file.page_content
        docs = text_splitter.create_documents([text], metadatas=metadata)

        # Example placeholder for PGVector
        db = PGVector.from_documents(
            documents=[docs],
            embedding=embeddings,
            collection_name="blog_posts",
            distance_strategy=DistanceStrategy.COSINE,
            connection_string=CONNECTION_STRING
        )

        # Append the result to the output list
        output.append(db)

    return output


# Include the router in the main app
app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI app using uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)