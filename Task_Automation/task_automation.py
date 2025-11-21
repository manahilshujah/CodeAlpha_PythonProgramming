import os
import shutil

source_folder = input("Enter the path of the source folder: ").strip()
destination_folder = input("Enter the path of the destination folder: ").strip()

if not os.path.exists(source_folder):
    print("Error: Source folder does not exist. Please check the path.")
    exit()

os.makedirs(destination_folder, exist_ok=True)

moved_count = 0

for file_name in os.listdir(source_folder):
    if file_name.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        if os.path.exists(destination_path):
            print(f"File already exists, skipping: {file_name}")
        else:
            shutil.move(source_path, destination_path)
            print(f"Moved: {file_name}")
            moved_count += 1

if moved_count == 0:
    print("No .jpg files found in the source folder.")
else:
    print(f"Successfully moved {moved_count} .jpg file(s) to {destination_folder}")
