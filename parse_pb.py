import dmrc_pb2  # Import the generated Python code from the .proto file
import pandas as pd
import os
import sys
from datetime import datetime

# Function to parse the .pb file and extract essential vehicle position data
def parse_vehicle_positions(pb_file, output_dir):
    # Initialize the FeedMessage object (from the .proto definition)
    feed_message = dmrc_pb2.FeedMessage()

    # Read the binary .pb file
    with open(pb_file, 'rb') as f:
        feed_message.ParseFromString(f.read())

    # List to store parsed data
    data = []

    # Iterate through all entities in the feed message
    for entity in feed_message.entity:
        if entity.HasField('vehicle'):
            vehicle_position = entity.vehicle
            position = vehicle_position.position if vehicle_position.position.latitude != 0 and vehicle_position.position.longitude != 0 else None

            # Extract only the essential data
            vehicle_data = {
                'vehicle_id': vehicle_position.vehicle.id if vehicle_position.vehicle.id != "" else None,
                'route_id': vehicle_position.trip.route_id if vehicle_position.trip.route_id != "" else None,
                'direction_id': vehicle_position.trip.direction_id if vehicle_position.trip.direction_id != 0 else None,
                'start_time': vehicle_position.trip.start_time if vehicle_position.trip.start_time != "" else None,
                'start_date': vehicle_position.trip.start_date if vehicle_position.trip.start_date != "" else None,
                'latitude': position.latitude if position and position.latitude != 0 else None,
                'longitude': position.longitude if position and position.longitude != 0 else None,
                'timestamp': vehicle_position.timestamp if vehicle_position.timestamp != 0 else None,
            }

            data.append(vehicle_data)

    # Convert the list of data into a DataFrame for easy handling
    df = pd.DataFrame(data)

    # Check if the timestamp column exists and convert it to readable datetime
    if 'timestamp' in df.columns and not df['timestamp'].isnull().all():
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

    # Generate a timestamp for the CSV file name
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = os.path.join(output_dir, f'vehicle_positions_{current_time}.csv')

    # Save the essential data to a CSV file
    df.to_csv(output_file, index=False)
    print(f"Vehicle position data saved to {output_file}")

if __name__ == "__main__":
    # Ensure arguments are passed for pb_file and output_dir
    if len(sys.argv) < 3:
        print("Usage: python parse_pb.py <pb_file_path> <output_directory>")
        sys.exit(1)

    pb_file = sys.argv[1]
    output_dir = sys.argv[2]

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Parse the .pb file and generate the CSV file
    parse_vehicle_positions(pb_file, output_dir)
