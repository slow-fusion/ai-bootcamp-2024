#!/usr/bin/env python3
"""Contains the helper functions related to displaying the disclaimer text.


"""

# ======================================================================
# display_disclaimer.py
# ======================================================================
# Created as submission for
# Govtech AI Bootcamp 2024
# Capstone project
#
# Lee Woei Chieh (MINDEF)
# ======================================================================

# ======================================================================
# Common imports

import streamlit as st

# ======================================================================
# Global variables

FILEPATH_DISCLAIMER = "./data/disclaimer.txt"

# ======================================================================


# ======================================================================
# Helper functions
# ======================================================================


def display_disclaimer():

    with open(FILEPATH_DISCLAIMER, "r") as f:
        DISCLAIMER = f.read()

    with st.expander("Disclaimer"):
        st.write(DISCLAIMER)


# ======================================================================
# Main script


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
