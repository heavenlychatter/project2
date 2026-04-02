import httpx
from functions.appFunctions import getAlphaAdvantageAPIKey

def httpClient() -> httpx.Client:
    client = httpx.Client()
    return client
    
def makeAlphaVantageRequest(function: str, **kwargs) -> dict[str, any] | None: # this returns the raw data from the request as json, calling functions are responsible for parsing the data
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": function,
        "apikey": getAlphaAdvantageAPIKey()
    }
    params.update(kwargs) # pass parameters into this function as kwargs and they will be added to the params dict
    
    try:
        with httpClient() as client:
            response = client.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            if "Information" in data:
                print(f"API call limit reached: {data['Information']}")
                return None
            return response.json()
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
    except httpx.RequestError as e:
        print(f"An error occurred while making the request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None
    
