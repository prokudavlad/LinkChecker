import json
import requests


def test_links(filename):
    with open(filename, 'r') as file:
        links = json.load(file)

        error_codes = {
            400: "400 Bad Request",
            403: "403 Forbidden",
            404: "404 Not Found",
            500: "500 Internal Server Error",
            502: "502 Bad Gateway",
            504: "504 Gateway Timeout"
        }

        for link in links:
            url = link["url"]
            try:
                response = requests.get(url)
                if response.status_code in error_codes:
                    print(f"Error {response.status_code}: {error_codes[response.status_code]} - {url}")
                else:
                    print(f"Success: {url}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {str(e)} - {url}")


test_links('links.json')
