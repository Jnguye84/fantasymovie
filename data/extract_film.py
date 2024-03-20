import os
import random
import shutil

# Function to randomly keep 5 photos and delete the rest
def keep_random_photos(folder):
    files = os.listdir(folder)
    photos = [file for file in files if file.endswith(('jpg', 'jpeg', 'png', 'gif'))]
    
    # If there are more than 5 photos, randomly select 5 to keep
    if len(photos) > 5:
        photos_to_keep = random.sample(photos, 5)
        for file in files:
            if file not in photos_to_keep:
                os.remove(os.path.join(folder, file))

# Main function to iterate through folders and apply the above function
def main(root_folder):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for dirname in dirnames:
            folder = os.path.join(dirpath, dirname)
            keep_random_photos(folder)

if __name__ == "__main__":
    root_folder = "data"  # Change this to the path of your main folder
    main(root_folder)
