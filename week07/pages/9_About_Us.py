#!/usr/bin/env python3

# ======================================================================
# 9_About_Us.py
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

import streamlit as st

# ======================================================================
# Global variables


# ======================================================================


# ======================================================================
# Helper functions
# ======================================================================


# ======================================================================
# Main script


def main():
    st.set_page_config(page_title="About Us")

    st.title("About this App")
    st.write(
        "This is a Streamlit app that demonstrates how to use the "
        "OpenAI API to generate text completions."
    )

    with st.expander("How to use this App", expanded=False):
        st.write(
            """
1. Enter your prompt in the text area.
1. Click the 'Submit' button.
1. The app will generate a text completion based on your prompt.
        """
        )


# End of main script
# ======================================================================


if __name__ == "__main__":
    main()
