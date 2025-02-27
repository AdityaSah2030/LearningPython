"""
This script demonstrates:
1. Opening, writing, and reading text files.
2. Using context managers (the "with" statement) for safe file operations.
3. File modes: 'r', 'w', 'a', and 'r+'.
4. Appending to files and verifying the content.
5. Working with binary files.
6. Optional cleanup of created files.

How to run:
    python 09_files.py

Note:
    This script creates and modifies files in the current directory.
"""

import os

# ------------------------------------------------------------------------------
# SECTION 1: Writing to a File
# ------------------------------------------------------------------------------
print("=== SECTION 1: WRITING TO A FILE ===")

# Define the file name and content to write
file_name = "example.txt"
content = "Hello, this is a sample file.\nThis is the second line.\n"

# Using 'w' mode: Creates a new file or overwrites an existing one.
with open(file_name, "w") as file:
    file.write(content)
print(f"Content written to {file_name} using write mode ('w').\n")

# ------------------------------------------------------------------------------
# SECTION 2: Reading from a File
# ------------------------------------------------------------------------------
print("=== SECTION 2: READING FROM A FILE ===")

# Using 'r' mode: Opens the file for reading.
with open(file_name, "r") as file:
    read_content = file.read()
print("Content read from the file:")
print(read_content)

# ------------------------------------------------------------------------------
# SECTION 3: Appending to a File
# ------------------------------------------------------------------------------
print("=== SECTION 3: APPENDING TO A FILE ===")

# Using 'a' mode: Opens the file for appending; content is added to the end.
append_content = "This line was appended to the file.\n"
with open(file_name, "a") as file:
    file.write(append_content)
print(f"Content appended to {file_name} using append mode ('a').\n")

# Read the file again to show the appended content
with open(file_name, "r") as file:
    updated_content = file.read()
print("Content after appending:")
print(updated_content)

# ------------------------------------------------------------------------------
# SECTION 4: Using 'r+' Mode (Read and Write)
# ------------------------------------------------------------------------------
print("=== SECTION 4: USING 'r+' MODE (READ AND WRITE) ===")

# 'r+' mode allows reading and writing without truncating the file.
with open(file_name, "r+") as file:
    # Read the first line
    first_line = file.readline()
    print("First line:", first_line.strip())
    
    # Write a new line at the current pointer position (at the end of current content)
    file.write("New line added in r+ mode.\n")
    
    # Move the pointer back to the beginning to read the full updated content
    file.seek(0)
    full_content = file.read()
print("Updated content after using r+ mode:")
print(full_content)

# ------------------------------------------------------------------------------
# SECTION 5: Binary Mode (Optional)
# ------------------------------------------------------------------------------
print("=== SECTION 5: BINARY MODE ===")

# Demonstrate writing and reading in binary mode
binary_file = "example_binary.bin"
binary_data = bytes([50, 100, 150, 200])  # Some sample binary data

# Write binary data using 'wb' mode
with open(binary_file, "wb") as bfile:
    bfile.write(binary_data)
print(f"Binary data written to {binary_file} using 'wb' mode.")

# Read binary data using 'rb' mode
with open(binary_file, "rb") as bfile:
    read_binary = bfile.read()
print("Binary data read from the file:", list(read_binary))

# ------------------------------------------------------------------------------
# SECTION 6: Cleanup (Optional)
# ------------------------------------------------------------------------------
print("=== SECTION 6: CLEANUP ===")

# Optionally remove the created files to clean up
try:
    os.remove(file_name)
    os.remove(binary_file)
    print("Cleanup: Created files removed.")
except Exception as e:
    print("Cleanup error:", e)

# ------------------------------------------------------------------------------
# END OF SCRIPT
# ------------------------------------------------------------------------------
print("\nEnd of 09_files.py")
