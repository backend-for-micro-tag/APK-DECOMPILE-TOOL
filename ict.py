import subprocess
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

print("ict (INCELL TOOL)")
print("helps you decompile apks from anywhere!")

# Function to decompile the APK using the selected apktool
def decompile_apk(apk_path, apktool_path):
    folder_path = os.path.dirname(apk_path)
    output_dir = os.path.join(folder_path, 'decompiled_apks')
    
    # Check if the output directory exists, and if so, delete it to avoid the "directory exists" error
    if os.path.exists(output_dir):
        print(f"Directory '{output_dir}' already exists. It will be overwritten.")
        subprocess.run(['rm', '-rf', output_dir])  # Remove the existing output directory

    os.makedirs(output_dir)  # Create the output directory again after removal

    try:
        subprocess.run([apktool_path, 'd', apk_path, '-o', output_dir, '-f'], check=True)
        print(f"APK decompiled successfully. Output saved to {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error during APK decompiling: {e}")

# Ask the user for the path to the apktool
apktool_path = input("Please enter the full path to apktool (e.g., /path/to/apktool): ")

# Ask the user to select the APK file using a file dialog
def get_apk_path():
    Tk().withdraw()
    return askopenfilename(title="Select an APK file", filetypes=[("APK files", "*.apk")])

# Get the APK file path
apk_path = get_apk_path()

# Decompile the APK
if apktool_path and apk_path:
    decompile_apk(apk_path, apktool_path)
else:
    print("Both the apktool path and APK file path must be provided.")
