import os
import json

def combine_and_filter_jsonl_files(input_directory, output_file, relevance_threshold=0.7):
    combined_data = []

    # Iterate over all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.jsonl'):
            file_path = os.path.join(input_directory, filename)
            with open(file_path, 'r') as file:
                for line in file:
                    data = json.loads(line)
                    relevance_score = data.get('CRITERIA', {}).get('CRITERIA_scores', {}).get('Relevance', 0)
                    if relevance_score >= relevance_threshold:
                        combined_data.append(data)

    # Write the combined and filtered data to the output file
    with open(output_file, 'w') as outfile:
        for entry in combined_data:
            json.dump(entry, outfile)
            outfile.write('\n')

# Specify the input directory and output file path
input_directory = os.path.expanduser('inputfiledirectory')
output_file = os.path.expanduser('outputfiledirectory')

# Call the function to combine and filter the JSONL files
combine_and_filter_jsonl_files(input_directory, output_file)

print(f"Combined and filtered data has been saved to {output_file}")
