import os
import shutil

def copy_images(source_folder, target_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png')):
                source_file = os.path.join(root, file)
                subfolder_parts = os.path.basename(root).split('_')
                subfolder_name = '_'.join(subfolder_parts[1:])
                target_file = os.path.join(target_folder, subfolder_name + '_' + file)
                shutil.copy(source_file, target_file)
source_folder = '/Users/malik/Desktop/hocschule/BA/data/images'
target_folder = '/Users/malik/Desktop/hocschule/BA/data/imagesALL'
copy_images(source_folder, target_folder)
