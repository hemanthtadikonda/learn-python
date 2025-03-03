import requests

URL_list = "main.log"

with open(URL_list, "r") as file:
    for line in file:
        url = line.strip()  # Remove leading/trailing whitespace and newline
        if url:
            try:
                response = requests.get(url)
                response.raise_for_status() # Raises exception for bad status codes.
                print(f"{url} is up!")
            except requests.exceptions.ConnectionError: #Catch name resolution errors.
                print(f"{url} is down!")
            except requests.exceptions.HTTPError: #catch bad status codes.
                print(f"{url} is down!")
            except Exception as e: # Catch any other errors.
                print(f"Error checking {url}: {e}")
