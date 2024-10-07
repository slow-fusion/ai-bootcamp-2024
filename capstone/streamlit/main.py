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

    # Check if the user gave the correct password
    if not helper_functions.utility.check_password():
        st.stop()

    st.title("AI Bootcamp Course Information")

    # Display disclaimer message
    helper_functions.disclaimer.display_disclaimer()

    form = st.form(key="form")
    form.subheader("What do you want to know about AI Bootcamp?")

    user_prompt = form.text_area("Example: Who can join AI Bootcamp?", height=200)

    if form.form_submit_button("Submit"):
        st.toast(f"User Input Submitted - {user_prompt}")
        # response, course_details = logics.customer_query_handler.process_user_message(
        #    user_prompt
        # )
        response = logics.customer_query_handler.rag_answer_query(user_prompt)

        st.write(response)

        st.divider()

        # df_course_details = pd.json_normalize(course_details)
        # st.dataframe(df_course_details)

        print(f'User Input is "{user_prompt}"')


# End of main script
# ======================================================================


if __name__ == "__main__":
    main()
