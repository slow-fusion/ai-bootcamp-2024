#!/usr/bin/env python3
""" Use AISAY to parse the documents into structured data.
"""

# ======================================================================
# parsedoc.py
# ======================================================================
# Created as submission for
# Govtech AI Bootcamp 2024
# Capstone Project
#
# Lee Woei Chieh (MINDEF)
# ======================================================================

# ======================================================================
# Common imports

import dotenv
import requests

# ======================================================================
# Global variables


# ======================================================================


# ======================================================================
# Helper functions
# ======================================================================


def get_token():
    """Gets the OAUTH access token to use AISAY."""

    FILEPATH_DOTENV = "../../../.env"
    URL_AISAY = "https://aisay-stg.auth.ap-southeast-1.amazoncognito.com/oauth2/token"

    dotenv.load_dotenv(FILEPATH_DOTENV)

    # Define the payload for the access token request
    PAYLOAD = {
        "grant_type": "client_credentials",
        "scope": "aisay-api/query"
    }

    # Make the request to the AWS Cognito Token endpoint
    response = requests.post(
        URL_AISAY,
        data=PAYLOAD,
        auth=requests.auth.HTTPBasicAuth(AISAY_CLIENT_ID, AISAY_CLIENT_SECRET),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=30
    )

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        token_response = response.json()
        access_token = token_response.get("access_token")
        print("Access token obtained")
    else:
        access_token = None
        print("Failed to retrieve access token:", response.status_code, response.text)

    return access_token

# ======================================================================
# Main script


def main():
    """Parses the given document using AISAY into structured output."""

    print(
        "This file contains the common helper functions used in Streamlit.\n"
        "It is not meant to be run directly."
    )


# End of main script
# ======================================================================


if __name__ == "__main__":
    main()
