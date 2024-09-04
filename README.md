<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Delhi Metro Real-Time Vehicle Positions</title>
</head>
<body>

<h1>Delhi Metro Real-Time Vehicle Positions</h1>

<p>This repository fetches real-time vehicle position data from the Delhi Metro API and parses it into a CSV format. It uses a <code>.proto</code> file to define the structure of the Protobuf data.</p>

<h2>Project Files</h2>

<ul>
  <li><code>dmrc.proto</code>: The Protobuf definition file for real-time vehicle position data.</li>
  <li><code>dmrc_pb2.py</code>: Generated Python code from the <code>dmrc.proto</code> file using the <code>protoc</code> command. This is required to parse the Protobuf data.</li>
  <li><code>dmrc_api.py</code>: Python script to call the Delhi Metro API and download the real-time data in <code>.pb</code> format.</li>
  <li><code>parse_pb.py</code>: Python script to parse the downloaded <code>.pb</code> file and convert it into a CSV file with essential vehicle data.</li>
  <li><code>run_dmrc.sh</code>: A shell script that automates the process of calling the API, downloading the <code>.pb</code> file, and parsing it into a CSV file.</li>
</ul>

<h2>Getting Started</h2>

<p>To use this project, follow the steps below:</p>

<ol>
  <li><strong>Clone the repository:</strong></li>
  <pre><code>git clone https://github.com/your-repo/delhi-metro-positions.git</code></pre>

  <li><strong>Install dependencies:</strong></li>
  <p>This project requires the <code>protobuf</code> and <code>pandas</code> Python libraries. Install them using:</p>
  <pre><code>pip install protobuf pandas</code></pre>

  <li><strong>Generate the <code>dmrc_pb2.py</code> file:</strong></li>
  <p>If you do not already have the <code>dmrc_pb2.py</code> file, you need to generate it from the <code>dmrc.proto</code> file using the <code>protoc</code> command:</p>
  <pre><code>protoc --python_out=. dmrc.proto</code></pre>
  <p>This will generate the <code>dmrc_pb2.py</code> file, which is necessary to parse the Protobuf data.</p>

  <li><strong>Run the shell script:</strong></li>
  <p>The shell script <code>run_dmrc.sh</code> automates the process of fetching real-time data, parsing it, and saving it to a CSV file. Make sure the script is executable by running:</p>
  <pre><code>chmod +x run_dmrc.sh</code></pre>
  <p>Then run the script:</p>
  <pre><code>./run_dmrc.sh</code></pre>
  <p>This will download the real-time vehicle position data from the Delhi Metro API, parse it, and save a CSV file to the <code>outputs</code> directory, with the filename <code>vehicle_positions_{timestamp}.csv</code>.</p>
</ol>

<h2>Directory Structure</h2>

<pre>
delhi-metro-positions/
│
├── dmrc.proto        # Protobuf definition file
├── dmrc_pb2.py       # Python file generated from dmrc.proto using protoc
├── dmrc_api.py       # Script to fetch real-time data
├── parse_pb.py       # Script to parse .pb file and generate CSV
├── run_dmrc.sh       # Shell script to automate the process
├── outputs/          # Directory where parsed CSV files will be saved
└── README.html       # This README file
</pre>

<h2>Example Output</h2>

<p>The CSV file generated by the script will contain the following columns:</p>

<ul>
  <li><code>vehicle_id</code>: Unique ID for each vehicle</li>
  <li><code>route_id</code>: Route ID from the GTFS feed</li>
  <li><code>direction_id</code>: Direction of the trip</li>
  <li><code>start_time</code>: Start time of the trip</li>
  <li><code>start_date</code>: Start date of the trip</li>
  <li><code>latitude</code>: Latitude of the vehicle's position</li>
  <li><code>longitude</code>: Longitude of the vehicle's position</li>
  <li><code>timestamp</code>: Timestamp of the position reading</li>
</ul>

<h2>Contact</h2>
<p>If you encounter any issues, feel free to open an issue on the GitHub repository or reach out at <a href="mailto:your-email@example.com">your-email@example.com</a>.</p>

</body>
</html>
