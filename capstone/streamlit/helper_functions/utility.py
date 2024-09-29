#!/usr/bin/env python3
""" Contains the common components used in the Streamlit App.
This includes the sidebar, the title, the footer, and the password check.
"""

# ======================================================================
# utility.py
# ======================================================================
# Created as submission for
# Govtech AI Bootcamp 2024
# Week 8 - Deploying Streamlit App
#
# Lee Woei Chieh (MINDEF)
# 21 Sep 2024
# ======================================================================

# ======================================================================
# Common imports

import random

import hmac
import streamlit as st

# ======================================================================
# Global variables


# ======================================================================


# ======================================================================
# Helper functions
# ======================================================================


def check_password():
    """Returns 'True' if the user entered the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""

        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store password
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("Password is incorrect")

    return False


# ======================================================================
# Main script


def main():
    """Informs user that this file is meant to be run directly."""

    print(
        "This file contains the common helper functions used in Streamlit.\n"
        "It is not meant to be run directly."
    )


# End of main script
# ======================================================================


if __name__ == "__main__":
    main()
