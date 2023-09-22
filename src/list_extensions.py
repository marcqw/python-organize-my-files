import os
import argparse

def list_extensions(directory):
    extensions = set()
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Get the file extension and add it to the set of extensions
            _, extension = os.path.splitext(file)
            if extension:  # Ignore files without extension
                extensions.add(extension)
    
    if not extensions:
        print("No file extensions found.")
    else:
        print("Found file extensions:")
        for extension in sorted(extensions):
            print(extension)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='List all different file extensions in a directory.')
    parser.add_argument('directory', type=str, help='The path to the directory to scan.')
    
    args = parser.parse_args()
    list_extensions(args.directory)
