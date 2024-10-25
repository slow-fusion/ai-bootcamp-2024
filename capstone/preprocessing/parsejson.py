#!/usr/bin/env python3
""" Collection of scripts to parse a JSON text into Chroma_DB.
"""

# ======================================================================
# parsejson.py
# ======================================================================
# Created as submission for
# Govtech AI Bootcamp 2024
# Capstone Project
#
# Lee Woei Chieh (MINDEF)
# ======================================================================

# ======================================================================
# Common imports

import os
import requests
import json

import dotenv
import tiktoken
from langchain_community.document_loaders import TextLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_text_splitters import RecursiveJsonSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
import langchain_chroma

# ======================================================================
# Global variables

FILEPATH_DOTENV = "../../../.env"
URL_AISAY = "https://aisay-stg.auth.ap-southeast-1.amazoncognito.com/oauth2/token"

# Loads into environmental variables
dotenv.load_dotenv(FILEPATH_DOTENV)
AISAY_CLIENT_ID = os.environ["AISAY_CLIENT_ID"]
AISAY_CLIENT_SECRET = os.environ["AISAY_CLIENT_SECRET"]

# ======================================================================


# ======================================================================
# Helper functions
# ======================================================================


def count_tokens(text):
    """Count number of tokens contained within given text."""

    encoding = tiktoken.encoding_for_model("gpt-4o-mini")
    return len(encoding.encode(text))


def get_aisay_authtoken():
    """Get the OAUTH access token to use AISAY."""

    # Define the payload for the access token request
    payload = {"grant_type": "client_credentials", "scope": "aisay-api/query"}

    # Make the request to the AWS Cognito Token endpoint
    response = requests.post(
        URL_AISAY,
        data=payload,
        auth=requests.auth.HTTPBasicAuth(AISAY_CLIENT_ID, AISAY_CLIENT_SECRET),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=30,
    )

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        token_response = response.json()
        access_token = token_response.get("access_token")
        print("Access token obtained")
    else:
        access_token = None
        print("Failed to retrieve access token:", response.status_code, response.text)

    return access_token



def load_text(filename):
    """
    Given a string to a text file, load it and return a single Document
    object.
    """

    loader = TextLoader(filename)

    return loader.load()


def load_document():
    """
    Load all the source documents.
    """

    # Load JSON text file
    with open("courses_first500.json", "r") as f:
        pages = json.load(f)

    return pages


def split_text(pages):
    """
    Given a list of pages, split and chunk the text in the pages, and
    returns it as Document objects.
    """

    json_splitter = RecursiveJsonSplitter()

    splitted_documents = json_splitter.create_documents(texts=pages)

    return splitted_documents


def create_vector_store(splitted_documents):
    """
    Given a list of Document objects, create a vector store for subsequent
    retrieval. Saves it to disk as "./aibootcamp_db".
    Returns the created vector store.
    """

    # Specify embedding model
    embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")

    # create the vector store
    vector_store = langchain_chroma.Chroma.from_documents(
        collection_name="ssg_courses",
        documents=splitted_documents,
        embedding=embeddings_model,
        persist_directory="./ssg_courses_db",
    )

    return vector_store


def test_run():
    """Test run of created scripts."""

    pages = load_document()
    splitted_documents = split_text(pages)
    create_vector_store(splitted_documents)


# ======================================================================
# Main script


def main():
    """Parses the given document using AISAY into structured output."""

    # print(
    #    "This file contains the common helper functions used in Streamlit.\n"
    #    "It is not meant to be run directly."
    # )

    test_run()


# End of main script
# ======================================================================


if __name__ == "__main__":
    main()
