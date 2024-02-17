import os
import shutil
from concurrent.futures import ThreadPoolExecutor


def sort_files_by_extension(src_folder, dest_folder):
    try:
        os.makedirs(dest_folder, exist_ok=True)

        subdirectories = [d for d in os.listdir(
            src_folder) if os.path.isdir(os.path.join(src_folder, d))]

        with ThreadPoolExecutor(max_workers=5) as executor:
            for subdir in subdirectories:
                executor.submit(process_subdirectory, src_folder, dest_folder, subdir)

    except Exception as e:
        print(f"Error processing subdirectories: {e}")

def process_subdirectory(src_folder, dest_folder, subdir):
    subdir_path = os.path.join(src_folder, subdir)
    dest_path = os.path.join(dest_folder, subdir)

    try:
        os.makedirs(dest_path, exist_ok=True)

        files = [f for f in os.listdir(subdir_path) if os.path.isfile(os.path.join(subdir_path, f))]

        for file in files:
            src_path = os.path.join(subdir_path, file)
            dest_file_path = os.path.join(dest_path, file)

            shutil.move(src_path, dest_file_path)
            print(f"Moved: {file}")

    except Exception as e:
        print(f"Error sorting files in {subdir}: {e}")

if __name__ == "__main__":
    src_folder = "Bałagan"  # Replace with the actual source folder path
    dest_folder = "Sorted"  # Replace with the destination folder path

    sort_files_by_extension(src_folder, dest_folder)
