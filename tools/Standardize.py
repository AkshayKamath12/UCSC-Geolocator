import os
import re

def standardize_filename(filename):
    """Standardize the filename to the format xxx.xxx_xxx.xxx_direction."""
    # Replace $ with . in the filename
    standardized_filename = filename.replace('$', '.')
    match = re.search(r'([-+]?\d*\.\d+|\d+)_([-+]?\d*\.\d+|\d+)', standardized_filename)
    if match:
        lat = match.group(1)
        lon = match.group(2)
        direction = standardized_filename.split('_')[-1]
        new_filename = f"{lat}_{lon}_{direction}"
        return new_filename
    return filename

def standardize_filenames_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.jpg'):
                new_filename = standardize_filename(file)
                if new_filename != file:
                    old_path = os.path.join(root, file)
                    new_path = os.path.join(root, new_filename)
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")

if __name__ == "__main__":
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
    standardize_filenames_in_directory(output_dir)