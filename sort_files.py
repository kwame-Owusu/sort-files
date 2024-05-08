import os
import shutil

downloads_path = os.path.expanduser("~/Downloads")
images_folder = os.path.expanduser("~/Downloads/images_folder")
doc_folder = os.path.expanduser("~/Downloads/doc_folder")
pdf_folder = os.path.expanduser("~/Downloads/pdf_folder")

# Create directories if they don't exist
for folder in [images_folder, doc_folder, pdf_folder]:
    os.makedirs(folder, exist_ok=True)

def move_images():
    for file in os.listdir(downloads_path):
        if file.lower().endswith((".png", ".jpg", ".gif")):
            file_path = os.path.join(downloads_path, file)
            try:
              shutil.move(file_path, pdf_folder)
              print(f"Moved {file} successfully to Images folder.")
            except FileExistsError:
                shutil.move(file_path, downloads_path)
                print(f"Overridden {file} in Images folder")

def move_documents():
    for file in os.listdir(downloads_path):
        if file.lower().endswith((".doc", ".docx", ".pptx")):
            file_path = os.path.join(downloads_path, file)
            try:
              shutil.move(file_path, pdf_folder)
              print(f"Moved {file} successfully to DOC folder.")
            except FileExistsError:
                shutil.move(file_path, downloads_path)
                print(f"Overridden {file} in DOC folder")

def move_pdf():
    for file in os.listdir(downloads_path):
        if file.lower().endswith(".pdf"):
            file_path = os.path.join(downloads_path, file)
            try:
              shutil.move(file_path, pdf_folder)
              print(f"Moved {file} successfully to PDF folder.")
            except FileExistsError:
                shutil.move(file_path, downloads_path)
                print(f"Overridden {file} in PDF folder")

# Call functions to move files
try:
    move_documents()
    move_images()
    move_pdf()
except Exception as e:
    print(f"Error: {e}")
else:
    print("No files to move.")
