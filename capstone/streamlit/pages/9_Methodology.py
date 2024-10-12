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


# ======================================================================


# ======================================================================
# Helper functions
# ======================================================================
FILEPATH_METHODOLOGY = "./data/methodology.md"

# ======================================================================
# Main script


def main():
    st.set_page_config(page_title="Methodology")

    st.title("Methodology")

    with open(FILEPATH_METHODOLOGY, 'r') as f:
        TEXT_METHODOLOGY = f.read()

    st.write(TEXT_METHODOLOGY)



# End of main script
# ======================================================================


if __name__ == "__main__":
    main()
