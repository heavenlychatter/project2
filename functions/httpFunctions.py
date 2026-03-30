import httpx

def httpClient() -> httpx.Client:
    client = httpx.Client()
    
    return client