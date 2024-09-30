#!/usr/bin/env python3
""" Use AISAY to parse the documents into structured data.
"""

# ======================================================================
# parsedoc.py
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

import dotenv
import tiktoken
import langchain_community.document_loaders
import langchain_experimental.text_splitter
import langchain_openai.embeddings
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


def load_document():
    """
    Given a string to a PDF, load it and return a list of Document object
    corresponding to each page.
    """

    loader = langchain_community.document_loaders.PyPDFLoader(
        "AI_Champion_Bootcamp_-_Pilot_02_-_Info_Deck.pdf"
    )
    pages = loader.load()

    return pages


def split_text(pages):
    """
    Given a list of pages, split and chunk the text in the pages, and
    returns it as Document objects.
    """

    # text_splitter = langchain.text_splitter.RecursiveCharacterTextSplitter(
    #    separators=["\n\n", "\n", " ", ""],
    #    chunk_size=500,
    #    chunk_overlap=50,
    #    length_function=count_tokens
    # )
    text_splitter = langchain_experimental.text_splitter.SemanticChunker(
        langchain_openai.embeddings.OpenAIEmbeddings(model="text-embedding-3-small")
    )

    splitted_documents = text_splitter.split_documents(pages)

    return splitted_documents


def create_vector_store(splitted_documents):
    """
    Given a list of Document objects, create a vector store for subsequent
    retrieval. Saves it to disk as "./chroma_langchain.db".
    Returns the created vector store.
    """

    # Specify embedding model
    embeddings_model = langchain_openai.embeddings.OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    # create the vector store
    vector_store = langchain_chroma.Chroma.from_documents(
        collection_name="ai_bootcamp_info_deck",
        documents=splitted_documents,
        embedding=embeddings_model,
        persist_directory="./chroma_langchain_db",
    )

    return vector_store


def test_run():
    """Test run of created scripts."""

    pages = load_document()
    splitted_documents = split_text(pages)
    vector_store = create_vector_store(splitted_documents)


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
