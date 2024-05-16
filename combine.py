import os

def read_and_combine(folder_path):
    combined_lines = []
    
    # Walk through all files in the given folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            # Construct full file path
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    # Strip whitespace from the beginning and end of the line
                    stripped_line = line.strip()
                    # Check if the line is not empty and does not start with //
                    if stripped_line and not stripped_line.startswith('//'):
                        combined_lines.append(stripped_line)

    return combined_lines

def save_to_file(lines, output_path):
    # Write all lines to the specified file
    with open(output_path, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + '\n')  # Add newline to separate the lines

# Usage
folder_path = './rules'  # Replace with your folder path
output_path = 'rules_combined.txt'   # The file where you want to save the output

# Read and combine lines
result = read_and_combine(folder_path)

# Save the combined lines to a file
save_to_file(result, output_path)

print(f"Combined lines saved to {output_path}")
