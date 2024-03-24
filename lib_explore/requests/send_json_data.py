import requests

# URL for the API endpoint
url = "http://127.0.0.1:3000/api/message"

# JSON data to be sent in the request
data = {
    'name': 'John',
    'age': 25
}

"""
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"name": "John", "age": 25}' \
     http://127.0.0.1:3000/api/message
"""

response = requests.post(url="http://127.0.0.1:3000/demo", data=data)
# Check the response
if response.status_code == 200:
    # Request was successful, print the response JSON
    print("HTML response")
    print(f"{response.text}")
else:
    # Request failed, print the error code and message
    print(f"HTML Error: {response.status_code}: {response.text}")

# Send a POST request with JSON data
print("")
response = requests.post(url, json=data)
if response.status_code == 200:
    # Request was successful, print the response JSON
    print("JSON response")
    print(f"{response.json()}")
else:
    # Request failed, print the error code and message
    print(f"JSON Error: {response.status_code}: {response.json()}")

