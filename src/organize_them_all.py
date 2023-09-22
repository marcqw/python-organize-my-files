import os
import shutil
import argparse

def sort_files(source_directory):
    target_directories = {
        'Images': ['.png', '.jpg', '.jpeg', '.gif', '.tiff', '.bmp'],
        'Documents': ['.doc', '.docx', '.pdf', '.txt', '.rtf', '.ppt', '.pptx', '.pdf'],
        'Excel': ['.xls', '.xlsx', '.csv'],
        'Zip': ['.zip'],
        'Sounds': ['.wav', '.mp3', '.amr'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'GP': ['.gpx', '.gp5', '.gp4'],
        #'': ['.'],
        # Add other file types and target folders as needed.
    }

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
    
    args = parser.parse_args()
    sort_files(args.directory)
