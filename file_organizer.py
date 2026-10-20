import os
import shutil

folder_to_organize = "./"

file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"]
}

def organize_files():
    for filename in os.listdir(folder_to_organize):
        file_path = os.path.join(folder_to_organize, filename)
        
        if os.path.isdir(file_path) or filename.startswith('.'):
            continue
            
        file_extension = os.path.splitext(filename)[1].lower()
        
        moved = False
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                category_path = os.path.join(folder_to_organize, category)
                if not os.path.exists(category_path):
                    os.makedirs(category_path)
                shutil.move(file_path, os.path.join(category_path, filename))
                print(f"Moved: {filename} -> {category}/")
                moved = True
                break
                
        if not moved and file_extension != '':
            others_path = os.path.join(folder_to_organize, "Others")
            if not os.path.exists(others_path):
                os.makedirs(others_path)
            shutil.move(file_path, os.path.join(others_path, filename))
            print(f"Moved: {filename} -> Others/")

if __name__ == "__main__":
    print("Organizing files...")
    organize_files()
    print("Done organizing!")
