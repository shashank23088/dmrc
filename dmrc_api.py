import requests

# Your private API key
api_key = ""    # paste your api key here

# API endpoint for real-time data
url = f"https://otd.delhi.gov.in/api/realtime/VehiclePositions.pb?key={api_key}"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the response content to a file (protobuf format)
    with open("VehiclePositions.pb", "wb") as file:
        file.write(response.content)
    print("Real-time data saved successfully!")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

