import os
import shutil
import re

def organize_files(root_dir, target_dir):
    # Create the target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    
    # Define regex patterns for both naming conventions without "real" or "fake"
    pattern1 = re.compile(r'^([a-zA-Z]+)_(\d+)\.(jpg|jpeg|png)$')
    pattern2 = re.compile(r'^([a-zA-Z]+_[a-zA-Z]+)_(\d+)\.(jpg|jpeg|png)$')
    
    # Iterate through each file in the root directory
    for file_name in os.listdir(root_dir):
        file_path = os.path.join(root_dir, file_name)
        
        # Check if it's a file
        if os.path.isfile(file_path):
            # Match the file name with the patterns
            match1 = pattern1.match(file_name)
            match2 = pattern2.match(file_name)
            pp = file_name.split('_')
            del pp[-1]

            folder_name = '_'.join(pp)
            
            # # Determine the folder name based on the matching pattern
            # if match1:
            #     folder_name = match1.group(1)  # Use only firstname
            # elif match2:
            #     folder_name = match2.group(1)  # Use firstname_lastname
            # else:
            #     # Skip files that don't match either pattern
            #     continue
            
            # Create subfolder in target directory if it doesn't exist
            target_folder = os.path.join(target_dir, folder_name)
            os.makedirs(target_folder, exist_ok=True)
            
            # Move the file to the corresponding folder
            shutil.move(file_path, os.path.join(target_folder, file_name))
            print(f"Moved {file_name} to {target_folder}")

# Example usage
root_directory = "lfw_checkpoint"
target_directory = "lfw_checkpoint_sub"
organize_files(root_directory, target_directory)
