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

CATEGORY_N_COURSE_NAME = {
    "Programming and Development": [
        "Web Development Bootcamp",
        "Introduction to Cloud Computing",
        "Advanced Web Development",
        "Cloud Architecture Design",
    ],
    "Data Science & AI": [
        "Data Science with Python",
        "AI and Machine Learning for Beginners",
        "Machine Learning with R",
        "Deep Learning with TensorFlow",
    ],
    "Marketing": ["Digital Marketing Masterclass", "Social Media Marketing Strategy"],
    "Cybersecurity": ["Cybersecurity Fundamentals", "Ethical Hacking for Beginners"],
    "Business and Management": [
        "Project Management Professional (PMP)Â® Certification Prep",
        "Agile Project Management",
    ],
    "Writing and Literature": [
        "Creative Writing Workshop",
        "Advanced Creative Writing",
    ],
    "Design": ["Graphic Design Essentials", "UI/UX Design Fundamentals"],
}


with open(helper_functions.llm.FILEPATH_COURSES_FULL, "r") as file:
    DICT_OF_COURSES = json.loads(file.read())

# ======================================================================


# ======================================================================
# Helper functions
# ======================================================================


def identify_category_and_courses(user_message):
    DELIMITER = "####"

    system_message = f"""
    You will be provided with customer service queries. 
    The customer service query will be enclosed in 
    the pair of {DELIMITER}.

    Decide if the query is relevant to any specific courses in the 
    python dictionary below, which each key is a`category` 
    and the value is a list of `course_name`.

    If there are any relevant course(s) found, output the pair(s) of
    (a) `course_name` the relevant courses, and
    (b) the associated `category` into a list of dictionary object, where 
    each item in the list is a relevant course and each course is a 
    dictionary that contains two keys:
    (1) category
    (2) course_name

    {DELIMITER} {CATEGORY_N_COURSE_NAME} {DELIMITER}

    if there are no relevant courses found, output an empty list.

    Ensure your response contains only the list of dictionary objects 
    or an empty list, without any enclosing tags or delimiters.
    """

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"{DELIMITER}{user_message}{DELIMITER}"},
    ]

    category_and_product_response_str = helper_functions.llm.get_completion_by_messages(
        messages
    )
    category_and_product_response_str = category_and_product_response_str.replace(
        "'", '"'
    )
    category_and_product_response = json.loads(category_and_product_response_str)

    return category_and_product_response


def get_course_details(list_of_category_n_course: list[dict]):
    list_course_names = []
    for x in list_of_category_n_course:
        list_course_names.append(x.get("course_name"))

    list_of_course_details = []
    for course_name in list_course_names:
        list_of_course_details.append(DICT_OF_COURSES.get(course_name))

    return list_of_course_details


def generate_response_based_on_course_details(user_message, product_details):
    DELIMITER = "####"

    system_message = f"""
    Follow these steps to answer the customer's queries.
    The customer query will be delimited with a pair of {DELIMITER}.

    Step 1:{DELIMITER} If the customer is asking about courses, 
    understand the relevant course(s) from the following list.
    All available courses are shown in the json data below:
    {product_details}

    Step 2:{DELIMITER} Use the information about the course to 
    generate the answer for the customer's query.
    You must rely only on the facts or information in the course information.
    Your response should be as detailed as possible and 
    include information that is useful for the customer to better
    understand the course.

    Step 3:{DELIMITER}: Answer the customer in a friendly tone. 
    Make sure the statements are factually accurate. 
    Your response should be comprehensive and informative to help the 
    customer to make their decision. 
    Complete with details such as rating, pricing, and skiils to be learnt. 
    Use Neural Linguistic Programming to construct your response.

    Use the following format:
    Step 1:{DELIMITER} <step 1 reasoning>
    Step 2:{DELIMITER} <step 2 reasoning>
    Step 3:{DELIMITER} <step 3 response to customer>

    Make sure to include {DELIMITER} to separate every step.
    """

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"{DELIMITER}{user_message}{DELIMITER}"},
    ]

    response_to_customer = helper_functions.llm.get_completion_by_messages(messages)
    response_to_customer = response_to_customer.split(DELIMITER)[-1]

    return response_to_customer


def process_user_message(user_input):

    # Process 1: If courses are found, look them up
    category_n_course_name = identify_category_and_courses(user_input)
    print("category_n_course_name : ", category_n_course_name)

    # Process 2: Get the course details
    course_details = get_course_details(category_n_course_name)

    # Process 3: Generate the response based on course details
    reply = generate_response_based_on_course_details(user_input, course_details)

    return (reply, course_details)

# Functions to retrieve RAG queries
filepath_vector_store = "./data/chroma_langchain_db"

# Specify embedding model
embeddings_model = langchain_openai.embeddings.OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector_store = langchain_chroma.Chroma(
    "ai_bootcamp_info_deck",
    embedding_function=embeddings_model,
    persist_directory=filepath_vector_store,
)

def rag_answer_query(user_query):
    """Answer the given user_query, using the vector_store."""


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
