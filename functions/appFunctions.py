import logging
import os

def getAlphaAdvantageAPIKey(no_prompt: bool = False) -> str:
    api_key = "AYARIRSQKP25QIL1"
    if not api_key:
        try:
            if no_prompt:
                raise ValueError("ALPHA_VANTAGE_API_KEY environment variable not found and no_prompt is set to True.")
            logging.error(
                "ALPHA_VANTAGE_API_KEY environmental variable not found. Prompting..."
            )
            api_key = input("Please enter your AlphaVantage API key:")
            if api_key:
                os.putenv("ALPHA_VANTAGE_API_KEY", api_key)
            else:
                raise ValueError("No API key provided. Please set the ALPHA_VANTAGE_API_KEY environment variable or provide it when prompted.")
        except Exception:
            logging.exception("An error occurred while retrieving the AlphaVantage API key.")
            return ""
            
    return api_key