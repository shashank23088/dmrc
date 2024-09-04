#!/bin/bash

# Set up variables
API_KEY=""    # paste youru api key here
API_URL="https://otd.delhi.gov.in/api/realtime/VehiclePositions.pb?key=${API_KEY}"
PB_FILE="VehiclePositions.pb"
OUTPUT_DIR="./outputs"

# Step 1: Call the API to get the real-time data and save it as a .pb file
echo "Fetching real-time data from the API..."
response=$(curl -s -o ${PB_FILE} -w "%{http_code}" ${API_URL})

if [ "$response" -eq 200 ]; then
    echo "Real-time data saved as ${PB_FILE}"
else
    echo "Failed to fetch data. HTTP status code: $response"
    exit 1
fi

# Step 2: Check if the output directory exists, if not create it
if [ ! -d "${OUTPUT_DIR}" ]; then
  mkdir -p "${OUTPUT_DIR}"
fi

# Step 3: Run the Python script (parse_pb.py) to parse the .pb file and generate the CSV
echo "Parsing .pb file and generating CSV..."
python3 parse_pb.py ${PB_FILE} ${OUTPUT_DIR}

# Final message
echo "Process completed. Output saved in ${OUTPUT_DIR}"
