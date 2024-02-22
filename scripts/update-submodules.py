version = '0.1.0'

import os

#!usr/bin/python3
import subprocess

# Example 1: Run a simple shell command
result = subprocess.run("git submodule update --remote", shell=True, check=True)
print("git submodule update --remote exited with return code:", result.returncode)

result = subprocess.run("git submodule status > data/submodules.txt", shell=True, check=True)
print("git status > data/submodules.txt exited with return code:", result.returncode)

from datetime import datetime

# Get the current date
current_date = datetime.now()

# Format the date as a string in 'YYYYMMDD' format
date_string = current_date.strftime(f'%Y%m%d')

print(date_string)

import pandas as pd

print(os.getcwd())

# Assuming your data is in a file named 'your_data.txt' and has space-separated values
file_path = 'data/submodules.txt'

# Read the space-separated data into a DataFrame
df = pd.read_csv(file_path, delimiter=' ', header=None)
df.columns = ["NaN", "hash", "name", "refs"]

# Display the DataFrame
print(df)

def replace_line(file_path, search_prefix, new_line):
    # Read the content of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the line starting with the specified prefix
    for i, line in enumerate(lines):
        if line.startswith(search_prefix):
            print(f'Replacing:\n{lines[i]} with {new_line}')
            lines[i] = new_line
            break  # Assuming you want to replace only the first matching line

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

for i, row in df.iterrows():
    if row["name"] == "cosmic-workspaces-epoch":
        row["name"] = "cosmic-workspaces"
    elif row["name"] == "launcher":
        row["name"] == "pop-launcher"
    elif row["name"] == "simple-wrapper":
        continue
    print("row:    ",row)
    print(f'{row["name"]} is now at commit {row["hash"]}')
    # Example usage
    file_path = f'specfiles/{row["name"]}.spec'
    search_prefix = f'%global commit '
    new_line = f'%global commit {row["hash"]}\n'

    replace_line(file_path, search_prefix, new_line)

    ver_string = f'{version}~{date_string}.{row["hash"][:6]}'

    print("New version string:",ver_string)

    search_prefix = f'Version:        '
    new_line = f'Version:        {ver_string}\n'

    replace_line(file_path, search_prefix, new_line)


