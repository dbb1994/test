import json

def get_response_content(response):

    result = json.loads(response.text)
    return result