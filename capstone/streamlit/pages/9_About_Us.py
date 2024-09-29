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

import streamlit as st

# ======================================================================
# Global variables
FILEPATH_ABOUTUS = "./data/about_us.txt"

# ======================================================================


# ======================================================================
# Helper functions
# ======================================================================


# ======================================================================
# Main script


def main():
    st.set_page_config(page_title="About Us")

    with open(FILEPATH_ABOUTUS, 'r') as f:
        TEXT_ABOUTUS = f.read()

    st.title("About this App")
    st.write(TEXT_ABOUTUS)

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
