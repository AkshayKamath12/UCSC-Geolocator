import os

def remove_images():
    """Remove images based on coordinates in Removal.txt"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    removal_file = os.path.join(script_dir, 'Removal.txt')
    output_dir = os.path.join(script_dir, 'output')
    
    # Read coordinates to remove
    with open(removal_file, 'r') as f:
        coordinates = set(line.strip() for line in f.readlines())
    
    # Count and collect files to be removed
    files_to_remove = []
    for filename in os.listdir(output_dir):
        if filename.endswith('.jpg'):
            parts = filename.split('_')
            if len(parts) == 3:
                lat, lon = parts[0], parts[1]
                coord_key = f"{lat},{lon}"
                
                if coord_key in coordinates:
                    files_to_remove.append((filename, os.path.join(output_dir, filename)))
    
    # Show confirmation prompt
    if not files_to_remove:
        print("No files found matching the coordinates in Removal.txt")
        return
    
    print(f"Found {len(files_to_remove)} files to remove:")
    for filename, _ in files_to_remove[:5]:
        print(f"- {filename}")
    if len(files_to_remove) > 5:
        print(f"... and {len(files_to_remove) - 5} more files")
    
    confirmation = input("\nDo you want to proceed with removal? (y/n): ").lower().strip()
    if confirmation != 'y':
        print("Operation cancelled")
        return
    
    # Proceed with removal
    removed_count = 0
    for filename, file_path in files_to_remove:
        try:
            os.remove(file_path)
            removed_count += 1
            print(f"Removed: {filename}")
        except OSError as e:
            print(f"Error removing {filename}: {e}")
    
    print(f"\nRemoval complete: {removed_count} files removed")

if __name__ == '__main__':
    remove_images()