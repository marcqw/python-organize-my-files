import os
import shutil
import argparse
import json

def load_config(config_file):
    with open(config_file, 'r') as f:
        return json.load(f)

def sort_files(source_directory, config_file):
    target_directories = load_config(config_file)

    # Create subdirectories if they do not already exist
    for directory in target_directories.keys():
        directory_path = os.path.join(source_directory, directory)
        os.makedirs(directory_path, exist_ok=True)

    # Go through all the files in the source directory and move them to the appropriate folders
    for file in os.listdir(source_directory):
        file_path = os.path.join(source_directory, file)
        
        # Check if it is a file and not a folder
        if os.path.isfile(file_path):
            for directory, extensions in target_directories.items():
                # Check the file extension and move it to the corresponding folder
                if any(file_path.endswith(ext) for ext in extensions):
                    target_path = os.path.join(source_directory, directory, file)
                    shutil.move(file_path, target_path)
                    break

    print("Sorting completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sort files in a directory based on their type.')
    parser.add_argument('directory', type=str, help='The path to the directory to sort.')
    parser.add_argument('config', type=str, help='The path to the configuration file.')
    
    args = parser.parse_args()
    sort_files(args.directory, args.config)
