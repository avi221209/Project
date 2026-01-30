import os
import shutil

# CHANGE THIS PATH TO THE FOLDER YOU WANT TO CLEAN
TARGET_FOLDER = r"C:\Users\YourName\Downloads"

# File type mapping
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav"],
    "Python": [".py"],
    "Archives": [".zip", ".rar"]
}

def get_folder_name(extension):
    for folder, extensions in FILE_TYPES.items():
        if extension in extensions:
            return folder
    return "Others"

def clean_folder(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        # Skip directories
        if os.path.isdir(item_path):
            continue

        _, ext = os.path.splitext(item)
        folder_name = get_folder_name(ext.lower())
        folder_path = os.path.join(path, folder_name)

        # Create folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        shutil.move(item_path, folder_path)
        print(f"Moved: {item} → {folder_name}/")

if __name__ == "__main__":
    clean_folder(TARGET_FOLDER)
    print("Folder cleaning completed ✅")
