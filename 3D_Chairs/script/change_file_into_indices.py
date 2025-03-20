import os
import shutil

def find_file_indices_and_rename(index_file_path, folder_path):
    # Read the index file
    with open(index_file_path, 'r') as file:
        index_lines = file.readlines()
    
    # Create a dictionary mapping filenames to indices
    index_dict = {}
    for line in index_lines:
        if line.strip():  # Skip empty lines
            parts = line.strip().split(' ', 1)  # Split on first space
            if len(parts) == 2:
                index = parts[0].strip('.')  # Remove the period after the number
                filename = parts[1].strip()
                index_dict[filename] = index
    
    # Check each file in the folder and rename
    results = []
    for filename in os.listdir(folder_path):
        if filename in index_dict:
            index = index_dict[filename]
            # Format index as three digits with leading zeros
            formatted_index = f"{int(index):03d}"
            
            # Get file extension
            file_extension = os.path.splitext(filename)[1]
            
            # Create new filename
            new_filename = f"chair_{formatted_index}{file_extension}"
            
            # Full paths for renaming
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            shutil.copy2(old_file_path, new_file_path)  # Copy instead of rename to preserve original
            
            results.append((filename, new_filename, formatted_index))
        else:
            results.append((filename, "Not renamed", "Not found in index"))
    
    return results

def main():
    # Get the paths from the user
    index_file = input("Enter the path to your index file: ")
    folder_path = input("Enter the path to the folder containing the files: ")
    
    # Find indices and rename files
    results = find_file_indices_and_rename(index_file, folder_path)
    
    # Display the results
    print("\nRenaming Results:")
    print("-" * 70)
    print(f"{'Original Filename':<40} | {'New Filename':<20} | {'Index':<5}")
    print("-" * 70)
    for original, new, index in results:
        print(f"{original[:38]:<40} | {new:<20} | {index:<5}")

if __name__ == "__main__":
    main()