#!/usr/bin/env python3
""" Contains a collection of test programs to check parsedoc.py
"""

# ======================================================================
# tester.py
# ======================================================================
# Created as submission for
# Govtech AI Bootcamp 2024
# Capstone Project
#
# Lee Woei Chieh (MINDEF)
# ======================================================================

# ======================================================================
# Common imports

import langchain
import langchain_openai.embeddings
import langchain_chroma
import langchain.prompts
import langchain.chains

import parsedoc

# ======================================================================
# Global variables


# ======================================================================


# ======================================================================
# Helper functions
# ======================================================================


def test_create():
    """Test run of created scripts."""

    pages = parsedoc.load_document()
    splitted_documents = parsedoc.split_text(pages)
    vector_store = parsedoc.create_vector_store(splitted_documents)


def test_retrieve():
    """Given a previously created vector store, test the retrieval using
    a test prompt
    """
    filepath_vector_store = "./chroma_langchain_db"

    # Specify embedding model
    embeddings_model = langchain_openai.embeddings.OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vector_store = langchain_chroma.Chroma(
        "ai_bootcamp_info_deck",
        embedding_function=embeddings_model,
        persist_directory=filepath_vector_store,
    )

    # Test basic retrieval
    print("Test case 1: Test basic retrieval")
    print(vector_store.similarity_search("course duration", k=10))

    # -----------------------------
    # Test using custom Q&A prompt

    # Build prompt
    template = """
Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say you don't know, and don't try to 
make up an answer. Always say 'thanks for asking.' at the end of the answer.

Context: {context}
Question: {question}
Answer: 
    """
    qa_chain_prompt = langchain.prompts.PromptTemplate.from_template(template)

    # Run chain
    qa_chain = langchain.chains.RetrievalQA.from_chain_type(
        langchain_openai.ChatOpenAI(model="gpt-4o-mini"),
        retriever=vector_store.as_retriever(),
        return_source_documents=True,  # Make inspection of documents possible
        chain_type_kwargs={"prompt": qa_chain_prompt},
    )

    answer = qa_chain.invoke("What is the duration of the AI Champions Bootcamp?")
    print(answer)


# ======================================================================
# Main script


def main():
    """Parses the given document using AISAY into structured output."""

    # print(
    #    "This file contains the common helper functions used in Streamlit.\n"
    #    "It is not meant to be run directly."
    # )

    test_retrieve()


# End of main script
# ======================================================================


if __name__ == "__main__":
    main()
