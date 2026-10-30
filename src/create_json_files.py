import os
import json
import sys

def create_json_files(directory, num_files):
    # Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)
    
    # Get the list of existing files in the directory
    existing_files = set(os.listdir(directory))
    
    # Create the specified number of JSON files
    created_files = 0
    for i in range(1, num_files + 1):
        file_name = f"{i}.json"
        if file_name in existing_files:
            print(f"File {file_name} already exists. Skipping.")
            continue
        
        file_path = os.path.join(directory, file_name)
        data = {
            "id": i,
            "name": f"Item {i}",
            "description": f"This is item number {i}",
            "value": i * 10
        }
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"Created {file_path}")
        created_files += 1
    
    print(f"\nSuccessfully created {created_files} JSON files in the '{directory}' directory.")

def main():
    # Check if directory and number of files were provided as command-line arguments
    if len(sys.argv) > 2:
        directory = sys.argv[1]
        try:
            num_files = int(sys.argv[2])
        except ValueError:
            print("Error: Please provide a valid number of files as the second argument.")
            sys.exit(1)
    else:
        # Default to creating 5 files in the current directory if no arguments are provided
        directory = '.'
        num_files = 5
        print(f"No directory or number specified. Creating {num_files} files in the current directory by default.")
    
    print(f"\nSelected directory: {directory}")
    
    # Create JSON files
    create_json_files(directory, num_files)

if __name__ == "__main__":
    main()