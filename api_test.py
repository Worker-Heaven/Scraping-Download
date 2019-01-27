import requests

api_url = 'https://oasm.dfsa.dk/uk/searchresult.aspx'

data = {
  't': 'shortselling',
  'ps': 10,
  'p': 1,
}

# Making the post request
response = requests.post(api_url, data=data)

print (response.json())