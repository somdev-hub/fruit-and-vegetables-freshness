import os
import shutil


def copy_images(src_directory, dest_directory):
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    for root, dirs, files in os.walk(src_directory):
        for file in files:
            if file.endswith(("jpg", "jpeg", "png", "webp")):
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_directory, file)
                shutil.copy2(src_file_path, dest_file_path)
                print(f"Copied {src_file_path} to {dest_file_path}")


src_directory = "dataset/Rotten"
dest_directory = "dataset2/Rotten"

copy_images(src_directory, dest_directory)
