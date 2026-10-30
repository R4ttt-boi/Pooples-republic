#!/usr/bin/env python3
import os
import json
import sys

def list_directories(path='.'):
    """List directories in the specified path."""
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    
    if not directories:
        print(f"No directories found in '{path}'.")
        return []
    
    print(f"\nDirectories in '{path}':")
    for i, directory in enumerate(directories, 1):
        print(f"{i}. {directory}")
    
    return directories

def main():
    print("\nJSON File Creator\n===============")
    
    current_path = '.'
    while True:
        directories = list_directories(current_path)
        
        print("\nOptions:")
        print("1. Select a directory to navigate into")
        print("2. Go up to parent directory")
        print("3. Create JSON files in current directory")
        print("4. Exit")
        
        # Simulate user input for this environment
        # In a real terminal, this would be: choice = input("Enter your choice (1-4): ")
        # For this environment, we'll just wait for a command-line argument or proceed with default
        
        # Check if there's a command-line argument for the choice
        if len(sys.argv) > 1:
            choice = sys.argv[1]
            sys.argv = sys.argv[1:]  # Remove the argument to avoid reprocessing
        else:
            # Default to option 3 (create JSON files) if no input is provided
            choice = '3'
        
        if choice == '1':
            if directories:
                dir_choice = '1'  # Default to first directory
                try:
                    dir_num = int(dir_choice)
                    if 1 <= dir_num <= len(directories):
                        current_path = os.path.join(current_path, directories[dir_num - 1])
                    else:
                        print(f"Invalid choice. Using default directory.")
                except ValueError:
                    print("Invalid input. Using default directory.")
            else:
                print("No directories to navigate into. Using current directory.")
        elif choice == '2':
            parent_path = os.path.dirname(current_path)
            if parent_path == '':
                current_path = '.'
            else:
                current_path = parent_path
        elif choice == '3':
            # Create JSON files in the current directory
            num_files = 5  # Default number of files
            if len(sys.argv) > 1:
                try:
                    num_files = int(sys.argv[1])
                    sys.argv = sys.argv[1:]  # Remove the argument
                except ValueError:
                    print("Invalid number of files. Using default (5).")
            
            print(f"\nCreating {num_files} JSON files in '{current_path}'...")
            
            # Create the directory if it doesn't exist
            os.makedirs(current_path, exist_ok=True)
            
            # Get the list of existing files in the directory
            existing_files = set(os.listdir(current_path))
            
            # Create the specified number of JSON files
            created_files = 0
            for i in range(1, num_files + 1):
                file_name = f"{i}.json"
                if file_name in existing_files:
                    print(f"File {file_name} already exists. Skipping.")
                    continue
                
                file_path = os.path.join(current_path, file_name)
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
            
            print(f"\nSuccessfully created {created_files} JSON files in '{current_path}'.")
            
            # Exit after creating files
            break
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Using default option (create JSON files).")
            choice = '3'

if __name__ == "__main__":
    main()