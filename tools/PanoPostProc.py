def parse_coordinates(input_file, output_file):
    """Parse latitude and longitude pairs from the input file and save them to the output file."""
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            # Skip lines that contain min/max latitude and longitude
            if line.startswith("Min Latitude") or line.startswith("Max Latitude") or line.startswith("Min Longitude") or line.startswith("Max Longitude"):
                continue

            # Split the line by comma and extract lat, lon pairs
            parts = line.strip().split(',')
            if len(parts) == 3:
                lat, lon = parts[1], parts[2]
                outfile.write(f"{lat},{lon}\n")

# Configuration
INPUT_FILE = 'PanoramaCoordinates.txt'
OUTPUT_FILE = 'PanoCoordPostProc.txt'

# Run the function
parse_coordinates(INPUT_FILE, OUTPUT_FILE)