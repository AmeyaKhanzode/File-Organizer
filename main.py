import os
import shutil
directory = os.path.join(os.path.expanduser("~"), "Desktop")    #no need to define path, just write the folder name

extensions = {
    ".jpg" : "Images",
    ".jpeg" : "Images",
    ".png" : "Images",
    ".mp4" : "Videos",                  #more extensions can be added
    ".doc" : "Documents",
    ".pdf" : "Documents",
    ".txt" : "Documents",
    ".csv" : "Documents"
}

for filename in os.listdir(directory):
    current_file_path = os.path.join(directory, filename)

    if os.path.isfile(current_file_path):
        extension = os.path.split(filename)[1].lower()

        if extension in extensions:
            destination_folder_name = extensions[extension]

            current_folder_path = os.path.join(directory, destination_folder_name)
            os.mkdir(current_folder_path, exist_ok = True)

            destination_file_path = os.path.join(current_folder_path, filename)
            shutil.move(current_file_path, destination_file_path)

            print(f"Moved {filename} to {destination_folder_name} folder.")
    
    else:
        print("It is a directory.")

print("All files are organised.")