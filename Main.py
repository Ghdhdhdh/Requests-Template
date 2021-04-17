import requests

url = 'https://jsonplaceholder.typicode.com/posts'

form_data = {
    'form': "Data"
}

requests.post(url, data=form_data, allow_redirects=False)