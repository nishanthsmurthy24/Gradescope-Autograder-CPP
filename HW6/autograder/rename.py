import os
import sys
import shutil

def copy_files(src_path, dest_path):
    # Check if source and destination paths exist
    if not os.path.exists(src_path):
        print(f"Error: Source path '{src_path}' does not exist.")
        return
    if not os.path.exists(dest_path):
        print(f"Error: Destination path '{dest_path}' does not exist.")
        return

    # Get a list of files in the source folder
    files = os.listdir(src_path)

    # Flag to check if any files were copied
    files_copied = False

    # Loop through the files and copy those ending with "_hw5A.cpp", "_hw5B.cpp" and "_hw5C.cpp"
    for file_name in files:
        if file_name.lower().endswith("_hw6a.cpp"):
            src_file_path = os.path.join(src_path, file_name)
            dest_file_path = os.path.join(dest_path, "HW6A.cpp")
            shutil.copy(src_file_path, dest_file_path)
            files_copied = True
        if file_name.lower().endswith("_hw6b.cpp"):
            src_file_path = os.path.join(src_path, file_name)
            dest_file_path = os.path.join(dest_path, "HW6B.cpp")
            shutil.copy(src_file_path, dest_file_path)
            files_copied = True
        if file_name.lower().endswith("_hw6c.cpp"):
            src_file_path = os.path.join(src_path, file_name)
            dest_file_path = os.path.join(dest_path, "HW6C.cpp")
            shutil.copy(src_file_path, dest_file_path)
            files_copied = True

    # Check if no files were copied
    if not files_copied:
        print("Error: No files ending with '_hw6A.cpp' or '_hw6B.cpp' or '_hw6C.cpp' found in the source path.")
        return

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python3 rename.py <source_path> <destination_path>")
    else:
        # Get source and destination paths from command line arguments
        source_path = sys.argv[1]
        destination_path = sys.argv[2]
        copy_files(source_path, destination_path)
