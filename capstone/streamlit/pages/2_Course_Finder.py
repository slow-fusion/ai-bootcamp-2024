#!/usr/bin/env python3
"""
# ======================================================================
# 2_Course_Finder.py
# ======================================================================
# Created as submission for
# Govtech AI Bootcamp 2024
#
# Lee Woei Chieh (MINDEF)
# Updated on 20 Oct 2024
# ======================================================================
"""

# ======================================================================
# Common imports

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

    st.title("Skillsfuture Course Finder")

    # Display disclaimer message
    helper_functions.disclaimer.display_disclaimer()

    form = st.form(key="form")
    form.subheader("Describe the SkillsFuture course you are looking for.")

    user_prompt = form.text_area(
        "I will search the Skillsfuture directory "
        "and recommend some courses for you.\n\n "
        "Example: What courses are good to learn about generative AI?",
        height=200,
    )

    if form.form_submit_button("Submit"):
        st.toast(f"User Input Submitted - {user_prompt}")
        response = logics.customer_query_handler.rag_answer_query_course_finder(
            user_prompt
        )

        st.write(response)

        st.divider()

        print(f'User Input is "{user_prompt}"')


# End of main script
# ======================================================================


if __name__ == "__main__":
    main()
