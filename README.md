# File & Folder Organizer

## Overview

The **File_and_Folder_Organizer** is a Python script designed to help you efficiently organize a large number of files into a structured folder hierarchy. It's particularly useful when you have a substantial number of files to manage and want to divide them into manageable groups for better organization and easier access.

## Key Features

- **Automatic Folder Creation**: The script automatically creates folders with a customizable naming pattern.

- **Bulk File Distribution**: It moves files from a source directory into the newly created folders, ensuring each folder contains a specified maximum number of files (default: 9998).

- **User-Friendly**: The script prompts the user to input the number of files to be organized and the source directory containing the files to be moved.

## Usage

1. Run the script.
2. Enter the number of files you want to organize.
3. Provide the source directory containing the files to be organized.
4. The script will create the necessary folders and distribute files accordingly.

## Example

Suppose you have 30,000 files to organize. The script will create four folders (by default) with up to 9998 files each:

- `civitai_wildcard_prompt_1`
- `civitai_wildcard_prompt_2`
- `civitai_wildcard_prompt_3`
- `civitai_wildcard_prompt_4`

This makes managing large collections of files much more efficient.

## Requirements

- Python 3.x
- The `shutil` and `math` modules are used, but they are part of the Python standard library.

## How to Run

1. Clone this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using the `python` command:

   ```bash
   python File_and_Folder_Organizer.py
