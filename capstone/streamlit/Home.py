#!/usr/bin/env python3
"""
# ======================================================================
# main.py
# ======================================================================
# Created as submission for
# Govtech AI Bootcamp 2024
# Week 8 - Deploying Streamlit App
#
# Lee Woei Chieh (MINDEF)
# Updated on 21 Sep 2024
# ======================================================================
"""

# ======================================================================
# Common imports

# Readjusted the style of import, so that the namespace is not as crowded,
# at the cost of more verbose commands
# Instead of "from xxx import yyy" to "import xxx"
# E.g. instead of "from dotenv import load_dotenv"
#              to "import dotenv"
#                 "dotenv.load_dotenv()"

import streamlit as st
import pandas as pd

import logics.customer_query_handler
import helper_functions.utility
import helper_functions.disclaimer

# ======================================================================
# Global variables
FILEPATH_HOME = "./data/home.md"

# ======================================================================


# ======================================================================
# Helper functions
# ======================================================================


# ======================================================================
# Main script


def main():
    """Main script to test out writing a Streamlit app."""

    # region <----------- Streamlit App Configuration -------------->
    st.set_page_config(layout="centered", page_title="Course Information")
    # endregion <----------- Streamlit App Configuration -------------->

    with open(FILEPATH_HOME, 'r') as f:
        TEXT_HOME = f.read()

    st.title("Course Information Portal")

    # Display disclaimer message
    helper_functions.disclaimer.display_disclaimer()

    st.markdown(TEXT_HOME)


# End of main script
# ======================================================================


if __name__ == "__main__":
    main()
