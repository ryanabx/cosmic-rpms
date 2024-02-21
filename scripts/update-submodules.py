#!usr/bin/python3
import subprocess

# Example 1: Run a simple shell command
result = subprocess.run("git submodule update --remote", shell=True, check=True)
print("git submodule update --remote exited with return code:", result.returncode)

result = subprocess.run("git status > data/submodules.txt", shell=True, check=True)
print("git status > data/submodules.txt exited with return code:", result.returncode)

import pandas as pd

# Assuming your data is in a file named 'your_data.txt' and has space-separated values
file_path = 'data/submodules.txt'

# Read the space-separated data into a DataFrame
df = pd.read_csv(file_path, delimiter=' ')

# Display the DataFrame
print(df)

def replace_line(file_path, search_prefix, new_line):
    # Read the content of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the line starting with the specified prefix
    for i, line in enumerate(lines):
        if line.startswith(search_prefix):
            lines[i] = new_line
            break  # Assuming you want to replace only the first matching line

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

for row in df.iterrows():
    # Example usage
    file_path = f'specfiles/{row[1]}.txt'
    search_prefix = f'%global commit '
    new_line = f'%global commit ${row[0]}\n'

    replace_line(file_path, search_prefix, new_line)
