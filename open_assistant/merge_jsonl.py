import os
import json

def merge_jsonl_files(directory, output_file):
    unique_lines = set()

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".jsonl"):
            with open(os.path.join(directory, filename), 'r') as file:
                for line in file:
                    unique_lines.add(line.strip())

    # Write the unique lines to the output file
    with open(output_file, 'w') as outfile:
        for line in unique_lines:
            outfile.write(line + "\n")

if __name__ == "__main__":
    downloads_folder = os.path.expanduser("INPUT_FOLDER_PATH") # Change this to the folder where your JSONL files are stored
    output_file = os.path.join(downloads_folder, "OUTPUT_FILE_NAME.jsonl") # Change this to the name of the output file
    merge_jsonl_files(downloads_folder, output_file)
    print(f"Merged file saved to {output_file}")