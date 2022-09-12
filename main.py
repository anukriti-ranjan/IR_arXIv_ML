import streamlit as st
from haystack.utils import clean_wiki_text, convert_files_to_docs, fetch_archive_from_http, print_answers
from haystack.nodes import FARMReader, TransformersReader
from haystack.utils import launch_es


launch_es()

from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import BM25Retriever

document_store = ElasticsearchDocumentStore(host="localhost", username="", password="", index="document")
#return_embedding=True


st.write("it's working!")
