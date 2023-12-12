import urllib.parse, urllib.request, urllib.error, json
import pprint # Module that allows you print complicated data in a more readable way
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def call_api(q):
    api_key = 'eTOuRjyq+I7QGR8Qy+6t7Q==IlNa5L9a2ZTOKQCn'
    query = q
    api_url = 'https://api.api-ninjas.com/v1/nutrition'
    params = {'query': query}
    headers = {'X-Api-Key': api_key}

    try:
        encoded_params = urllib.parse.urlencode(params)
        full_url = f'{api_url}?{encoded_params}'
        request = urllib.request.Request(full_url, headers=headers)

        with urllib.request.urlopen(request) as response:
            api_response = response.read().decode()
        parsed_response = json.loads(api_response)
        return parsed_response
    except urllib.error.URLError as e:
        print(f"Error accessing the API: {e}")