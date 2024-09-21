#!/usr/bin/env python3

# ======================================================================
# 1_View_All_Courses.py
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
import streamlit as st
import pandas as pd

import helper_functions.llm

# ======================================================================
# Global variables


# ======================================================================


# ======================================================================
# Helper functions

# ======================================================================


# ======================================================================
# Main script


def main():
    # st.set_page_config(page_title="About Us")

    st.title("Full Course Listing")
    st.write("This is a listing of all courses available.")

    with open(helper_functions.llm.FILEPATH_COURSES_FULL, "r") as file:
        course_details_database = json.load(file)
    df_course_details_database = pd.json_normalize(course_details_database.values())

    st.dataframe(df_course_details_database)


# End of main script
# ======================================================================


if __name__ == "__main__":
    main()
