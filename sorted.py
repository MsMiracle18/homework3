import os
import shutil
import threading
from concurrent.futures import ThreadPoolExecutor

def move_file(file_path, destination_folder):
    try:
        shutil.move(file_path, destination_folder)
        print(f"Moved {file_path} to {destination_folder}")
    except Exception as e:
        print(f"Error moving {file_path}: {e}")

def process_directory(input_path, output_path):
    try:
        os.makedirs(output_path, exist_ok=True)
        for item in os.listdir(input_path):
            item_path = os.path.join(input_path, item)
            if os.path.isfile(item_path):
                extension = item.split('.')[-1]
                extension_folder = os.path.join(output_path, extension)
                os.makedirs(extension_folder, exist_ok=True)
                move_file_thread = threading.Thread(target=move_file, args=(item_path, extension_folder))
                move_file_thread.start()
            elif os.path.isdir(item_path):
                process_directory_thread = threading.Thread(target=process_directory, args=(item_path, output_path))
                process_directory_thread.start()
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

if __name__ == "__main__":
    source_folder = "Мотлох"
    destination_folder = "Sorted"
    max_threads = 5  # Кількість одночасно запущених потоків

    with ThreadPoolExecutor(max_threads) as executor:
        process_directory_thread = threading.Thread(target=process_directory, args=(source_folder, destination_folder))
        process_directory_thread.start()


