import logging
import os

def getAlphaAdvantageAPIKey():
    api_key = os.getenv("ALPHA_ADVANTAGE_API_KEY")
    if not api_key:
        logging.error(
            "ALPHA_ADVANTAGE_API_KEY environmental variable not found. Prompting..."
        )
        api_key = input("Please enter your AlphaAdvantage API key:")
        if api_key:
            os.putenv("ALPHA_ADVANTAGE_API_KEY", api_key)
        else:
            logging.error(
                "No acceptable ALPHA_ADVANTAGE_API_KEY given. Please update the environmental variables and please try again."
            )

    return api_key