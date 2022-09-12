import streamlit as st
import time
from haystack.utils import clean_wiki_text, convert_files_to_docs, fetch_archive_from_http, print_answers
from haystack.nodes import FARMReader, TransformersReader
from haystack.utils import launch_es


launch_es()
time.sleep(30)

from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import BM25Retriever

#ConnectionError: Initial connection to Elasticsearch failed. Make sure you run an Elasticsearch instance at `[{'host': 'localhost', 'port': 9200}]` and that it has finished the initial ramp up (can take > 30s).
#document_store = ElasticsearchDocumentStore(host="localhost", username="", password="", index="document")
document_store = ElasticsearchDocumentStore(return_embedding=True)



st.write("it's working!")
