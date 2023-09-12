import os
import shutil
import math

# Define the base directory name
base_dir = "civitai_wildcard_prompt"

# Get the number of files from the user
num_files = int(input("Enter the number of files: "))

# Calculate the number of folders needed
num_folders = math.ceil(num_files / 9998)

# Create the directories
for i in range(1, num_folders + 1):
    folder_name = f"{base_dir}_{i}"
    os.makedirs(folder_name)

# Get the source directory of the files to be moved
source_dir = input("Enter the source directory of the files: ")

# Move files into each folder
folder_index = 1
file_count = 0
for root, dirs, files in os.walk(source_dir):
    for file in files:
        source_path = os.path.join(root, file)
        target_folder = os.path.join(base_dir, f"{base_dir}_{folder_index}")
        target_path = os.path.join(target_folder, file)
        
        # Create the target folder if it doesn't exist
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        
        # Move the file
        shutil.move(source_path, target_path)
        
        file_count += 1
        
        # If 9998 files have been moved, move to the next folder
        if file_count == 9998:
            folder_index += 1
            file_count = 0

print(f"{num_files} files have been moved to {num_folders} directories.")
