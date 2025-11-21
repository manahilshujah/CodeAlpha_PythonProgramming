# Task Title: Task Automation: Move .jpg Files

## Description
This Python script automates the task of moving all `.jpg` files from a source folder to a destination folder.  
The script was created to simplify and speed up repetitive file management tasks, especially when handling a large number of image files.  

The project was developed using **PyCharm IDE**, which made coding, testing, and debugging easier.

---

## Features
- Automatically detects all `.jpg` files in the source folder
- Moves files to the specified destination folder
- Case-insensitive detection (works for `.JPG` or `.jpg`)
- Avoids overwriting existing files in the destination folder
- Creates the destination folder if it does not exist
- Provides clear messages for each file moved or skipped
- Simple and beginner-friendly

---

## How to Use
1. Open the project in **PyCharm** or any Python IDE.
2. Run the Python script `move_jpg_files.py`.
3. When prompted, enter the **full path of the source folder** containing `.jpg` files:
4. Enter the **full path of the destination folder** where files should be moved:
5. The script will automatically move all `.jpg` files from the source to the destination, skipping files that already exist.  
6. At the end, the script displays the total number of files moved.

---

## Key Concepts Used
- **`os`** → Interact with the operating system for tasks like listing files, joining paths, and checking folder existence.  
- **`shutil`** → Move files from one folder to another.  
- **File Handling** → Access and manage files in the filesystem.  
- **Loops (`for`)** → Iterate through all files in the source folder.  
- **Conditional Statements (`if-else`)** → Check file extension, folder existence, and avoid overwriting.  
- **User Input** → Accept dynamic folder paths from the user.  
- **String Methods (`.lower()`)** → Ensure case-insensitive file detection.

---

## Example Output

Successfully moved

<img width="860" height="218" alt="image" src="https://github.com/user-attachments/assets/90f0d541-fd9c-4c9b-a500-5d736d4c3c77" />

