#!/usr/bin/env python3

# ======================================================================
# customer_query_handler.py
# ======================================================================
# Created as submission for
# Govtech AI Bootcamp 2024
# Week 7 - Quick Prototyping with Streamlit
#
# Lee Woei Chieh (MINDEF)
# 14 Sep 2024
# ======================================================================

# ======================================================================
# Common imports

# Readjusted the style of import, so that the namespace is not as crowded,
# at the cost of more verbose commands
# Instead of "from xxx import yyy" to "import xxx"
# E.g. instead of "from dotenv import load_dotenv"
#              to "import dotenv"
#                 "dotenv.load_dotenv()"

import json

import helper_functions.llm

# imports for langchain
import langchain
import langchain.prompts
import langchain.chains
import langchain_openai.embeddings
import langchain_chroma

# ======================================================================
# Global variables

# ======================================================================


# ======================================================================
# Helper functions
# ======================================================================


# Functions to retrieve RAG queries
filepath_vector_store = "./data/chroma_langchain_db"
filepath_vector_store_course_finder = "./data/ssg_courses_db"

# Specify embedding model
embeddings_model = langchain_openai.embeddings.OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector_store = langchain_chroma.Chroma(
    collection_name="ai_bootcamp_info_deck",
    embedding_function=embeddings_model,
    persist_directory=filepath_vector_store,
)

vector_store_course_finder = langchain_chroma.Chroma(
    collection_name="ssg_courses",
    embedding_function=embeddings_model,
    persist_directory=filepath_vector_store_course_finder,
)


def rag_answer_query(user_query):
    """Answer the given user_query, using the vector_store."""

    # Build prompt
    template = """
You are an AI assistant tasked to answer question regarding a course 
called AI Bootcamp.
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

    answer = qa_chain.invoke(user_query)

    return answer["result"]


def rag_answer_query_course_finder(user_query):
    """Answer the given user_query, using the vector_store."""

    # Build prompt
    template = """
You are an AI assistant tasked to answer question regarding SkillsFuture 
courses. You are given a directory of courses in json format as context. 
When recommending courses, always include the course ID as part of the answer. 
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
        retriever=vector_store_course_finder.as_retriever(search_kwargs={"k": 10}),
        return_source_documents=True,  # Make inspection of documents possible
        chain_type_kwargs={"prompt": qa_chain_prompt},
    )

    answer = qa_chain.invoke(user_query)

    return answer["result"]


# ======================================================================
# Main script


def main():
    pass


# End of main script
# ======================================================================


if __name__ == "__main__":
    main()
