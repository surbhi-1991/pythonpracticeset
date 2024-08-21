import os

def print_directory_contents(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    
    # Check if the given path is a directory
    if not os.path.isdir(directory):
        print(f"'{directory}' is not a directory.")
        return
    
    # Get list of files and directories in the given directory
    contents = os.listdir(directory)
    
    # Print each item in the directory
    print(f"Contents of directory '{directory}':")
    for item in contents:
        print(item)

# Example usage:
directory_path = "/"
print_directory_contents(directory_path)
