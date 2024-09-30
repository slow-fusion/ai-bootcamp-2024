#!/usr/bin/env python3
"""Contains the helper functions related to calling OpenAI through its API.


"""

# ======================================================================
# llm.py
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

import os

import dotenv
import openai
import tiktoken

# ======================================================================
# Global variables

FILEPATH_DOTENV = "../../../.env"
FILEPATH_COURSES_FULL = "./data/courses-full.json"

# ======================================================================


# ======================================================================
# Helper functions
# ======================================================================


def setup():
    """Setup the environment.
    1. Load the dotenv file to provide the API keys
    """

    # Load the environment variables
    # If the .env file is not found, the function will return `False
    dotenv.load_dotenv(FILEPATH_DOTENV)


def get_embedding(input, model="text-embedding-3-small"):
    """Function to generate embeddings."""

    response = client.embeddings.create(input=input, model=model)
    return [x.embedding for x in response.data]


def get_completion(
    prompt,
    model="gpt-4o-mini",
    temperature=0,
    top_p=1.0,
    max_tokens=1024,
    n=1,
    json_output=False,
):
    """Function for text generation."""

    if json_output:
        output_json_structure = {"type": "json_object"}
    else:
        output_json_structure = None

    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        n=n,
        response_format=output_json_structure,
    )

    return response.choices[0].message.content


def get_completion_by_messages(
    messages,
    model="gpt-4o-mini",
    temperature=0,
    top_p=1.0,
    max_tokens=1024,
    n=1,
):
    """Function for text generation from messages.
    Note that this function directly takes in "messages" as the parameter.
    """

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        n=n,
    )

    return response.choices[0].message.content


# Functions for Token Counting
def count_tokens(text):
    """Returns the number of tokens in the given text."""

    encoding = tiktoken.encoding_for_model("gpt-4o-mini")
    return len(encoding.encode(text))


def count_tokens_from_message(messages):
    """Returns the number of tokens in the given message."""

    encoding = tiktoken.encoding_for_model("gpt-4o-mini")
    value = " ".join([x.get("content") for x in messages])
    return len(encoding.encode(value))




# ======================================================================
# Main script

setup()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def main():
    """Informs user that this file is meant to be run directly."""
    print(
        "This file contains helper functions for use with OpenAI API.\n"
        "It is not meant to be run directly."
    )


# End of main script
# ======================================================================


if __name__ == "__main__":
    main()
