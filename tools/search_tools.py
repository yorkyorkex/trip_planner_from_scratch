# search_tools.py
import os
import json
import requests


def search_internet(query: str) -> str:
    """Useful to search the internet about a given topic and return relevant results"""
    top_result_to_return = 4
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': os.environ['SERPER_API_KEY'],
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    # check if there is an organic key
    if 'organic' not in response.json():
        return "Sorry, I couldn't find anything about that, there could be an error with you serper api key."
    else:
        results = response.json()['organic']
        string = []
        for result in results[:top_result_to_return]:
            try:
                string.append('\n'.join([
                    f"Title: {result['title']}", f"Link: {result['link']}",
                    f"Snippet: {result['snippet']}", "\n--------------------"
                ]))
            except KeyError:
                continue

        return '\n'.join(string)


class SearchTools:
    search_internet = search_internet
