import rhinoscriptsyntax as rs
import os
import sys

def process_file(file_path, output_folder):
    """Process a single Rhino file and save the result."""
    # Open the file
    print("Processing file: " + file_path)
    
    # Check if file exists
    if not os.path.exists(file_path):
        print("File not found: " + file_path)
        return False
        
    # Open the file using Rhino command
    rs.Command('_-Open "' + file_path + '" _Enter')
    
    # Perform operations on the file
    # Create a new layer called "wrapped" with magenta color
    if not rs.IsLayer("wrapped"):
        # Create new layer (Magenta color RGB: 255, 0, 255)
        rs.AddLayer("wrapped", [255, 0, 255])
        print("Created new 'wrapped' layer with magenta color")
    
    # Save the processed file
    rs.Command('_-Save "' + file_path + '" _Enter')
    
    # Close the file
    rs.Command('_-Close _Enter')

def batch_process(input_folder, output_folder, file_extension=".3dm"):
    """Process all Rhino files in the input folder and save results to the output folder."""
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get all files with the specified extension
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(file_extension.lower())]
    
    if not files:
        print("No files found with extension: " + file_extension)
        return
    
    # Process each file
    for file in files[4:5]:
        file_path = os.path.join(input_folder, file)
        process_file(file_path, output_folder)
    
    print("Batch processing complete!")

# Example usage
if __name__ == "__main__":
    # Define input and output folders
    # ***IMPORTANT***
    # Change to absolute path since rs.Command('_-Open "' + file_path + '" _Enter')
    # will modify Rhino's working directory
    input_folder = os.path.abspath("../")
    output_folder = os.path.abspath("./")
    
    # Start batch processing
    batch_process(input_folder, output_folder)