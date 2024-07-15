import json
import os

# Path to the input JSONL file
input_file_path = os.path.expanduser("PATH_TO_INPUT_FILE.jsonl") # Replace with the actual path to the input file

# Path to the output filtered JSONL file
output_filtered_file_path = os.path.expanduser("PATH_TO_OUTPUT_FILE.jsonl") # Replace with the actual path to the output file

def filter_and_deduplicate_message_trees(input_file, output_file):
    seen_lines = set()
    lines_written = 0  # Counter to track the number of lines written
    lines_processed = 0  # Counter to track the number of lines processed

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            lines_processed += 1
            data = json.loads(line)
            criteria_score = data.get("prompt", {}).get("CRITERIA", {})
            # Debugging output
            print(f'CRITERIA: {criteria_score}')
            relevance_score = criteria_score.get("Relevance", 0)
            print(f'Relevance score: {relevance_score}')
            if relevance_score > 0.4:  # Adjust the threshold to filter out greater or lesser relevance scores
                if line not in seen_lines:
                    outfile.write(line)
                    seen_lines.add(line)
                    lines_written += 1

    print(f'Number of lines processed: {lines_processed}')
    print(f'Number of lines written: {lines_written}')

filter_and_deduplicate_message_trees(input_file_path, output_filtered_file_path)

print(f'Filtered and deduplicated file created at: {output_filtered_file_path}')