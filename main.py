import openai 
import os
from dotenv import load_dotenv
import streamlit as st
from pymilvus import connections, Collection, utility
from openai import AzureOpenAI

from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import AzureOpenAIEmbeddings


load_dotenv()

# Set up OpenAI and Milvus connections
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_version = os.getenv("OPENAI_API_VERSION")

COLLECTION_NAME = os.getenv("COLLECTION_NAME")
EMBEDDING_MODEL = os.getenv("OPENAI_ENGINE")
MILVUS_HOST = os.getenv("MILVUS_HOST")
MILVUS_PORT = os.getenv("MILVUS_PORT")
DIMENSION =  os.getenv("DIMENSION") 

connections.connect(host=MILVUS_HOST, port=MILVUS_PORT) 
collection = Collection(name=COLLECTION_NAME)
collection.load()

has = utility.has_collection(COLLECTION_NAME)
print(f"Does {COLLECTION_NAME} collection exist in Milvus: {has}")

# Azure OpenAI client
client = AzureOpenAI(api_version=openai.api_version, api_key=openai.api_key, azure_endpoint=openai.api_base)

# Generate embeddings
def generate_embeddings(texts):
    return [client.embeddings.create(input=[text], model=EMBEDDING_MODEL).data[0].embedding for text in texts]

# Search in Milvus
def search_milvus(queries):
    top_k = 5
    if type(queries) != list:
        queries = [queries]
    documents = collection.search(generate_embeddings(queries), anns_field='embedding', param={"metric_type": "L2", "params": {"ef": 64}}, limit=top_k, output_fields=['page_content', 'source'])
    context = ""
    for values in documents:
        for doc in values:
            context += doc.entity._row_data["page_content"] + " link: " + doc.entity._row_data["source"] + " "
    return context

# Generate answer with OpenAI LLM
def generate_answer(question, context, temperature):
    prompt = f"""Given this text extracts:
    -----
    {context}
    -----
    Please answer with to the following question:
    Question: {question}
    Answer: """
    response = client.chat.completions.create(model="gpt-35-turbo", messages=[{"role": "user", "content": prompt}], temperature=temperature)
    return response.choices[0].message.content


# Streamlit interface
with st.sidebar:
    st.markdown(
        "## How to use\n"
        "1. Choose pre-loaded collection.\n"
        "2. If CSV is chosen as a data source, upload a CSV file.\n"
        "3. Ask a question about Wiki Softtech Pages \n"
    )
    st.markdown("---")
    st.markdown("# About")
    st.markdown(
        "AI app to find answers from [Wiki Softtech](https://wiki.softtech.com.tr/) in a Space. "
        "It uses vector database as [Milvus]( https://milvus.io/docs/overview.md ) "
         

    )
    st.markdown("[View the source code on GitHub](https://github.com/devops-alierdogan/wikiqna)")


st.title("Softtech Wiki Knowledge Base")
#temperature = st.slider("Choose the temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1)

# Veri kaynağı seçimi ve CSV dosyası yükleme
data_sources = st.multiselect("Data Source Seçimi", ["Collection Name: DEVOPS", "CSV Upload"])
csv_file = st.file_uploader("CSV Dosyası Yükle", type=["csv"]) if "CSV Upload" in data_sources else None



embeddings = AzureOpenAIEmbeddings(
    azure_deployment="gpt-35-turbo",
    openai_api_version="2023-07-01-preview",
)

def process_csv_data(csv_file, query):
    # CSV dosyasını DataFrame olarak oku
    loader = PyPDFLoader(csv_file)
    pages = loader.load_and_split()
    
    faiss_index = FAISS.from_documents(pages, embeddings)
    docs = faiss_index.similarity_search(query , k=2)
    for doc in docs:
        print(str(doc.metadata["page"]) + ":", doc.page_content[:300])
        
    

    return all_results

question = st.text_input("Enter your question", value="DevOps Künyesi Nedir?")

if st.button('Get Answer'):
    with st.spinner("Retrieving data and generating answer..."):
        retrieved_documents = search_milvus(question)   
        answer = generate_answer(question, retrieved_documents, 0)
        st.text_area("Answer", value=answer, height=300)
        
 
        
        
        
        
        
        
        
        

