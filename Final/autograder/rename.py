import sys
import glob
import shutil
import os

def copy_cpp_file(src_path):
    # Find the first matching file with the specified pattern
    cpp_files = glob.glob(f"{src_path}/*.cpp")

    # Check if any matching file is found
    if cpp_files:
        # Take the first matching file
        cpp_file = cpp_files[0]

        # Extract the filename from the path
        filename = os.path.basename(cpp_file)

        # Check if the filename ends with "hw0.cpp" (case-insensitive)
        if filename.lower().endswith(".cpp"):
            # Specify the fixed destination path for copying
            fixed_destination_path = "/autograder/source/final.cpp"

            # Copy the file to the fixed destination path
            shutil.copy(cpp_file, fixed_destination_path)

            # print(f"File {cpp_file} copied to {fixed_destination_path}")
        else:
            print(f"No matching file ending with '.cpp' found. Found: {filename}")
    else:
        print("No matching file found.")

if __name__ == "__main__":
    # Check if the number of command-line arguments is correct
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <source_path>")
        sys.exit(1)

    # Get the source path from command-line arguments
    source_path = sys.argv[1]

    # Call the function to copy the file
    copy_cpp_file(source_path)
