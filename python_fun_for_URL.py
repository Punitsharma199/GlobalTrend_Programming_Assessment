import requests
from requests.exceptions import RequestException

def download_urls(urls):
    max_retries = 3
    results = {}

    for url in urls:
        retry_count = 0
        success = False

        while (retry_count < max_retries and not success):
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise error for bad response status

                # If successful, store the content in results
                results[url] = response.content
                success = True

            except requests.exceptions.RequestException as e:
                # Handle connection errors, HTTP errors, and retries
                print(f"Attempt {retry_count+1} failed for URL: {url}. Error: {e}")
                retry_count += 1

            except Exception as e:
                # Handle other unexpected exceptions
                print(f"Unexpected error occurred for URL: {url}. Error: {e}")
                retry_count += 1

    return results

# usage
urls = [
    'https://facebook.com',
    'https://youtube.com',
    'https://www.python.org',
    'https://google.com'
]

downloaded_contents = download_urls(urls)
print(downloaded_contents.keys())  # List of URLs successfully downloaded

# output : dict_keys(['https://facebook.com', 'https://youtube.com', 'https://www.python.org', 'https://google.com'])
